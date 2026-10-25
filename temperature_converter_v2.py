import functions


while True:
    first_type_temperature = input("Inform the type of temperature you want to convert from! ").lower()
    second_type_temperature = input("Inform the type of temperature you want to convert to! ").lower()

    try:
        number_temperature = float(input("Inform the Temperature! "))

        if first_type_temperature == "celsius":
            if second_type_temperature == "fahrenheit":
                result = functions.cel_to_fah_operation(number_temperature)
                print(f"The temperature is {result} °F")

                if not functions.question():
                    break

            elif second_type_temperature == "kelvin":
                result = functions.cel_to_kel_operation(number_temperature)
                print(f"The temperature is {result} K")

                if not functions.question():
                    break

            elif second_type_temperature == "rankine":
                result = functions.cel_to_ran_operation(number_temperature)
                print(f"The temperature is {result} °R")

                if not functions.question():
                    break

            else:
                print("Those types are not readable!")

        elif first_type_temperature == "fahrenheit":
            if second_type_temperature == "celsius":
                result = functions.fah_to_cel_operation(number_temperature)
                print(f"The temperature is {result} °C")

                if not functions.question():
                    break

            elif second_type_temperature == "kelvin":
                result = functions.fah_to_kel_operation(number_temperature)
                print(f"The temperature is {result} K")

                if not functions.question():
                    break

            elif second_type_temperature == "rankine":
                result = functions.fah_to_ran_operation(number_temperature)
                print(f"The temperature is {result} °R")

                if not functions.question():
                    break

            else:
                print("Those types are not readable!")

        elif first_type_temperature == "kelvin":
            if second_type_temperature == "celsius":
                result = functions.kel_to_cel_operation(number_temperature)
                print(f"The temperature is {result} °C")

                if not functions.question():
                    break

            elif second_type_temperature == "fahrenheit":
                result = functions.kel_to_fah_operation(number_temperature)
                print(f"The temperature is {result} °F")
                
                if not functions.question():
                    break

            elif second_type_temperature == "rankine":
                result = functions.kel_to_ran_operation(number_temperature)
                print(f"The temperature is {result} °R")
                
                if not functions.question():
                    break

            else:
                print("Those types are not readable!")

        elif first_type_temperature == "rankine":
            if second_type_temperature == "celsius":
                result = functions.ran_to_cel_operation(number_temperature)
                print(f"The temperature is {result} °C")

                if not functions.question():
                    break

            elif second_type_temperature == "fahrenheit":
                result = functions.ran_to_fah_operation(number_temperature)
                print(f"The temperature is {result} °F")
                
                if not functions.question():
                    break

            elif second_type_temperature == "kelvin":
                result = functions.ran_to_kel_operation(number_temperature)
                print(f"The temperature is {result} K")
                
                if not functions.question():
                    break

            else:
                print("Those types are not readable!")

        else:
            print("Those types are not readable!")

    except ValueError:
        print("It must be a number of temperature")