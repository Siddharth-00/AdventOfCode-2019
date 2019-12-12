file = open("input.txt","r") 
mainArr = list(map(int, file.readline().split(","))) #Get list of numbers and put them in array as ints
output = [] #List to store all outputs
#Key:
#arr = Main Array
#string = opcode string (parameter modes + opcode), string[-3] = 1st param, string[-4] = 2nd param, string[-5] = 3rd Param
#j = position on array
#base = offset base
def get_address(arr, mode, j, base): #Function to get values from the array
    if(mode == 0): #Positional Mode
        return(arr[arr[j]]) 
    elif(mode == 2): #Relative Mode
        return(arr[arr[j] + base]) #Offset with Base
    else:
        return(arr[j]) #Immediate Mode
def store_address(arr, mode, j, val, base): #Store values in array
    x = arr.copy() 
    if(mode == 0): #Positional Mode
        x[x[j]] = val 
    elif(mode == 2): #Relative Mode
        x[x[j]+base] = val
    else:
        x[j] = val #Immediate Mode
    return x #Send new version of array back
def opcode1(arr, string, j, base, debug): #Opcode 1
    param1 = get_address(arr, int(string[-3]), j+1, base) #Get 1st Param
    param2 = get_address(arr, int(string[-4]), j+2, base) #Get 2nd Param
    param3 = get_address(arr, int(string[-5]), j+3, base) #Get 3rd Param
    if debug:
        print(f"Opcode {1}: Altered {param3} at {j+3} to {param1+param2}")
    return(store_address(arr, int(string[-5]), j+3, param1 + param2, base)) #Store sum of two params, mode for storing  is set to 0
def opcode2(arr, string, j, base, debug): #Opcode 2
    param1 = get_address(arr, int(string[-3]), j+1, base) #Get 1st Param
    param2 = get_address(arr, int(string[-4]), j+2, base) #Get 2nd Param
    param3 = get_address(arr, int(string[-5]), j+3, base) #Get 3rd Param
    if debug:
        print(f"Opcode {2}: Altered {param3} at {j+3} to {param1*param2}")
    return(store_address(arr, int(string[-5]), j+3, param1 * param2, base)) #Store product of two params, mode for storing  is set to 0
def opcode3(arr, string, j, base, debug): #Opcode 3
    if debug:
        print(f"Opcode {3}: idx{j}: Altered {arr[j+1]} at {j+1} to {1}")
    return(store_address(arr, int(string[-3]), j+1, int(input("input: ")), base)) #Store input in correct position
def opcode4(arr, string, j, base, debug): #Opcode 4
    output.append(get_address(arr, int(string[-3]), j+1, base)) #Add value at address to global output variable
    if debug:
        print(f"Opcode {4}: Output is {get_address(arr, int(string[-3]), j+1, base)}")
    return arr #Send arr back 
def opcode5(arr, string, j, base): #Opcode 5
    return arr #Send arr back (Just to make calling later on easier)
def jump5(arr, string, j, base, debug): #Jump 5
    param1 = get_address(arr, int(string[-3]), j+1, base) #Get 1st Param
    param2 = get_address(arr, int(string[-4]), j+2, base) #Get 2nd Param
    if(param1 != 0): #Set jump
        if debug:
            print(f"Opcode {5}: {param1} != 0. idx from {j} to {param2}")
        return(param2-j)
    else:
        if debug:
            print(f"Opcode {5}: {param1} == 0. noop")
        return 3
def jump6(arr, string, j, base, debug): #Jump 6
    param1 = get_address(arr, int(string[-3]), j+1, base) #Get 1st Param
    param2 = get_address(arr, int(string[-4]), j+2, base) #Get 2nd Param
    if(param1 == 0): #Set jump
        if debug:
            print(f"Opcode {6}: idx from {j} to {param2}")
        return(param2-j)
    else:
        return 3
def opcode7(arr, string, j, base, debug): #Opcode 7
    param1 = get_address(arr, int(string[-3]), j+1, base) #Get 1st Param
    param2 = get_address(arr, int(string[-4]), j+2, base) #Get 2nd Param
    param3 = get_address(arr, int(string[-5]), j+3, base) #Get 3rd Param
    if(param1 < param2): #Store either 1 or 0 depending on Params
        if debug:
            print(f"Opcode {7}: {param1} < {param2}, loc {j+3} from {param3} to 1")
        return(store_address(arr, int(string[-5]), j+3, 1, base))
    else:
        if debug:
            print(f"Opcode {7}: {param1} !< {param2}, loc {j+3} from {param3} to 0")
        return(store_address(arr, int(string[-5]), j+3, 0, base))
def opcode8(arr, string, j, base, debug): #Opcode 8
    param1 = get_address(arr, int(string[-3]), j+1, base) #Get 1st Param
    param2 = get_address(arr, int(string[-4]), j+2, base) #Get 2nd Param
    param3 = get_address(arr, int(string[-5]), j+3, base) #Get 3rd Param
    if(param1 == param2): #Store either 1 or 0 depending on Params
        if debug:
            print(f"Opcode {8}: {param1} == {param2}, loc {j+3} from {param3} to 1")
        return(store_address(arr, int(string[-5]), j+3, 1, base))
    else:
        if debug:
            print(f"Opcode {8}: {param1} != {param2}, loc {j+3} from {param3} to 0")
        return(store_address(arr, int(string[-5]), j+3, 0, base))
def opcode9(arr, string, j, base, debug): #Opcode 9
    param1 = get_address(arr, int(string[-3]), j+1, base) #Get Param: offset in base
    if debug:
        print(f'opcode 9, mode = {string[-3]}, value = {param1}')
    if debug:
        print(f"Relative Base now {base + param1}")
    return base + param1 #Change the base
def BOOST(arr, debug): #Main Function
    i = 0 #Curr Position in arr
    base = 0 #Curr base
    functions = {1: opcode1, 2: opcode2, 3:opcode3, 4:opcode4, 5:opcode5, 6:opcode5, 7:opcode7, 8:opcode8, 9:opcode9} #Dictionary of functions
    jumps = {1:4, 2:4, 3:2, 4:2, 5:jump5, 6:jump6, 7:4, 8:4, 9:2} #Dictionary of jumps
    while True: 
        string = ('0' * (5-len(str(arr[i]))) + str(arr[i])) #Pad opcode string with 0
        opcode = int(string[-2:]) #Get opcode part of string
        if debug:
            print(f"idx: {i} - current opcode: {opcode}, {string}")
        if(opcode == 99): #Break out of loop, end function
            break
        elif(opcode == 5 or opcode == 6): #If 5 or 6 needed since jump functions need different arguments
            arr = functions[opcode](arr, string, i, base) #Function to change array
            i += jumps[opcode](arr, string, i, base, debug) #Function to change curr position
        elif(opcode == 9): #Change base if opcode is 9
            base = functions[opcode](arr, string, i, base, debug) 
            i += jumps[opcode]
        else:
            arr = functions[opcode](arr, string, i, base, debug) #Generic function for remaining opcodes
            i += jumps[opcode]
    return(output)
BOOST(mainArr + [0] * 100000, False) #BOOST: Main function. Pad array with 0s to allow for extra memory
print(output[-1]) #Print last output


