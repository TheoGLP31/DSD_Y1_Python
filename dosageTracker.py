# Track total mg of paracetamol given today
total_mg = 0

def record_dose(mg):
    global total_mg

    total_mg = total_mg + mg
    print("Recorded dose:", mg, "mg. Total today:", total_mg, "mg")

record_dose(250)
record_dose(250)
print("Final total:", total_mg)