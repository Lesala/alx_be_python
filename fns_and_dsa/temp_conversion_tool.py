# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global factor"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factor"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ").strip()
        
        # Validate numeric input
        if not temp_input.replace('.', '', 1).lstrip('-').isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temp_value = float(temp_input)

        # Get unit type
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            result = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {result}°F")
        elif unit == "F":
            result = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {result}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
