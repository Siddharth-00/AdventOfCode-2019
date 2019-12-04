file = open("input.txt","r")
arr = list(map(int, file.readline().split(",")))
arr2 = arr.copy()
i = 0
def test(noun, value, arr):
    arr[1] = noun
    arr[2] = value
    i = 0
    while True:
        if(arr[i] == 1):
            arr[arr[i+3]] = arr[arr[i+2]] + arr[arr[i+1]]
        elif(arr[i] == 2):
            arr[arr[i+3]] = arr[arr[i+2]] * arr[arr[i+1]]
        elif(arr[i] == 99):
            break
        i+=4
    return(arr[0])
for j in range(100):
    for k in range(100):
        if(test(j,k,arr2) == 19690720):
            print(j*100 + k)
            break
        arr2 = arr.copy()


    
