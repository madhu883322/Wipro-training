# -------------------------------
# Project 1: Travel Suggestion
# -------------------------------

# Ask the user how far they want to travel
distance = int(input("How far would you like to travel in miles? "))

# Suggest mode of transport based on distance
if distance < 3:
    print("I suggest Bicycle to your destination")
elif distance < 300:
    print("I suggest Motor-Cycle to your destination")
else:
    print("I suggest Super-Car to your destination")


# -------------------------------
# Project 2: Server Cost Calculation
# -------------------------------

# Define cost per hour
cost_per_hour = 0.51

# Calculate costs
cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

# Assume budget
budget = 918

# Calculate number of days server can run with budget
days_with_budget = budget / cost_per_day

# Display results
print("\n--- Server Cost Calculations ---")
print(f"Cost to operate one server per day: ${cost_per_day:.2f}")
print(f"Cost to operate one server per week: ${cost_per_week:.2f}")
print(f"Cost to operate one server per month: ${cost_per_month:.2f}")
print(f"Number of days one server can be operated with $918: {int(days_with_budget)} days")