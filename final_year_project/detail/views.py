from django.shortcuts import render,HttpResponse
import json
from django.forms.models import model_to_dict
from .models import crop,land
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.
def blog(request):
     details={}
     lands=land.objects.all()
     '''for i in lands:
          details[str(i.name)] =[i.pk]
          for j in crop.objects.all().filter(land_type=str(i.name).lower()):
               details[str(i.name)].append(j)
          print(details[i.name])'''
     crops=crop.objects.all()[:15]
     lands = land.objects.all()
     return render(request, 'detail/blog.html',locals())
def about(request):
     crops = crop.objects.all()[:2]
     return render(request, 'detail/about.html',locals())
def land_detail(request,offset):
     lands=land.objects.all()
     landselected=land.objects.get(pk=offset)
     print(landselected.name)
     crops=crop.objects.all().filter(land_type=landselected.name.lower())
     return render(request, 'detail/blog.html',locals())
def crop_detail(request,offset):
     lands = land.objects.all()
     cropselected=crop.objects.get(pk=offset)
     return render(request,'detail/single.html',locals())

def search(request):
     item=request.GET['item']
     crops=crop.objects.all().filter(name__icontains=item)
     lands = land.objects.all()
     return render(request, 'detail/blog.html',locals())

def cropsinland(request,offset):
    offset=offset+' soil'
    crops=crop.objects.all().filter(land_type=offset.lower())
    s="<select name=\"cropselected\" id=\"crops\">"
    for i in crops:
        s+=f'<option value={i.name}>{i.name}</option>'
    s+="</select>"
    return HttpResponse(s)














