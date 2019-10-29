import http.client, urllib, base64, uuid,json,datetime,multiprocessing

from django.shortcuts import render, redirect  
from MOMO_TASK.models import MRequest 
from MOMO_TASK.forms import MRequestForm
from MOMO_TASK.task import add_tasks,run
from MOMO_TASK.momoRequest import momoCollect,momoDisburse
from  MOMO_TASK.config import globalParams


def collect(request):  
    if request.method == "POST":  
        print (request.POST)
        form = MRequestForm(request.POST)  
        print(form.is_valid())
        if form.is_valid():  
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ save form data into db ')
                x = form.save()
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ call collect api ')
                refId = momoCollect(x)
                if(refId != 'None'):
                 x.rid = refId
                 x.rtype = 'requesttopay'
                 x.rcreationTime = datetime.datetime.now()
                 x.save()
                 print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ add collect request to Queue ')
                 add_tasks(refId)
                 if(globalParams.run == True):
                  run()      
                 print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ retrun after finish ')                  
                return render(request,'collect.html',{'form':form}) 
    else:
        form = MRequestForm()  
    return render(request,'collect.html',{'form':form}) 
    
def disburse(request):  
    if request.method == "POST":  
        form = MRequestForm(request.POST)  
        if form.is_valid():  
                x = form.save()
                refId = momoDisburse(x)
                if(refId != 'None'):
                 x.rid = refId
                 x.rtype = 'transfer'
                 x.rcreationTime = datetime.datetime.now()
                 x.save()
                 add_tasks(refId)
                 if(globalParams.run == True):
                  run()                          
                return render(request,'disburse.html',{'form':form}) 
    else:
        form = MRequestForm()  
    return render(request,'disburse.html',{'form':form}) 
