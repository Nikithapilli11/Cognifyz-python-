def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    print("=== Temperature Converter ===")
    
    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().lower()
        
        if unit == 'c':
            converted = celsius_to_fahrenheit(value)
            print(f"{value:.2f}°C is equal to {converted:.2f}°F")
        elif unit == 'f':
            converted = fahrenheit_to_celsius(value)
            print(f"{value:.2f}°F is equal to {converted:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
