from django.shortcuts import render
from django.http import HttpResponse
from .models import Process

def scheduling(request):
    if request.method == 'POST':
        # Handle user input and scheduling logic here
        # Update the Process model with user input and scheduling results
        # Redirect to the results page

    return render(request, 'sjf_app/scheduling.html')

def results(request):
    # Retrieve and display scheduling results from the Process model
    return render(request, 'sjf_app/results.html')
