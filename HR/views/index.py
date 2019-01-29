from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
  # return HttpResponse("Hello, world. You're at the Death Star index.")
  print("REQUEST", request)
  return render(request, 'HR/index.html')