
def print_parameters(form):
    """ Print POST http parameters. Used for debugging. """
    for name, value in form.cleaned_data.items():
        print("{}: ({}) {}".format(name, type(value), value))