inplist = input()
halflength = int(len(inplist)/2)
status = ""
for i in range(halflength):
    if inplist[i] == inplist[i+3]:
        status = "happy"
    else :
        status = "unhappy"
print("status", status)    
