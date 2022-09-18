# Assign the problem data to variables with representative names
# hole height, daily advance, night retreat, accumulated distance
total_distance=125
traveled=0
day_time=30
night_time=20
distance_day=day_time-night_time
# Assign 0 to the variable that represents the solution
days=0
# Writing the code that solves the problem
while (traveled<125):
    traveled=traveled+distance_day
    days+=1
# Printing the result with print('Days =', days)
print("The Snail takes",days,"days to climb the well")