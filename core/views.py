from django.shortcuts import render
from .models import Patient

def home(request):
    patients = Patient.objects
    return render(request, 'index.html', {'patients': patients})