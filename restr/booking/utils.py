
def print_parameters(form):
    for name, value in form.cleaned_data.items():
        print("{}: ({}) {}".format(name, type(value), value))