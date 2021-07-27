import astro
from datetime import date
from math import sqrt

mx = 0
mn = 0
total_estimated_value = 0
counter = 0
estimated_values = list()

for y in range(1900, 2000):
    for m in range(1,13):
        for d in range(1,32):
            try:
                date(y, m, d)
                temp = astro.get_estimated_value(str(y), str(m), str(d))[0]
                if temp > mx:
                    mx = temp
                    mx_date = str(y) + "/" + str(m) + "/" + str(d)
                if temp < mn:
                    mn = temp
                    mn_date = str(y) + "/" + str(m) + "/" + str(d)
                estimated_values.append(temp)
                if temp > 6.79 and temp < 6.81:
                    print(y, m, d)
            except ValueError:
                continue
            
mean = sum(estimated_values) / len(estimated_values)            
standard_deviation_squares = list()
for i in range(0, len(estimated_values)):
    standard_deviation_squares.append((estimated_values[i] - mean) ** 2)
standard_deviation = sqrt(sum(standard_deviation_squares) / len(standard_deviation_squares)) 
    

print(mx, mx_date)
print(mn, mn_date)
print(mean)
print(standard_deviation)

exit()
