from django.shortcuts import render


def home(request):
    return HttpResponse('Olá Mundo!')


def about(request):
    return HttpResponse('About')


def contact(request):
    return HttpResponse('Contact')
