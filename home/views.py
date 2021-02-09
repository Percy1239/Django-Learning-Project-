from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    #return HttpResponse("This is my homepage (/)")
    context = {'name':'Paresh','game':'cricket'}
    return render(request,'home.html', context)

def about(request):
    #return HttpResponse("This is my homepage (/about)")
    return render(request,'about.html')

def project(request):
    #return HttpResponse("This is my homepage (/project)")
    return render(request,'project.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        #print(name, email, phone, desc)
        details = Contact(name = name , email = email , phone = phone , desc = desc)
        details.save()
        print("DAta saveed to db")
    #return HttpResponse("This is my homepage (/contact)")
    return render(request,'contact.html')

    