from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Ohms(models.Model):
    value_needed_choices = (

                            ('voltage', 'Voltage'),
                            ('current', 'Current'),
                            ('resistance', 'Resistance')

                            )

    value_needed = models.CharField(choices = value_needed_choices,
                                    max_length = 20,
                                    default = 'voltage')

    # MaxValueValidator and MinValueValidator endures the number does not go above or below the given numbers 
    voltage = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)],
                                  default=0.00
                                  )

    current = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)],
                                  default=0.00
                                 )

    resistance = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)],
                                    default=0.00
                                    )

    def __str__(self):
        return f"Calculation Id = { self.id }"


    # Calculates the resistance value if resistance is chosen as value needed 
    @property
    def get_resistance(self):
        resistance_value = self.voltage / self.current 

        return resistance_value


    # Calculates the current value if current is chosen as value needed 
    @property
    def get_current(self):
        current_value = self.voltage / self.resistance

        return current_value


    # Calculates the voltage value if voltage if chosen as value needed 
    @property
    def get_voltage(self):
        voltage_value = self.current * self.resistance 

        return voltage_value