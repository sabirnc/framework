from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def testwest(request):
    return HttpResponse("hi this my first response")
def testeast(request):
    # return HttpResponse("hello welcome")
    return render(request,'south.html')

