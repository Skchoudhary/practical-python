# bounce.py
#
# Exercise 1.5
bounces = 1
height = 100
ratio = 3 / 5

while bounces <= 10:
    height = height * ratio
    print(f"Bounces: {bounces}, Height: {round(height, 4)}")
    bounces = bounces + 1
    
