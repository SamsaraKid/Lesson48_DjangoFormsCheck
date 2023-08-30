from django.shortcuts import render, redirect
from .myforms import *


def index(req):
    return render(req, 'index.html')


def def1(req):
    print(1)
    if req.method == 'POST':
        print(2)
        anketa = UserFormComment(req.POST)
        if anketa.is_valid():
            print(3)
            name = anketa.cleaned_data.get('name')
            email = anketa.cleaned_data['email']
            comm = anketa.cleaned_data.get('comm')
            print(name, email, comm)
        else:
            print('ошибка заполнения формы')
    else:
        anketa = UserFormComment()
    data = {'form': anketa}
    return render(req, 'forma.html', context=data)


def def2(req):
    print(1)
    if req.method == 'POST':
        print(2)
        anketa = UserFormErrors(req.POST)
        if anketa.is_valid():
            print(3)
            name = anketa.cleaned_data.get('name')
            num = anketa.cleaned_data['num']
            agree = anketa.cleaned_data.get('agree')
            print(name, num, agree)
            return redirect('index')
        else:
            print('ошибка заполнения формы')
            print(anketa.errors)
    else:
        anketa = UserFormErrors()
    data = {'form': anketa}
    return render(req, 'forma.html', context=data)


def def3(req):
    print(1)
    if req.method == 'POST':
        print(2)
        anketa = UserFormValidator(req.POST)
        if anketa.is_valid():
            print(3)
            name = anketa.cleaned_data.get('name')
            code = anketa.cleaned_data['code']
            tel = anketa.cleaned_data.get('tel')
            print(name, code, tel)
            return redirect('index')
        else:
            print('ошибка заполнения формы')
            print(anketa.errors)
    else:
        anketa = UserFormValidator()
    data = {'form': anketa}
    return render(req, 'forma.html', context=data)


