from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def student_list(request):
    return HttpResponse("List of students will be displayed here.")
