from itertools import permutations
from threading import Thread
from queue import Queue
file = open("input.txt","r")
arr = list(map(int, file.readline().split(",")))
outputs = {}
queues = {}
out = Queue(maxsize=1)
def global_change(x):
    return False
for i in range(5):
    queues[i] = Queue(maxsize = 1000)
    outputs[i] = []
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
def opcode3(arr, string, j, x):
    return(store_address(arr, int(string[-3]), j+1, x))
def opcode4(arr, string, j, count):
    outputs[count].append(get_address(arr, int(string[-3]), j+1))
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
def amplify(arr, count, mode):    
    i = 0
    arrCopy = arr.copy()
    cnt = 0
    functions = {1: opcode1, 2: opcode2, 3:opcode3, 4:opcode4, 5:opcode5, 6:opcode5, 7:opcode7, 8:opcode8}
    jumps = {1:4, 2:4, 3:2, 4:2, 5:jump5, 6:jump6, 7:4, 8:4}
    opcode = 0
    while True:
        string = ('0' * (5-len(str(arrCopy[i]))) + str(arrCopy[i]))
        opcode = int(string[-2:])
        if(opcode == 99 and count == 4):
            out.put(outputs[4][-1])
            return
        elif(opcode == 99):
            return
        elif(opcode == 3):
            if(cnt == 0):
                arrCopy = functions[opcode](arrCopy, string, i, mode)
                cnt += 1
            elif(cnt == 1):
                arrCopy = functions[opcode](arrCopy, string, i, queues[count].get())
                queues[count].task_done()
            i += jumps[opcode]
        elif(opcode == 4):
            arrCopy = functions[opcode](arrCopy, string, i,count)
            i += jumps[opcode]
            queues[(count+1)%5].put(outputs[count][-1])
        elif(opcode == 5 or opcode == 6):
            arrCopy = functions[opcode](arrCopy, string, i)
            i += jumps[opcode](arrCopy, string, i)
        else:
            arrCopy = functions[opcode](arrCopy, string, i)
            i += jumps[opcode]

      

combos = list(permutations([9,8,7,6,5]))
highest = 0
for i in combos:
    queues[0].put(0)
    workers = []
    for m in range(5):
        worker = Thread(target=amplify, args = (arr, m, i[m],))
        worker.setDaemon(True)
        worker.start()
        workers.append(worker)
    p = 0
    while True:
        p = out.get()
        if(p != None):
            break
    if(p > highest):
        highest = p
    for i in range(5):
        with queues[i].mutex:
            queues[i].queue.clear()
    
print(highest)
        
    





    
