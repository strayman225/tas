from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import MyFileForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'base/home.html')

def upload(request):
    myform = MyFileForm()
    context={'form':myform}
    return render (request,"base/upload.html", context)



def display_records(request):
    records = upload.objects.all()
    return render (request,"warehouse/records.html",{'records':records})
   


def uploadfile(request):
    if request == "POST":
        myform = MyFileForm(request.POST,request.FILES)
        if myform.is_valid():
            MyFileName = request.POST.get('file_name')
            MyFile = request.FILES.get('file')
            MyFileForm.objects.create(information=MyFileName, file=MyFileName).save()
            messages.success(request,"File Uploaded Succesfully.")
    return redirect("home_html")
    