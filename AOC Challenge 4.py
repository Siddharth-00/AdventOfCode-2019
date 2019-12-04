import re
file = open("input.txt","r")
nums = file.readline()
num1 = int(nums.split("-")[0])
num2 = int(nums.split("-")[1])
def validNum(x):
    string = str(x)
    check = False
    groups = [y.group() for y in re.finditer(r'(.)\1+', string)]
    
    for j in range(len(string)-1):
        if((string[j] > string[j+1])):
            return False
    for k in groups:
        if(len(k) == 2):
            return True
    return False    
cnt = 0
for i in range(num1, num2):
    if(validNum(i) == True):
        cnt += 1
print(cnt)
