from django.shortcuts import render, redirect
from HR.models import Training


def trainingList(request):
    training_list = Training.objects.all()
    context = {'training_list': training_list}
    return render(request, 'HR/training/training.html', context)


def add_training_program(request):
    if request.method == "POST":
        name = request.POST['training_name']
        start_date= request.POST['training_startDate']
        end_date = request.POST['training_endDate']
        maxAttendees = request.POST['training_maxEnrollment']
        t = Training(name = name, start_date = start_date, end_date = end_date, maxAttendees = maxAttendees)
        t.save()
        response = redirect('HR:trainings')
        return response
    if request.method == "GET":
        return render(request, 'HR/training/addTraining.html')
    
