# bounce.py
#
# Exercise 1.5
height = 100
for bounce in range(1, 11):
    height = height * .6
    print(bounce, round(height, 4))