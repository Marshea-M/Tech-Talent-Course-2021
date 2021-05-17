original_cost_of_bike=2000
value_loss_rate=0.9
for years in range(0,7,1):
    cost_of_bike=original_cost_of_bike*(value_loss_rate**years)
    print("The value of the bike that year is", cost_of_bike)