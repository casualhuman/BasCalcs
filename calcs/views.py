from django.shortcuts import render
#from .models import Ohms
from .forms import OhmsForm, MessageForm
from . import calculations
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


def home_page(request):
    return render(request, 'calcs/pages/home.html', {})


# When the user wants to Send a message to the developer 
def leave_message(request):
    sent = False 
    # The form has been submitted 
    if request.method == 'POST':
        message_form = MessageForm(request.POST) # submit form 
        if message_form.is_valid():    # Checks if all the fields where filled 
            cd = message_form.cleaned_data

            header = f"Message from {cd['name']} a BASCAL user."

            body = f"""
                       From: {cd['name']}
                       email: {cd['email']}
                       message: {cd['body']}
                       
                    """

            # use send mail to send email to developer
            send_mail(header, body, cd['email'], ['abdulrahimjallohaarj@gmail.com']) 
            
            sent = True 

    else:
        message_form = MessageForm()

    return render(request, 'calcs/pages/leave_message.html', {'message_form': message_form,
                                                              'sent': sent
                                                             }
                 )

def ohms_law(request):
    # user submitted the value they need sto calculate 
    #ohms_form = OhmsForm()
    result = None 
    if request.method == 'POST':
        # The user has requested the calculated value 
        ohms_form = OhmsForm(request.POST)
        if ohms_form.is_valid():
            #values = ohms_form.save() # saves the values to the db 
            cd = ohms_form.cleaned_data
            
            # Calls the various functions used to calculate voltage, current, resistance from  imported module calculation
            if cd['value_needed'] == 'voltage':
                result = calculations.get_voltage(cd['current'], cd['resistance']) 
                
            # Calculates the current value 
            elif cd['value_needed'] == 'current':
                result = calculations.get_current(cd['voltage'], cd['resistance'])
                
            # Calculates the resistance value 
            elif cd['value_needed'] == 'resistance':
                result = calculations.get_resistance(cd['voltage'], cd['current'])
            ohms_form = OhmsForm()
                
    else:
        ohms_form = OhmsForm()

    return render(request, 'calcs/pages/ohms_law.html', {'ohms_form': ohms_form,
                                                      'result': result 
                                                    })





# 