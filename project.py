

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Conversion from centimeters to meters
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def food_suggestions(bmi):
    if bmi < 18.5:
        print("\n You are Underweight. Food suggestions to increase height and weight:")
        foods = [
            " Eggs and milk",
            " Almonds and peanuts",
            " Chicken and beef",
            " Bananas and other fruits",
            " Condensed milk and ghee",
            " Brown bread, potatoes and chira",
            " Rice and pulses",
            " Healthy fats (avocado, olive oil)"
        ]
        for food in foods:
            print(f"- {food}")
    elif 18.5 <= bmi <= 24.9:
        print("\n Your BMI is normal. Follow a balanced diet to stay healthy")
    else:
        print("\n You are overweight. Consult your doctor for healthy weight loss")

# Input
try:
    age = int(input("25: "))
    height = float(input("5.5: "))
    weight = float(input("60: "))

    bmi = calculate_bmi(weight, height)
    print(f"\n my BMI: {bmi}")
    food_suggestions(bmi)
except ValueError:
    print("\n 170")
