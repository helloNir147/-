# מקבל את נתוני הגובה והמשקל מהמשתמש
height = int(input("Enter your height in cm: ")) / 100
weight = int(input("Enter your weight in kg: "))
age = int(input("Enter your age: "))

# חישוב ה-BMI
bmi = weight / height**2

# בדיקת מצב המשקל לפי גיל עם טווחים מותאמים
def check_bmi_by_age(age, bmi):
    if 1 <= age <= 5:
        if bmi > 18:
            return "Above normal range for age",age
        elif 14 <= bmi <= 18:
            return "Normal weight for age",age
        else:
            return "Below normal range for age",age
    elif 6 <= age <= 12:
        if bmi > 20:
            return "Above normal range for age",age
        elif 15 <= bmi <= 20:
            return "Normal weight for age"
        else:
            return "Below normal range for age",age
    elif 13 <= age <= 18:
        if bmi > 25:
            return "Above normal range for age",age
        elif 18.5 <= bmi <= 25:
            return "Normal weight for age",age
        else:
            return "Below normal range for age",age
    elif 19 <= age <= 64:
        if bmi > 30:
            return "Obesity"
        elif bmi > 25:
            return "Overweight"
        elif bmi >= 18.5:
            return "Normal weight"
        else:
            return "Underweight"
    elif age >= 65:
        if bmi > 28:
            return "Overweight for age",age
        elif bmi >= 22:
            return "Normal weight for age",age
        else:
            return "Underweight for age",age
    else:
        return "Age out of range"

# קריאה לפונקציה והדפסת התוצאה
result = check_bmi_by_age(age, bmi)
print(f"For age {age}, you have {result}")
print("The BMI result is: {:.3f}".format(bmi))
