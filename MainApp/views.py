from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Hello")
    return render(request,'index.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
