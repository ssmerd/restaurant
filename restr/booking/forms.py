
from django import forms
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django.contrib import messages


from datetime import datetime

""" Global variables """

MIN_NO_OF_PEOPLE = 1
MAX_NO_OF_PEOPLE = 10

RESTAURANT_OPENS_HOUR = 11
RESTAURANT_CLOSES_HOUR = 23
RESTAURANT_CLOSES_MIN = 00
RESTAURANT_OPENING_MESSAGE = "The opening time are from 11am till 11pm."

def validate_no_of_people(value):
    """ Validate the number of people entered in the form. """
    if value < MIN_NO_OF_PEOPLE or value > MAX_NO_OF_PEOPLE: 
        raise ValidationError("Enter the number of people from {} to {}.".format(MIN_NO_OF_PEOPLE,    
                                                                                 MAX_NO_OF_PEOPLE))
    
class BookTableForm(forms.Form):
    """ Main booking form. The form provides cleaning and validation of entered data. """
 
    INTEGER_CHOICES= [tuple([x,x]) for x in range(1,MAX_NO_OF_PEOPLE+1)]


    name = forms.CharField(label="", help_text="", required=True,
                            error_messages={'required' : 'Please enter your name'},
                            widget=forms.TextInput(attrs={'class':'form-control', 
                            'placeholder': "Your name"}))

    email =forms.EmailField(label="", help_text="", 
                            widget=forms.EmailInput(attrs={'class':'form-control',
                            'placeholder': "Your email"}), required=True)

    phone = forms.CharField(label="", help_text="", 
                            widget=forms.TextInput(attrs={'class':'form-control',
                            'placeholder': "Your phone"}), required=True)
    
    date = forms.DateField(label="Date", help_text="", 
                            widget=forms.DateInput(attrs={'class':'form-control',
                            'type': 'date', 'placeholder': "Date" }), required=True)

    time = forms.TimeField(label="Time", help_text="",
                           widget=forms.TimeInput(attrs={'class':'form-control',
                           'type': 'time', 'placeholder': "Time" }), required=True)
    
    no_of_people = forms.IntegerField(initial=2, label="# of people", help_text="", min_value=1, max_value=10, 
                            widget=forms.NumberInput(attrs={'class':'form-control',
                            'placeholder': "# of people"}), required=True,
                            validators=[validate_no_of_people])
    
    message = forms.CharField(label="", help_text="", 
                            widget=forms.Textarea(attrs={'class':'form-control',
                            'placeholder': "Message",
                            'rows': '5',
                            'cols': '1024'}),
                            required=False)

    def clean_email(self):
        """ Lowercase email. """
        return self.cleaned_data["email"].lower()
    

    def clean(self):
        """ Validate date and time are future time and date. """
        pass
        cleaned_data = super().clean() 
        now = datetime.now()

        date = cleaned_data.get("date")
        time = cleaned_data.get("time")

        if datetime.combine(date, time) < now:
            self.add_error(None, "Enter future date an time.")
        
        restaurant_opens = datetime(1,1,1,RESTAURANT_OPENS_HOUR,0)
        restaurant_closes = datetime(1,1,1,RESTAURANT_CLOSES_HOUR, RESTAURANT_CLOSES_MIN)
        
        if time < restaurant_opens.time() or time > restaurant_closes.time():
             self.add_error(None, ValidationError(RESTAURANT_OPENING_MESSAGE))



class DivErrorList(ErrorList):
     def __str__(self):
         return self.as_divs()
     def as_divs(self):
         if not self: return ''
         return mark_safe('<div class="errorlist">%s</div>' % ''.join(['<div class="alert alert-danger">%s</div>' % e for e in self]))  
       

