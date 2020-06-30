def shipping_cost(weight):
  if weight <= 2:
    group_shipping_cost = 1.5*weight + 20
    drone_shipping_cost = 4.5*weight + 0
    premium_shipping_cost = 125
  elif (weight > 2) and (weight <= 6):
    group_shipping_cost = 3*weight + 20
    drone_shipping_cost = 9*weight + 0
    premium_shipping_cost = 125
  elif (weight > 6) and (weight <= 10):
    group_shipping_cost = 4*weight + 20
    drone_shipping_cost = 12*weight + 0
    premium_shipping_cost = 125
  elif weight > 10:
    group_shipping_cost = 4.75*weight + 20
    drone_shipping_cost = 14.25*weight + 0
    premium_shipping_cost = 125
  
  return(min(group_shipping_cost,drone_shipping_cost,premium_shipping_cost))
  
print(shipping_cost(4.8))
print(shipping_cost(41.5))
