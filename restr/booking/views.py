from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from .forms import BookTableForm, DivErrorList
from .utils import print_parameters
from .models import BookTable

def index(request):
    """ Main view """
    
    if request.method == "POST":
        form = BookTableForm(request.POST, error_class=DivErrorList)
    else:
        form = BookTableForm()

    if request.method == "POST":
        if form.is_valid():
            print_parameters(form)
            # save_booking(form)
            messages.success(request, "Your booking has been sent. You'll get a confirmation email.")
            form = BookTableForm()

    return render(request, 'home.html', {"form": form})


def save_booking(form):
    """ The method saves the booking to the database."""

    table = BookTable()
    table.name = form.cleaned_data["name"]
    table.email = form.cleaned_data["email"]
    table.phone = form.cleaned_data["phone"]
    table.date = form.cleaned_data["date"]
    table.time = form.cleaned_data["time"]
    table.no_of_people = form.cleaned_data["no_of_people"]
    table.message = form.cleaned_data["message"]

    table.save()



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"
