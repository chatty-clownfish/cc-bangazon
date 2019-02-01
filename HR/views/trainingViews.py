from django.shortcuts import render, redirect, get_object_or_404
from HR.models import Training, EmployeeTraining
from django.utils import timezone
from datetime import datetime, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse



def trainingList(request):
    now = timezone.now()
    training_list = Training.objects.filter(start_date__gte=now)
    context = {'training_list': training_list}
    return render(request, 'HR/training/training.html', context)


def add_training_program(request):
    if request.method == "POST":
        name = request.POST['training_name']
        start_date = request.POST['training_startDate']
        end_date = request.POST['training_endDate']
        maxAttendees = request.POST['training_maxEnrollment']
        t = Training(name=name, start_date=start_date,
                     end_date=end_date, maxAttendees=maxAttendees)
        t.save()
        response = redirect('HR:trainings')
        return response
    if request.method == "GET":
        return render(request, 'HR/training/addTraining.html')


def trainingDetails(request, id):
    training = get_object_or_404(Training, pk=id)
    employeetraining = EmployeeTraining.objects.filter(training_id=id)
    context = {'training': training, 'employeetraining': employeetraining}
    return render(request, 'HR/training/trainingDetail.html', context)


def edit_training_form(request, id):
    training = get_object_or_404(Training, pk=id)
    start_date = str(training.start_date)
    startDateNonString = training.start_date
    end_date = str(training.end_date)
    print("training start date: ", training.start_date)
    print("training end date: ", training.end_date)
        # go to our join table filter through and find any rows where the ids match
    attendees = EmployeeTraining.objects.filter(
            training_id=id)
    td = timedelta(days=4)

    if end_date <= start_date:
        end_date = str(startDateNonString + td)
        print("new end date: ", end_date)
        context = {'training': training, 'attendees': attendees,
                    'start_date': start_date, 'end_date': end_date}
        print("context", context)
        return render(request, 'HR/training/editTraining.html', context)
