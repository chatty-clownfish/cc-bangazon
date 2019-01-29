from django.shortcuts import render, redirect
from HR.models import Training


def trainingList(request):
    training_list = Training.objects.all()
    context = { 'training_list' : training_list }
    return render(request, 'HR/training/training.html', context)

def addTraining(request):
    context = { 'hello' : 'hello' }
    return render(request, 'HR/training/addTraining.html', context)

def add_training_program(request):
  name = request.POST['training_name']
  start_date= request.POST['training_startDate']
  end_date = request.POST['training_endDate']
  maxEnrollment = request.POST['training_maxEnrollment']
  t = Training(name = name, startDate = start_date, endDate = end_date, maxEnrollment = maxEnrollment)
  t.save()
  response = redirect('./training')
  return response

