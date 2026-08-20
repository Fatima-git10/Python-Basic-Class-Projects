
# Three cyclists are riding at the speed of 10, 20, 30 km/h. Find the average and compare which cyclist is riding slower than the average speed
speed1 = 10
speed2 = 20
speed3 = 30

average_speed = (speed1 + speed2 + speed3) / 3
print("The average speed is:", average_speed)

if speed1 < average_speed:
    print("Cyclist 1 is riding slower than the average speed.")
if speed2 < average_speed:
    print("Cyclist 2 is riding slower than the average speed.")
if speed3 < average_speed:
    print("Cyclist 3 is riding slower than the average speed.")

if speed1 == average_speed:

    print("Cyclist 1 is riding at average speed")

if speed2 == average_speed:

    print("Cyclist 2 is riding at average speed")

if speed3 == average_speed:

    print("Cyclist 3 is riding at average speed")

if speed1 > average_speed:

    print("Cyclist 1 is faster than average speed")

if speed2 > average_speed:

    print("Cyclist 2 is faster than average speed")

if speed3 > average_speed:

    print("Cyclist 3 is faster than average speed")