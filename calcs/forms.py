
from django import forms 
from django.core.validators import MinValueValidator, MaxValueValidator


# Form for sending message to developer 
class MessageForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea)


class OhmsForm(forms.Form):
    value_needed_choices = (

                            ('voltage', 'Voltage'),
                            ('current', 'Current'),
                            ('resistance', 'Resistance')

                            )

    value_needed = forms.ChoiceField(
                                     widget = forms.Select,
                                     choices = value_needed_choices
                                    )

    # MaxValueValidator(100) -- Input does not exceed 100
    # MinValueValidator(0)   -- Input should be greater than 0
    voltage = forms.DecimalField(
                                 validators=[MaxValueValidator(100),
                                             MinValueValidator(0)
                                            ],
                                 initial=0.00
                                )

    current = forms.DecimalField(
                                 validators=[MaxValueValidator(100),
                                             MinValueValidator(0)
                                            ],
                                 initial=0.00
                                )

    resistance = forms.DecimalField(
                                    validators=[MaxValueValidator(100),
                                                MinValueValidator(0)
                                                ],
                                    initial=0.00
                                   )

