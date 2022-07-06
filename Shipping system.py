# Shipping system price calculations
weight = float(input())

# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20.00
elif weight <= 6:
  cost_ground = weight * 3.0 + 20.00
elif weight <= 10:
  cost_ground = weight * 4.0 + 20.00
else:
  cost_ground = weight * 4.75 + 20.00

# Premium Ground Shipping
cost_premium = 125.00

# Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("Ground shipping cost: $", cost_ground)
print("Ground shipping premium cost: $", cost_premium)
print("Drone shipping cost: $", cost_drone)