lineList = [line.rstrip('\n') for line in open('input.txt')]
def calculate_fuel_reqmts():
    sum= 0
    for i in lineList:
        i = int(i)
        sum = sum + ((i //3 ) - 2)
    return sum

def calculate_fuel_2():
     sum = 0
     for i in lineList:
         i = int(i)
         fuel = (i//3) -2
         while(fuel > 0):
             sum = sum + fuel
             fuel = (fuel//3 )-2
     return sum

print(calculate_fuel_reqmts())
print(calculate_fuel_2())
