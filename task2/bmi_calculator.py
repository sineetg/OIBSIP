def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("=== BMI Calculator ===")
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))
        
        if weight <= 0 or height <= 0:
            print("❌ Weight and height must be positive numbers.")
            return

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(f"You are classified as: {category}")
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
