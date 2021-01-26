# Given a year (as a positive integer), find the respective number of the century. Note that, for example, 20th century began with the year 1901.

import math

year = int(input())
century = math.ceil(year / 100)

print(century)