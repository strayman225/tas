from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def home(request):
    return render(request,'base/home.html')

def upload(request):
    if request.method == "POST":
        uploadfile = request.FILES["file"]
        document = fileupload.objects.create(file=uploadfile)
        document.save()
        return HttpResponse("Your file as uploaded")
    
    return render (request,"base/upload.html")



def display_records(request):
    records = upload.objects.all()
    return render (request,"warehouse/records.html",{'records':records})

