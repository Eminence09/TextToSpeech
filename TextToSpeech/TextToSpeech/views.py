from django.http import HttpResponse
from django.shortcuts import render
from win32com.client import Dispatch
import os
import pythoncom


def index(request):
    return render(request, "index.html")

def index2(request):
    return render(request, "index2.html")

def card2(request):
    return render(request, "In-CardDepth/card2.html")

# def my_function(request):
#     return HttpResponse("Success!")


def speak(request):
    pythoncom.CoInitialize()
    userinput = request.POST.get('userinput')
    speak = Dispatch("SAPI.SpVoice").Speak
    op = userinput
    speak(op)
    return render(request, "In-CardDepth/card2.html")