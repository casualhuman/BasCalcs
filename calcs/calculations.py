# This is where al the calculations snippets are located 


# Ohms law calculations

def get_resistance(voltage, current):
    try:
        resistance_value = int(voltage) / int(current) 
        resistance_value = f'Resistance = {resistance_value:.3f} Ω'
    except:
        resistance_value = 'Current should not be 0'

    return resistance_value

    
# Calculates the current value if current is chosen as value needed 
def get_current(voltage, resistance):
    try:
        current_value = int(voltage) / int(resistance)
        current_value = f'Current = {current_value:.3f} A'

    except ZeroDivisionError:
        current_value = 'Resistance should not be 0'
    return current_value


# Calculates the voltage value if voltage if chosen as value needed 
def get_voltage(current, resistance):
    voltage_value = int(current) * int(resistance) 
    
    return f'Voltage = {voltage_value} v'


# Area Calculations

def get_square_area(length): # Area of Square 
    square_area = length * 2
    return square_area 


def get_rectangle_area(length, breath):
    rectangle_area = length * breath
    return rectangle_area

# Perimeter Calculations 
def get_square_perimeter(length):
    perimeter = 4 * length
    return perimeter

def get_rectangle_perimeter(length, breath):
    rectangle_area = length + breath    # First find the area of rectangle becuase perimeter = 2(l + b)
    perimeter = 2 * rectangle_area
    return perimeter