from datetime import datetime
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)
def record_bmi(weight, height, file_path='bmi.txt'):
    bmi = calculate_bmi(weight, height)
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, 'a') as file:
        file.write(f"{current_date}, Height: {height} cm, Weight: {weight} kg, BMI: {bmi}\n")
    print("BMI recorded successfully.")



weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
record_bmi(weight, height)