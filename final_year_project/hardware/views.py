from django.shortcuts import render,HttpResponse
import random
from .models import hdata
from detail.models import crop
def data(request,Did,pk1,pk2,pk3):
    did=Did.lower()
    pk1=pk1
    pk2=pk2
    pk3=pk3
    hdata.objects.create(Did=did,temp=pk1,ph=pk2,moisture=pk3).save()
    pk=str(Did)+' '+str(pk1)+" "+str(pk2)+' '+str(pk3)
    return HttpResponse(random.randint(0, 3))
def data1(request):
    data=hdata.objects.all()
    s='<table><tr><th>Device ID</th><th>Moisture</th><th>Temperature</th><th>pH</th></tr>'
    for i in data:
        s+='<tr><td>'+i.Did+'</td><td>'+str(i.moisture)+'</td><td>'+str(i.temp)+'</td><td>'+str(i.ph)+'</td></tr>'
    s+='</table>'

    return HttpResponse(s)

# Create your views here.

#from .modles import hdata


 #   hdata.objects.create(Did=did,temp=pk1,ph=pk2,moisture=pk3)
  #  hdata.save()