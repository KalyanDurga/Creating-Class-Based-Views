from typing import Any, Dict
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *

def fbv_string(request):
    return HttpResponse('this is function based view')

class CBV_string(View):
    def get(self,request):
        return HttpResponse('This is class Based Viewww')
    
class fbv_html(View):
    def get(self,request):
        return render(request,'fbv_html.html')
# this is function view for form

def fbv_form(request):
    TFO=Topicform()
    WFO=Webpageform()
    d={'TFO':TFO,'WFO':WFO}
    if request.method=='POST':
        TD=Topicform(request.POST)
        WD=Webpageform(request.POST)
        if TD.is_valid() and WD.is_valid():
            TFD=TD.save(commit=False)
            TFD.save()
            WFD=WD.save(commit=False)
            WFD.topic_name=TFD
            WFD.save()
            return HttpResponse('data submited')
        return HttpResponse('data is not valid')

    return render(request,'fbv_form.html',d)

class CBV_form(View):
    def get(self,request):
        TFO=Topicform()
        WFO=Webpageform()
        d={'TFO':TFO,'WFO':WFO}
        return render(request,'CBV_form.html',d)
    def post(self,request):
        TFD=Topicform(request.POST)
        WFD=Webpageform(request.POST)
        if TFD.is_valid() and WFD.is_valid():
            TD=TFD.save(commit=False)
            TD.save()

            WD=WFD.save(commit=False)
            WD.topic_name=TD
            WD.save()
            return HttpResponse('data inserteds')

# this is template view

class CBT_template(TemplateView):
    template_name='CBT_template.html'

    def get_context_data(self, **kwargs):
        CO=super().get_context_data(**kwargs)
        TFO=Topicform()
        WFO=Webpageform()
        CO['TFO']=TFO
        CO['WFO']=WFO

        return CO
    
    def post(self,request):
        TD=Topicform(request.POST)
        WD=Webpageform(request.POST)
        if TD.is_valid() and WD.is_valid():
            TFD=TD.save(commit=False)
            TFD.save()

            WFD=WD.save(commit=False)
            WFD.topic_name=TFD
            WFD.save()
            return HttpResponse('data submited')
        else:
            return HttpResponse('data is not valid')
            




