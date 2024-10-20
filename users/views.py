from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from .forms.register import RegisterForm

# Create your views here.

def register(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/account/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})