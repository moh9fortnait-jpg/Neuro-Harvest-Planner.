# Project 12: Neuro-Harvest Planner
# Estimating agricultural yield based on land area

def estimate_yield(area, crop_type):
    # Simple logic: Yield per hectare (Hectare = 10,000 m2)
    yield_map = {"wheat": 3.5, "barley": 2.8, "potato": 30} # Tons per hectare
    rate = yield_map.get(crop_type.lower(), 1.0)
    total = (area / 10000) * rate
    return total

def main():
    print("--- Neuro-Harvest Planner v1.0 ---")
    try:
        area_m2 = float(input("Enter land area in Square Meters (m2): "))
        crop = input("Crop type (Wheat, Barley, Potato): ")
        
        result = estimate_yield(area_m2, crop)
        print(f"\nEstimated Harvest: {result:.2f} Tons of {crop}.")
        print("Note: This is a logical estimate based on regional averages.")
    except ValueError:
        print("Please enter a valid area.")