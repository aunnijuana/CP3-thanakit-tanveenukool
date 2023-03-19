inputNum = int(input("Input Number :"))
for x in range(inputNum):
    print(" "*(inputNum-(x+1)) + "*"*((x*2)+1))