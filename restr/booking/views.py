from django.shortcuts import render
from django.contrib import messages
from .forms import BookTableForm, DivErrorList
from .utils import print_parameters
from .models import BookTable


# Create your views here.
def index(request):

    if request.method == "POST":
        form = BookTableForm(request.POST, error_class=DivErrorList)
    else:
        form = BookTableForm()

    if request.method == "POST":
        form = BookTableForm(request.POST, error_class=DivErrorList)
        if form.is_valid():
            print_parameters(form)
            # save_booking(form)
            messages.success(request, "Your booking has been sent.")
            form = BookTableForm()

    return render(request, 'booking/form.html', {"form": form})


def save_booking(form):
    table = BookTable()

    table.name = form.cleaned_data["name"]
    table.email = form.cleaned_data["email"]
    table.phone = form.cleaned_data["phone"]
    table.date = form.cleaned_data["date"]
    table.time = form.cleaned_data["time"]
    table.no_of_people = form.cleaned_data["no_of_people"]
    table.message = form.cleaned_data["message"]

    table.save()