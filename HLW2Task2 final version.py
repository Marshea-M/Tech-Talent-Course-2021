def function_bike(year:int):
    original_cost_of_bike=2000
    value_loss_rate=0.9
    cost_of_bike=original_cost_of_bike*(value_loss_rate**year)
    
    output=cost_of_bike
    return output



message=function_bike(1)
print("The value of the bike that year is", message)

message=function_bike(2)
print("The value of the bike that year is", message)

message=function_bike(3)
print("The value of the bike that year is", message)

message=function_bike(4)
print("The value of the bike that year is", message)

message=function_bike(5)
print("The value of the bike that year is", message)

message=function_bike(6)
print("The value of the bike that year is", message)

message=function_bike(7)
print("The value of the bike that year is", message)
