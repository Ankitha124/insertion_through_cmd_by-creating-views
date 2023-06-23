from django.shortcuts import render
from django.http import HttpResponse
from app.models import*
# Create your views here.

def insert_topic(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('<h1>topic is inserted</h1>')


def insert_webpage(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')

    WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('<h1>Web page is created')


def insert_accessrecord(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    d=input('enter date')
    a=input('enetr author')

    WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()

    AO=AccessRecords.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()
    return HttpResponse('<h1> Access record is created')
    