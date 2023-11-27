
from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime

MIN_NO_OF_PEOPLE = 1
MAX_NO_OF_PEOPLE = 10

def validate_no_of_people(value):
    """
        Validate the number of people entered in the form.
    """
    if value < MIN_NO_OF_PEOPLE or value > MAX_NO_OF_PEOPLE: 
        raise ValidationError("Enter the number of people from {} to {}.".format(MIN_NO_OF_PEOPLE,    
                                                                                 MAX_NO_OF_PEOPLE))
    
class BookTableForm(forms.Form):
    """
        Main booking form.
    """

    INTEGER_CHOICES= [tuple([x,x]) for x in range(1,MAX_NO_OF_PEOPLE+1)]

    name = forms.CharField(label="", help_text="", min_length="4",
                            widget=forms.TextInput(attrs={'placeholder': "Your name"}), 
                            required=True)

    email =forms.EmailField(label="", help_text="", 
                            widget=forms.EmailInput(attrs={'placeholder': "Your email"}), required=True)

    phone = forms.CharField(label="", help_text="", 
                            widget=forms.TextInput(attrs={'placeholder': "Your phone"}), required=True)
    
    date = forms.DateField(label="Date", help_text="", 
                            widget=forms.DateInput(attrs={'type': 'date', 'placeholder': "Date" }), required=True)

    time = forms.TimeField(label="Time", help_text="",
                           widget=forms.TimeInput(attrs={'type': 'time', 'placeholder': "Time" }), required=True)
    
    no_of_people = forms.IntegerField(initial=2, label="# of people", help_text="", min_value=1, max_value=10, 
                            widget=forms.NumberInput(attrs={'placeholder': "# of people"}), required=True,
                            validators=[validate_no_of_people])
    
    message = forms.CharField(label="", help_text="",
                            widget=forms.Textarea(attrs={'placeholder': "Message"}),
                            required=False)

    def clean_email(self):
        """ Lowercase email. """
        return self.cleaned_data["email"].lower()
    

    def clean(self):
        """ Validate date and time are future time and date. """

        cleaned_data = super().clean() 
        now = datetime.now()

        date = cleaned_data.get("date")
        time = cleaned_data.get("time")

        if datetime.combine(date, time) < now:
            # self.add_error(None, "Enter future time.")
            self.add_error(None, ValidationError("Enter future date an time."))
        
        restaurant_opens = datetime(1,1,1,13,0)
        restaurant_closes = datetime(1,1,1,23,59)
        
        if time < restaurant_opens.time() or time > restaurant_closes.time():
             self.add_error(None, ValidationError("The opening time are from 1pm till midnight."))


       
       
