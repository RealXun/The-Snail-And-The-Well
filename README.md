# The Snail and the Well

![](https://github.com/RealXun/The-Snail-And-The-Well/blob/main/Resources/maxresdefault%20(1).jpg)

A snail :snail:	falls to the bottom of a 125 cm well. Every day the snail climbs 30 cm. but at night while sleeping he slips 20 cm because the walls are wet. How many days does it take to escape from the well?

## Here are 3 different types of solutions:
- Every day the snail always climbs 30 cm. (using just while)
```
total_distance=125
traveled=0
day_time=30
night_time=20
distanced_ay=day_time-night_time
days=0
while (traveled<125):
    traveled=traveled+distance_day
    days+=1
print("The Snail takes ",days,"days to climb the well")
```

- Every day the snail always climbs 30 cm. (using while,if and else)
```
total_distance=125
traveled=0
day_time=30
night_time=20
distance_day=day_time-night_time
days=0
while (1):
    if traveled<total_distance:
        traveled=traveled+distance_day
        days=days+1
    else: 
        break

print("The Snail takes ",days,"days to climb the well")
```

- The distance traveled by the snail is defined by a list.
```
traveled_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
traveled_day = [n-20 for n in traveled_cm]
acumulated_distance=0
days=0
for num in range(len(traveled_day)):
    if traveled_day[num]<125:
        acumulated_distance=acumulated_distance+traveled_day[num]
    days+=1
```

A pretty easy way to know in how many days the Snaill will finally climb the well.

## As bonus, lets check somthing else, just for fun.
- What is your maximum displacement in a day? And its minimum?
```
import statistics
min_value = min(traveled_day)
max_value = max(traveled_day)
print('The maximum movement in one day has been:', max_value, "cm")
print('The minimum displacement in one day has been:', min_value, "cm")
```
- What is your average progress?
```
import statistics
average = statistics.mean(traveled_day)
print("The average progress each day is :",average, "cm")
```
- What is the standard deviation of its displacement during the day?
```
import statistics
stdev=statistics.pstdev(traveled_day)
print("The standard deviation of the list is: " + str(stdev))
```
