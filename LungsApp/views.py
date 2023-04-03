from django.shortcuts import render, HttpResponse

# Create your views here.


def lungs(request):
    # return HttpResponse("Hello")
    return render(request, 'lungs.html')
