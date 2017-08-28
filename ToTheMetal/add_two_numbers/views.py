from django.shortcuts import render
from django.http import HttpResponse

def add_two_numbers_page(request):
    """Add two numbers"""
    if request.method == "GET":
        return HttpResponse("GET Not implemented yet")
    elif request.method == "POST":
        return HttpResponse("POST Not implemented yet")
