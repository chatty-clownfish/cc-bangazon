from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
  # return HttpResponse("Hello, world. You're at the Death Star index.")
  print("REQUEST", request)
  return render(request, 'history/index.html')



# def index(request):
#   return render(request, 'HR/index.html')

  # def index(request):
  # # return HttpResponse("Welcome to the music database.")
  # print("REQUEST", request)
  # artist_list = Artist.objects.order_by('name')
  # context = {'artist_list': artist_list}
  # return render(request, 'history/index.html', context)

  