# Q3
def to_celsius(fahrenheit):
    degrees_celcius = (fahrenheit - 32) * (5 / 9)
    return degrees_celcius
degrees = to_celsius(212.0)
print(degrees)


# Q4
def days_in_years(number_of_years):
    return (365 * number_of_years)
print(days_in_years(2))


# Q5
def calculate_cartons(eggs):
    return int(abs(eggs/12))
print(calculate_cartons(65))


# Q6
def dinner_calculator(meal_cost, drinks_cost):
    drinks_cost *= 0.7
    total_cost = drinks_cost + meal_cost
    total_cost *= 1.15
    return total_cost
print(dinner_calculator(12,4))


# Q7
def trip_cost(price,distance,economy):
    cost = distance * economy / 100 * price
    return cost
print(trip_cost(1.68,27,7.7))


# Q8
def odd_finder(a,b,c,d,e,f,g,h,i,j):
    count = 0
    x = a, b, c, d, e, f, g, h, i, j
    for i in x:
        if int(i) > 0 and int(i+1)%2 == 0:
            count += 1
    return count
print(odd_finder(1,2,3,4,5,-1,-2,-3,-4,0))


# Q9
def virus_growth(num,rate,hour,time):
    n = num * (rate**(time/hour))
    return n
print(round(virus_growth(100,2,4,16),1))
print(round(virus_growth(75,1.5,3,16),2))
print(round(virus_growth(1620, 2.5,12,100),2))

# Q10
def dseries(n_terms):
    x = 0
    for i in range(1, n_terms+1):
        x += i ** 2
    return x
print(dseries(4))