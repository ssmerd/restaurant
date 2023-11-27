from django.shortcuts import render
from .forms import BookTableForm


# Create your views here.
def index(request):

    if request.method == "POST":
        form = BookTableForm(request.POST)
    else:
        form = BookTableForm()

    if request.method == "POST":
        form = BookTableForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))

    return render(request, 'booking/form.html', {"form": form})

    