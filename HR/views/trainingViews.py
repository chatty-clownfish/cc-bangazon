from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from HR.models import Training, EmployeeTraining
from django.utils import timezone

def trainingList(request):
    now = timezone.now()
    training_list = Training.objects.filter(start_date__gte=now)
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

def trainingDetails(request, id):
  training = get_object_or_404(Training, pk= id)
  employeetraining = EmployeeTraining.objects.filter(training_id = id)
  context = { 'training' : training, 'employeetraining' : employeetraining}
  return render(request, 'HR/training/trainingDetail.html', context)

def training_delete(self, id):
    print(id)
    training = get_object_or_404(Training, pk= id)
    # print(training)
    training.delete()
    return HttpResponseRedirect(reverse("HR:trainings"))
