def getFuel(mass):
    if(mass <= 0):
        return 0
    else:
        return mass + getFuel(mass//3 -2) 

file = open("input.txt","r")
masses = file.readlines()
output = sum([getFuel(int(masses[i])//3 - 2) for i in range(len(masses))])
print(output)
