goal = 10000

def q4(water_ml):
    total_points = 0

    for i in range(water_ml // 250):
        total_points += 1
        print(total_points)
    
    return total_points

def summary_line(steps, water_ml, screen_mins):
    percentSteps = (steps / goal) * 100
    waterPoints = q4(water_ml)
    
    print(f"Steps: {steps} {percentSteps}, Water: {water_ml} ({"+" if waterPoints > 0 else "" if waterPoints == 0 else "-"}{waterPoints}), Screen: {screen_mins} - {"OK" if screen_mins <= 240 else "High"}")

summary_line(500, 100, 250)