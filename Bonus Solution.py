# Assign the problem data to variables with representative names
# hole height, daily advance, night retreat, accumulated distance
traveled_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
#Here I am going to subtract 20cm directly from each position on the list to calculate the progress per day
traveled_day = [n-20 for n in traveled_cm]
acumulated_distance=0
# Assign 0 to the variable that represents the solution
days=0
# Writing the code that solves the problem
for num in range(len(traveled_day)):
    if traveled_day[num]<125:
        acumulated_distance=acumulated_distance+traveled_day[num]
    days+=1


# Print the result with print('Days =', days)
print("The Snail takes ",days,"days to climb the well\n")

# What is your maximum displacement in a day? And its minimum?
import statistics
min_value = min(traveled_day)
max_value = max(traveled_day)
print('The maximum movement in one day has been:', max_value, "cm")
print('The minimum displacement in one day has been:', min_value, "cm")
# What is your average progress?
import statistics
average = statistics.mean(traveled_day)
print("The average progress each day is :",average, "cm")
# What is the standard deviation of your displacement during the day?
import statistics
stdev=statistics.pstdev(traveled_day)
print("The standard deviation of the list is: " + str(stdev))