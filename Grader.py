# Try to import module math for 'tan' and 'pi' function
import math

# Define a function for polysum, used 2 variables for polygons, and then return the value with 4 decimal
def polysum(n , s):
    area = (0.25*n*(s**2)/math.tan(math.pi/n))
    perimeter = n*s

    return round(area + perimeter**2, 4)