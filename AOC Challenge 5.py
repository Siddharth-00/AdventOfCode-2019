file = open("input.txt","r")
arr = list(map(int, file.readline().split(",")))
arr2 = arr.copy()
output = []
i = 0
def get_address(arr, mode, j):
    if(mode == 0):
        return(arr[arr[j]])
    else:
        return(arr[j])
def store_address(arr, mode, j, val):
    x = arr.copy()
    if(mode == 0):
        x[x[j]] = val
    else:
        x[j] = val
    return x
def opcode1(arr, string, j):
    mode3 = 0
    param1 = get_address(arr, int(string[-3]), j+1)
    param2 = get_address(arr, int(string[-4]), j+2)
    return(store_address(arr, mode3, j+3, param1 + param2))
def opcode2(arr, string, j):
    mode3 = 0
    param1 = get_address(arr, int(string[-3]), j+1)
    param2 = get_address(arr, int(string[-4]), j+2)
    return(store_address(arr, mode3, j+3, param1 * param2))
def opcode3(arr, string, j):
    return(store_address(arr, int(string[-3]), j+1, int(input())))
def opcode4(arr, string, j):
    output.append(get_address(arr, int(string[-3]), j+1))
    return arr
def opcode5(arr, string, j):
    return arr
def jump5(arr, string, j):
    param1 = get_address(arr, int(string[-3]), j+1)
    param2 = get_address(arr, int(string[-4]), j+2)
    if(param1 != 0):
        return(param2-j)
    else:
        return 3
def jump6(arr, string, j):
    param1 = get_address(arr, int(string[-3]), j+1)
    param2 = get_address(arr, int(string[-4]), j+2)
    if(param1 == 0):
        return(param2-j)
    else:
        return 3
def opcode7(arr, string, j):
    param1 = get_address(arr, int(string[-3]), j+1)
    param2 = get_address(arr, int(string[-4]), j+2)
    if(param1 < param2):
        return(store_address(arr, int(string[-5]), j+3, 1))
    else:
        return(store_address(arr, int(string[-5]), j+3, 0))
def opcode8(arr, string, j):
    param1 = get_address(arr, int(string[-3]), j+1)
    param2 = get_address(arr, int(string[-4]), j+2)
    if(param1 == param2):
        return(store_address(arr, int(string[-5]), j+3, 1))
    else:
        return(store_address(arr, int(string[-5]), j+3, 0))
def diagnosticCode(arr):
    i = 0
    functions = {1: opcode1, 2: opcode2, 3:opcode3, 4:opcode4, 5:opcode5, 6:opcode5, 7:opcode7, 8:opcode8}
    jumps = {1:4, 2:4, 3:2, 4:2, 5:jump5, 6:jump6, 7:4, 8:4}
    opcode = 0
    while True:
        string = ('0' * (5-len(str(arr[i]))) + str(arr[i]))
        opcode = int(string[-2:])
        if(opcode == 99):
            break
        if(opcode == 5 or opcode == 6):
            arr = functions[opcode](arr, string, i)
            i += jumps[opcode](arr, string, i)
        else:
            arr = functions[opcode](arr, string, i)
            i += jumps[opcode]
    return(output)
print(diagnosticCode(arr2)[-1])



    
