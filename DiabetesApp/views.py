from django.shortcuts import render, HttpResponse

# Create your views here.


def diabetes(request):
    # return HttpResponse("Hello")
    return render(request, 'diabetes.html')
