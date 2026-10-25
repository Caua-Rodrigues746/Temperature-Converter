def cel_to_fah_operation(number_temperature):   
    convertion = (number_temperature * 1.8) + 32
    return convertion        
        
def cel_to_kel_operation(number_temperature):
    convertion = number_temperature + 273.15
    return convertion

def cel_to_ran_operation(number_temperature):
    convertion = (number_temperature + 273.15) * 1.8
    return convertion

def fah_to_cel_operation(number_temperature):
    convertion = (number_temperature - 32) * 5 / 9
    return convertion

def fah_to_kel_operation(number_temperature):
    convertion = (number_temperature - 32) / 1.8 + 273.15
    return convertion

def fah_to_ran_operation(number_temperature):
    convertion = number_temperature + 459.67
    return convertion

def kel_to_cel_operation(number_temperature):
    convertion = number_temperature - 273.15
    return convertion

def kel_to_fah_operation(number_temperature):
    convertion = (number_temperature - 273.15) * 1.8 + 32
    return convertion

def kel_to_ran_operation(number_temperature):
    convertion = number_temperature * 1.8
    return convertion

def ran_to_cel_operation(number_temperature):
    convertion = (number_temperature - 491.67) / 1.8
    return convertion

def ran_to_fah_operation(number_temperature):
    convertion = number_temperature - 459.67
    return convertion

def ran_to_kel_operation(number_temperature):
    convertion = number_temperature / 1.8
    return convertion

def question():
    question = input("Do you want to perform another convertion? type Yes or No!").lower()
    
    if question == "yes":
        print("Lets try again!")
        return True

    elif question == "no":
        return False

    else:
        print("It must be Yes or No!")
        return False