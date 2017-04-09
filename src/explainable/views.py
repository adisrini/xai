from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world. You are at the explainable index.")

def flip(request):
    return HttpResponse("You're looking at the flip module.")
