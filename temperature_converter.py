import functions_v1

type_temperature = input("Inform what kind of temperature you want to convert from! ").lower()

try:
    number_temperature = float(input("Inform the temperature! "))

    if type_temperature == "celsius":
        result = functions_v1.cel_operation(number_temperature)
        print(f"The temperature is {result} °F")

    elif type_temperature == "fahrenheit":
        result = functions_v1.fah_operation(number_temperature)
        print(f"The temperature is {result} °C")

    else:
        print("It must be a type of temperature measurement!")

except ValueError:
    print("That is not an acceptable temperature!")