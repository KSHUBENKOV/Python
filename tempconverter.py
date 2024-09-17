# Converts Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # Formula: (Celsius * 9/5) + 32
    return (celsius * 9/5) + 32

# Converts Celsius to Kelvin
def celsius_to_kelvin(celsius):
    # Formula: Celsius + 273.15
    return celsius + 273.15

# Converts Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    # Formula: (Fahrenheit - 32) * 5/9
    return (fahrenheit - 32) * 5/9

# Converts Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    # Formula: ((Fahrenheit - 32) * 5/9) + 273.15
    return (fahrenheit - 32) * 5/9 + 273.15

# Converts Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    # Formula: Kelvin - 273.15
    return kelvin - 273.15

# Converts Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    # Formula: ((Kelvin - 273.15) * 9/5) + 32
    return (kelvin - 273.15) * 9/5 + 32

# Main function to run the converter
def main():
    # Greeting message
    print("Welcome to the Temperature Converter!")

    # Show the user what conversions they can choose from
    print("Choose a conversion type:")
    print("1. Celsius to Fahrenheit and Kelvin")
    print("2. Fahrenheit to Celsius and Kelvin")
    print("3. Kelvin to Celsius and Fahrenheit")

    # Get the user's choice
    choice = input("Enter your choice (1/2/3): ")

    # Check if the user chose to convert from Celsius
    if choice == '1':
        # Get the temperature in Celsius from the user
        celsius = float(input("Enter temperature in Celsius: "))

        # Convert to Fahrenheit and Kelvin and show results
        print(f"{celsius} °C = {celsius_to_fahrenheit(celsius):.2f} °F")
        print(f"{celsius} °C = {celsius_to_kelvin(celsius):.2f} K")

    # Check if the user chose to convert from Fahrenheit
    elif choice == '2':
        # Get the temperature in Fahrenheit from the user
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))

        # Convert to Celsius and Kelvin and show results
        print(f"{fahrenheit} °F = {fahrenheit_to_celsius(fahrenheit):.2f} °C")
        print(f"{fahrenheit} °F = {fahrenheit_to_kelvin(fahrenheit):.2f} K")

    # Check if the user chose to convert from Kelvin
    elif choice == '3':
        # Get the temperature in Kelvin from the user
        kelvin = float(input("Enter temperature in Kelvin: "))

        # Convert to Celsius and Fahrenheit and show results
        print(f"{kelvin} K = {kelvin_to_celsius(kelvin):.2f} °C")
        print(f"{kelvin} K = {kelvin_to_fahrenheit(kelvin):.2f} °F")

    # If the user enters anything other than 1, 2, or 3
    else:
        # Inform them that the input is invalid
        print("Invalid choice! Please choose 1, 2, or 3.")

# If this script is run directly, start the main function
if __name__ == "__main__":
    main()
