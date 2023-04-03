from django.shortcuts import render, HttpResponse
from HeartApp.heart import Classification
# Create your views here.

#1
def heart(request):
    # return HttpResponse("Hello")
    return render(request, 'heart.html')

