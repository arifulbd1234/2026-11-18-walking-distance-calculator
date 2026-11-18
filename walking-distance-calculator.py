# Day 43 - Walking Distance Calculator (2026-11-18)
# What it does:
#   Works out how long a walk takes, how many steps it is, how many
#   calories it burns, and converts between km and miles.
# Who it is useful for:
#   Anyone who walks to school, office, the bazaar or for exercise -
#   plan your walk, check your 10,000-step goal, and see the calories
#   you burn, all before you leave the house.
# Plain Python only - no external libraries needed.


def walking_time(distance_km, speed_kmh=5.0):
    """Return walking time in minutes for a distance at a given speed.

    Average walking speed is about 5 km/h; a slow stroll is ~3 km/h
    and a brisk walk is ~6 km/h.
    """
    if distance_km <= 0:
        raise ValueError("Distance must be more than 0 km.")
    if speed_kmh <= 0:
        raise ValueError("Speed must be more than 0 km/h.")
    return (distance_km / speed_kmh) * 60


def format_minutes(minutes):
    """Turn a minute count into a friendly '1h 25m' style string."""
    total = round(minutes)
    hours, mins = divmod(total, 60)
    if hours == 0:
        return f"{mins} min"
    if mins == 0:
        return f"{hours}h"
    return f"{hours}h {mins}m"


def steps_for_distance(distance_km, stride_m=0.75):
    """Estimate step count for a distance.

    Average adult stride is about 0.75 m (taller people ~0.8 m,
    shorter people ~0.65 m).
    """
    if distance_km <= 0:
        raise ValueError("Distance must be more than 0 km.")
    if stride_m <= 0:
        raise ValueError("Stride length must be more than 0 m.")
    return round((distance_km * 1000) / stride_m)


def distance_from_steps(steps, stride_m=0.75):
    """Estimate distance in km from a step count."""
    if steps < 0:
        raise ValueError("Steps cannot be negative.")
    if stride_m <= 0:
        raise ValueError("Stride length must be more than 0 m.")
    return round((steps * stride_m) / 1000, 2)


def calories_burned(distance_km, weight_kg, speed_kmh=5.0):
    """Estimate calories burned while walking.

    Uses the simple rule of about 0.53 kcal per kg of body weight
    per km walked (a standard walking estimate).
    """
    if distance_km <= 0:
        raise ValueError("Distance must be more than 0 km.")
    if weight_kg <= 0:
        raise ValueError("Weight must be more than 0 kg.")
    return round(0.53 * weight_kg * distance_km)


def km_to_miles(km):
    """Convert kilometres to miles."""
    return round(km * 0.621371, 2)


def miles_to_km(miles):
    """Convert miles to kilometres."""
    return round(miles / 0.621371, 2)


def plan_walk(distance_km, weight_kg, speed_kmh=5.0, stride_m=0.75):
    """Plan one walk and return all the useful numbers as a dict."""
    minutes = walking_time(distance_km, speed_kmh)
    return {
        "distance_km": distance_km,
        "distance_miles": km_to_miles(distance_km),
        "time": format_minutes(minutes),
        "steps": steps_for_distance(distance_km, stride_m),
        "calories": calories_burned(distance_km, weight_kg, speed_kmh),
    }


def show_plan(title, plan):
    """Print one walk plan in a tidy, readable way."""
    print(f"--- {title} ---")
    print(f"Distance : {plan['distance_km']} km ({plan['distance_miles']} miles)")
    print(f"Time     : {plan['time']}")
    print(f"Steps    : {plan['steps']:,}")
    print(f"Calories : ~{plan['calories']} kcal")
    print()


if __name__ == "__main__":
    # Example 1: Home to office in Dhaka - 3.5 km, 70 kg person,
    # normal walking speed (5 km/h).
    show_plan(
        "Basa theke office - 3.5 km",
        plan_walk(distance_km=3.5, weight_kg=70, speed_kmh=5.0),
    )

    # Example 2: The daily 10,000-step goal - how far is it, and how
    # long does it take at a brisk 6 km/h pace?
    goal_steps = 10_000
    goal_km = distance_from_steps(goal_steps)
    print(f"--- 10,000 steps goal ---")
    print(f"Distance : {goal_km} km")
    print(f"Time     : {format_minutes(walking_time(goal_km, 6.0))} (brisk walk)")
    print(f"Calories : ~{calories_burned(goal_km, 70, 6.0)} kcal (70 kg)")
    print()

    # Example 3: Evening walk in the park - 2 km at a relaxed 4 km/h.
    show_plan(
        "Bikeler hata - 2 km",
        plan_walk(distance_km=2, weight_kg=65, speed_kmh=4.0),
    )
