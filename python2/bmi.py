name1 = "jg"
height_m1 = 2
weight_kg1 = 90

name2 = "kc"
height_m2 = 1.8
weight_kg2 = 70

name3 = "mc"
height_m3 = 2.5
weight_kg3 = 160


def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m**2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not over weight"
    else:
        return name + " is overweight"


result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)
