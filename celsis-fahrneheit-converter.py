def print_celsius_values_with_signature(celsius):
    if False:  # Please add the condition
        print("The celsius value you entered is positive")
    elif False:  # Please add the condition
        print("The celsius value you entered is zero")
    else:
        print("The celsius value you entered is negative")


def compute_fahrenheit(celsius):
    result = 0 # Please calculate fahrenheit
    return result


def main():
    celsius = float(input("Enter a Temperature in Celsius to convert it to Fahrenheit: "))
    print_celsius_values_with_signature(celsius)
    fahrenheit = compute_fahrenheit(celsius)
    print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' % (celsius, fahrenheit))


main()
