'''
    solo learning code for python
'''
def bmi_calculation(weight, height):
    '''
        bmi calculator
        weight is a float in kg
        height is a float in metres
        result is a string with the BMI result
    '''
    result = ''
    bmi  = weight / (height ** 2)
    if bmi < 18.5:
        result = "Underweight"
    elif 18.5 < bmi < 25:
        result = "Normal"
    elif 25 < bmi < 30:
        result = "Overweight"
    else:
        result = "Obesity"
    return result


words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

N = int(input())
new_result = 0
for item in range(1, N + 1):
    new_result += item
print(new_result)
