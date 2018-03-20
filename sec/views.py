# -*- coding: utf-8 -*-
import datetime
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from models import Blog
from random import choice
import time
# Create your views here.
def home(request):
    context = {}
    weeks=Blog.objects.values('week')
    weekblogs = {}
    if weeks:
        now=weeks.last()['week']
        for w in range(1,now+1):
            weekblogs[str(w)]=[]
            blog=Blog.objects.filter(week=w)
            print blog.count()
            if blog.count()<=5:
                m=blog.count()
            else:
                m=5
            for b in range(0,m):
                # print str(w)
                # print weekblogs
                weekblogs[str(w)].append(blog[b])
    context['weekblogs'] =weekblogs
    return render(request, 'index.html',context)
@login_required
def submit(request):
    context = {}
    context['statu'] = '0'
    if request.method == 'POST':
        content = request.POST.get('content')
        url = request.POST.get('url')
        direction=request.POST.get('direction')
        weeks = datetime.datetime.now().isocalendar()
        week=weeks[1]-11
        blog = Blog()
        blog.blog_user=User.objects.get(username=request.session['username'])
        blog.content=content
        blog.url=url
        blog.direction=direction
        blog.time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        blog.week=week
        blog.save()
        context['statu'] = '1'
        context['error'] = "提交成功"
        return HttpResponseRedirect('/blog/'+str(week)+'/')
    return render(request, 'submit.html',context)
def user_login(request):
    context = {}
    context['statu'] = '0'
    if request.method == 'POST':
        get_name = request.POST.get('username')
        get_password = request.POST.get('password')
        print get_name
        print get_password
        user = authenticate(username=get_name, password=get_password)
        if user is not None:
            if user.is_active:
                request.session['username'] = get_name
                context['name'] = get_name
                request.session['id'] = user.id
                login(request, user)  # 这才是登录，才会写入session
                return HttpResponseRedirect('/')
            else:
                context['statu'] = '1'
                context['error'] = "您的用户已经被限制,请联系工作人员"
                # print('密码正确，但是用户无法登录')
        else:
            context['statu'] = '1'
            context['error'] = "用户名或者密码错误"
    return render(request, 'login.html', context)
def register(request):
    context = {}
    context['statu']=0
    if request.method == 'POST':
        name = request.POST.get('name')
        u=User.objects.filter(username=name)
        if u:
            context['statu'] = 1
            context['error'] = '该名字已被使用'
            return render(request, 'register.html', context)
        password = request.POST.get('password')
        email = request.POST.get('eamil')
        print name
        print password
        user = User.objects.create_user(name,email, password)
        user.first_name=request.POST.get('firstname')
        user.save()
        context['name'] = name
        return render(request, 'login.html', context)
    return render(request, 'register.html', context)
def weekblog(request,week):
    context = {}
    blogs=Blog.objects.filter(week=week)
    context['blogs']=blogs
    context['week'] = week
    u = User.objects.values('id')

    man=choice(u)
    context['man'] = man['id']
    return render(request, 'weekblog.html', context)
def myblog(request,user_id):
    context = {}
    blogs = Blog.objects.filter(blog_user_id=user_id)
    context['blogs'] = blogs
    return render(request, 'myblog.html', context)
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
