
import re

def extract_data(user_input):
    # Define regular expressions to extract data according to the specified formats
    age = re.search(r"(\d+)\s*(years|y)", user_input)  # Age in years
    gender = re.search(r"\b(male|female)\b", user_input, re.IGNORECASE)  # Gender (optional)
    height = re.search(r"(\d+)\s*cm", user_input)  # Height in cm
    weight = re.search(r"(\d+)\s*kg", user_input)  # Weight in kg
    temperature = re.search(r"(\d+\.?\d*)\s*°C", user_input)  # Temperature in Celsius
    blood_pressure = re.search(r"(\d+/\d+)\s*mmHg", user_input)  # Blood pressure
    sugar = re.search(r"(\d+)\s*mg/dL", user_input)  # Sugar levels

    return {
        "age": age.group(1) if age else None,
        "gender": gender.group(1).lower() if gender else None,
        "height": height.group(1) if height else None,
        "weight": weight.group(1) if weight else None,
        "temperature": temperature.group(1) if temperature else None,
        "blood_pressure": blood_pressure.group(1) if blood_pressure else None,
        "sugar": sugar.group(1) if sugar else None,
    }

def diagnose(data):
    # List to store diagnosis statements
    diagnosis_list = []

    # Temperature Diagnosis
    if data["temperature"]:
        temperature = float(data["temperature"])
        if temperature > 37.5:
            diagnosis_list.append("You have a fever.")
        elif temperature < 36.0:
            diagnosis_list.append("Your body temperature is too low.")
        else:
            diagnosis_list.append("Your body temperature is normal.")
    
    # Blood Pressure Diagnosis
    if data["blood_pressure"]:
        sys, dia = map(int, data["blood_pressure"].split('/'))
        if sys > 140 or dia > 90:
            diagnosis_list.append("Your blood pressure is high. Consider seeing a doctor.")
        else:
            diagnosis_list.append("Your blood pressure is normal.")
    
    # Sugar Levels Diagnosis
    if data["sugar"]:
        sugar_level = int(data["sugar"])
        if sugar_level < 70:
            diagnosis_list.append("Your blood sugar is low.")
        elif sugar_level > 100:
            diagnosis_list.append("Your blood sugar is high. You might be at risk for diabetes.")
        else:
            diagnosis_list.append("Your blood sugar levels are normal.")

    # BMI Check
    if data["height"] and data["weight"]:
        height_m = int(data["height"]) / 100  # Convert height from cm to meters
        weight_kg = int(data["weight"])  # Weight in kg
        bmi = weight_kg / (height_m ** 2)  # Calculate BMI

        if bmi < 18.5:
            diagnosis_list.append("Your BMI indicates you are underweight.")
        elif bmi >= 25:
            diagnosis_list.append("Your BMI indicates you are overweight.")
        else:
            diagnosis_list.append("Your BMI is within a normal range.")
    
    # Combine diagnosis statements or indicate insufficient data
    if diagnosis_list:
        return " ".join(diagnosis_list)
    else:
        return "No sufficient health data provided to make a diagnosis."

# Ask the user for input
print("Welcome to the Health Diagnosis Chatbot!")
print("Please provide your health details in a single sentence. For example:")
print("\"I am 30 years old, 175 cm tall, weigh 80 kg, have a temperature of 36.8°C, blood pressure 130/85 mmHg, and sugar level 95 mg/dL.\"")
user_input = input("\nEnter your details here: ")

# Extract data from user input
extracted_data = extract_data(user_input)

# Provide diagnosis
diagnosis = diagnose(extracted_data)
print("\nDiagnosis: ", diagnosis)
