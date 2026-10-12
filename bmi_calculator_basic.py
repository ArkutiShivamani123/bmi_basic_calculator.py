def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

try:
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be positive values.")
        exit()

    bmi = calculate_bmi(weight, height)

    print(f"\nYour BMI: {bmi:.2f}")

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal Weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")

except ValueError:
    print("Please enter valid numeric values.")