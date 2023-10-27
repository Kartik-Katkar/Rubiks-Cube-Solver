import twophase.solver as sv
import sys
def print_color_square(color):
    colors = {
        'R': '\x1b[48;5;196m  \x1b[0m',
        'G': '\x1b[48;5;46m  \x1b[0m',
        'O': '\x1b[48;5;208m  \x1b[0m',
        'B': '\x1b[48;5;21m  \x1b[0m',
        'Y': '\x1b[48;5;226m  \x1b[0m',
        'W': '\x1b[48;5;231m  \x1b[0m',
        'T': '  '  # No color
    }

    if color in colors:
        print(colors[color], end=' ')
    else:
        print(f"Color '{color}' not found ")  #Will never happen , but just in case lol

goal = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"

def printCubeDefault():
    #First 3 lines -> Transparent and Yellow 
    for j in range(3):
        for i in range(3):
            print_color_square("T")

        for i in range(3):
            print_color_square("Y")

        print("\n")

    #Body of the main Cube 
    for j in range(3):
        for i in range(3):
            print_color_square("B")
        
        for i in range(3):
            print_color_square("R")
        
        for i in range(3):
            print_color_square("G")
        
        for i in range(3):
            print_color_square("O")

        print("\n")
    
    #Last Block of the Cube 
    for j in range(3):
        for i in range(3):
            print_color_square("T")

        for i in range(3):
            print_color_square("W")
        
        print("\n")

    #Done printing the cube 
    print("\n")

def printCubeCustom(colorString):
    for i in range(9):
        print_color_square(colorString[i])
        if((i+1)%3 == 0):
            print("\n")

def printCube(inpstr1,inpstr2,inpstr3,inpstr4,inpstr5,inpstr6):
    
    cntr = 0
    #Printing First Block of Cubes 
    for j in range(3):
        for i in range(3):
            print_color_square("T")
        
        for i in range(3):
            print_color_square(inpstr1[cntr])
            cntr += 1
        
        print("\n")
    
        
    cntr = 0
    #Printing main body of the cube
    for j in range(3):
        cntr = j*3
        for i in range(3):
            print_color_square(inpstr2[cntr])
            cntr += 1
        
        cntr = j*3

        for i in range(3):
            print_color_square(inpstr3[cntr])
            cntr += 1
        
        cntr = j*3

        for i in range(3):
            print_color_square(inpstr4[cntr])
            cntr += 1

        cntr = j*3

        for i in range(3):
            print_color_square(inpstr5[cntr])
            cntr += 1

        print("\n")
        
    #printing Last matrix of the cube 
    cntr = 0
    for j in range(3):
        for i in range(3):
            print_color_square("T")
        
        for i in range(3):
            print_color_square(inpstr6[cntr])
            cntr += 1
        
        print("\n")
    #Printing finished 

def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp

def moveU(num, matrixU, matrixR, matrixF, matrixL, matrixB):
    for i in range(num):
        temp1 = matrixL[0][0]
        temp2 = matrixL[0][1]
        temp3 = matrixL[0][2]

        matrixL[0][0] = matrixF[0][0]
        matrixL[0][1] = matrixF[0][1]
        matrixL[0][2] = matrixF[0][2]

        matrixF[0][0] = matrixR[0][0]
        matrixF[0][1] = matrixR[0][1]
        matrixF[0][2] = matrixR[0][2]

        matrixR[0][0] = matrixB[0][0]
        matrixR[0][1] = matrixB[0][1]
        matrixR[0][2] = matrixB[0][2]

        matrixB[0][0] = temp1
        matrixB[0][1] = temp2
        matrixB[0][2] = temp3

        #Rotate the upper face 
        rotate90Clockwise(matrixU)

    #Done

def moveD(num, matrixD, matrixR, matrixF, matrixL, matrixB):
    for i in range(num):
        temp1 = matrixF[2][0]
        temp2 = matrixF[2][1]
        temp3 = matrixF[2][2]

        matrixF[2][0] = matrixL[2][0]
        matrixF[2][1] = matrixL[2][1]
        matrixF[2][2] = matrixL[2][2]

        matrixL[2][0] = matrixB[2][0]
        matrixL[2][1] = matrixB[2][1]
        matrixL[2][2] = matrixB[2][2]

        matrixB[2][0] = matrixR[2][0]
        matrixB[2][1] = matrixR[2][1]
        matrixB[2][2] = matrixR[2][2]

        matrixR[2][0] = temp1
        matrixR[2][1] = temp2
        matrixR[2][2] = temp3
        
        #Rotate the Down face
        rotate90Clockwise(matrixD)

    #Done

def moveF(num, matrixD, matrixR, matrixF, matrixL, matrixU):
    for i in range(num):
        
        temp1 = matrixL[0][2]
        temp2 = matrixL[1][2]
        temp3 = matrixL[2][2]

        matrixL[0][2] = matrixD[0][0]
        matrixL[1][2] = matrixD[0][1]
        matrixL[2][2] = matrixD[0][2]

        matrixD[0][0] = matrixR[2][0]
        matrixD[0][1] = matrixR[1][0]
        matrixD[0][2] = matrixR[0][0]

        matrixR[0][0] = matrixU[2][0]
        matrixR[1][0] = matrixU[2][1]
        matrixR[2][0] = matrixU[2][2]

        matrixU[2][0] = temp3
        matrixU[2][1] = temp2
        matrixU[2][2] = temp1

        #Rotate the Front face
        rotate90Clockwise(matrixF)
    
    #Done
    
def moveB(num, matrixD, matrixR, matrixB, matrixL, matrixU):
    for i in range(num):

        temp1 = matrixU[0][0]
        temp2 = matrixU[0][1]
        temp3 = matrixU[0][2]

        matrixU[0][0] = matrixR[0][2]
        matrixU[0][1] = matrixR[1][2]
        matrixU[0][2] = matrixR[2][2]

        matrixR[0][2] = matrixD[2][2]
        matrixR[1][2] = matrixD[2][1]
        matrixR[2][2] = matrixD[2][0]

        matrixD[2][0] = matrixL[0][0]
        matrixD[2][1] = matrixL[1][0]
        matrixD[2][2] = matrixL[2][0]

        matrixL[0][0] = temp3
        matrixL[1][0] = temp2
        matrixL[2][0] = temp1

        #rotate the back face 
        rotate90Clockwise(matrixB)
    #Done

def moveR(num, matrixD, matrixR, matrixB, matrixF, matrixU):
    for i in range(num):
        
        temp1 = matrixF[0][2]
        temp2 = matrixF[1][2]
        temp3 = matrixF[2][2]

        matrixF[0][2] = matrixD[0][2]
        matrixF[1][2] = matrixD[1][2]
        matrixF[2][2] = matrixD[2][2]

        matrixD[0][2] = matrixB[2][0]
        matrixD[1][2] = matrixB[1][0]
        matrixD[2][2] = matrixB[0][0]

        matrixB[0][0] = matrixU[2][2]
        matrixB[1][0] = matrixU[1][2]
        matrixB[2][0] = matrixU[0][2]

        matrixU[0][2] = temp1
        matrixU[1][2] = temp2
        matrixU[2][2] = temp3

        #rotate the Right face
        rotate90Clockwise(matrixR)
    #Done

def moveL(num, matrixD, matrixL, matrixB, matrixF, matrixU):
    for i in range(num):

        temp1 = matrixF[0][0]
        temp2 = matrixF[1][0]
        temp3 = matrixF[2][0]

        matrixF[0][0] = matrixD[0][0]
        matrixF[1][0] = matrixD[1][0]
        matrixF[2][0] = matrixD[2][0]

        matrixD[0][0] = matrixB[2][2]
        matrixD[1][0] = matrixB[1][2]
        matrixD[2][0] = matrixB[0][2]

        matrixB[0][2] = matrixU[2][0]
        matrixB[1][2] = matrixU[1][0]
        matrixB[2][2] = matrixU[0][0]

        matrixU[0][0] = temp1
        matrixU[1][0] = temp2
        matrixU[2][0] = temp3

        #rotate the left face in anticlockwise direction
        rotate90Clockwise(matrixL)
        rotate90Clockwise(matrixL)
        rotate90Clockwise(matrixL)
    #Done finally 


def string_to_3x3_matrix(input_string):
    matrix = [[input_string[i * 3 + j] for j in range(3)] for i in range(3)]
    return matrix

def matrix_to_string(matrix):
    result_string = ''
    for row in matrix:
        for element in row:
            result_string += element
    return result_string

def check_Y(input_string):
    middle_index = len(input_string) // 2
    return input_string[middle_index] == "Y"

def check_W(input_string):
    middle_index = len(input_string) // 2
    return input_string[middle_index] == "W"

def check_B(input_string):
    middle_index = len(input_string) // 2
    return input_string[middle_index] == "B"

def check_R(input_string):
    middle_index = len(input_string) // 2
    return input_string[middle_index] == "R"

def check_G(input_string):
    middle_index = len(input_string) // 2
    return input_string[middle_index] == "G"

def check_O(input_string):
    middle_index = len(input_string) // 2
    return input_string[middle_index] == "O"

def checkFinalValidity(inpstr1,inpstr2,inpstr3,inpstr4,inpstr5,inpstr6):
    cntR = 0
    cntB = 0
    cntG = 0
    cntY = 0
    cntO = 0
    cntW = 0

    for i in range(9):
        if(inpstr1[i] == "R"):
            cntR+=1
        if(inpstr2[i] == "R"):
            cntR+=1
        if(inpstr3[i] == "R"):
            cntR+=1
        if(inpstr4[i] == "R"):
            cntR+=1
        if(inpstr5[i] == "R"):
            cntR+=1
        if(inpstr6[i] == "R"):
            cntR+=1

        if(inpstr1[i] == "B"):
            cntB+=1
        if(inpstr2[i] == "B"):
            cntB+=1
        if(inpstr3[i] == "B"):
            cntB+=1
        if(inpstr4[i] == "B"):
            cntB+=1
        if(inpstr5[i] == "B"):
            cntB+=1
        if(inpstr6[i] == "B"):
            cntB+=1

        if(inpstr1[i] == "G"):
            cntG+=1
        if(inpstr2[i] == "G"):
            cntG+=1
        if(inpstr3[i] == "G"):
            cntG+=1
        if(inpstr4[i] == "G"):
            cntG+=1
        if(inpstr5[i] == "G"):
            cntG+=1
        if(inpstr6[i] == "G"):
            cntG+=1

        if(inpstr1[i] == "O"):
            cntO+=1
        if(inpstr2[i] == "O"):
            cntO+=1
        if(inpstr3[i] == "O"):
            cntO+=1
        if(inpstr4[i] == "O"):
            cntO+=1
        if(inpstr5[i] == "O"):
            cntO+=1
        if(inpstr6[i] == "O"):
            cntO+=1
        
        if(inpstr1[i] == "Y"):
            cntY+=1
        if(inpstr2[i] == "Y"):
            cntY+=1
        if(inpstr3[i] == "Y"):
            cntY+=1
        if(inpstr4[i] == "Y"):
            cntY+=1
        if(inpstr5[i] == "Y"):
            cntY+=1
        if(inpstr6[i] == "Y"):
            cntY+=1
        
        if(inpstr1[i] == "W"):
            cntW+=1
        if(inpstr2[i] == "W"):
            cntW+=1
        if(inpstr3[i] == "W"):
            cntW+=1
        if(inpstr4[i] == "W"):
            cntW+=1
        if(inpstr5[i] == "W"):
            cntW+=1
        if(inpstr6[i] == "W"):
            cntW+=1
    
    #Finally!
    if(cntR == 9 and cntB == 9 and cntG == 9 and cntY == 9 and cntO == 9 and cntW == 9):
        return True
    else:
        return False

def stringmod(st):
    res = ""
    for i in range(9):
        if( st[i] == "U"):
            res += "Y" 
        elif(st[i] == "D"):
            res += "W"
        elif(st[i] == "R"):
            res += "G"
        elif(st[i] == "L"):
            res += "B"
        elif(st[i] == "F"):
            res += "R"
        elif(st[i] == "B"):
            res += "O"

    return res

#Telling the user to Hold the cube in the following orientation 
print("Hello User, Welcome to the Rubik's Cube solver ! \n \n ")
print("Please look at the cube below and hold Your cube in the same orientation \n \n")
print("NOTE : Look at the center face color of the cube \n")

#Now printing the entire Cube 
printCubeDefault()

#Asking to Register the faces of the Cube
print("Now please Register the faces of Your cube  \n")
print("Enter the Following notations for the corresponding colors : \n ")
print("1. for RED color, enter R ")
print("2. for BLUE color, enter B ")
print("3. for GREEN color, enter G ")
print("4. for ORANGE color, enter O ")
print("5. for YELLOW color, enter Y ")
print("6. for WHITE color, enter W \n \n ")

#Starting with YELLOW ***********************************************
print("With respect to the above orientation, Please register the Face with YELLOW color at the center \n ")
i = 0
str1 = ""
str1cpy = ""
while(i < 9):
    print("Enter color at Face ",i+1)
    col = input()
    if(col == "R"):
        str1 += "F"
        str1cpy += "R"
        i+=1
    elif(col == "B"):
        str1 += "L"
        str1cpy += "B"
        i+=1
    elif(col == "G"):
        str1 += "R"
        str1cpy += "G"
        i+=1
    elif(col == "O"):
        str1 += "B"
        str1cpy += "O"
        i+=1
    elif(col == "Y"):
        str1 += "U"
        str1cpy += "Y"
        i+=1
    elif(col == "W"):
        str1 += "D"
        str1cpy += "W"
        i+=1
    else:
        print("Invalid Input, please enter again ")
    print("\n")

# Checking Validation
result = check_Y(str1cpy)
if(result == False):
    print("Invalid Cube Configuration. Aborting Program, please restart !")
    sys.exit()

print("Registered Face is as Below : \n ")
printCubeCustom(str1cpy)

#Moving on to BLUE ***********************************************

print("Please register the Face with BLUE color at the center \n ")
i = 0
str2 = ""
str2cpy = ""
while(i < 9):
    print("Enter color at Face ",i+1)
    col = input()
    if(col == "R"):
        str2 += "F"
        str2cpy += "R"
        i+=1
    elif(col == "B"):
        str2 += "L"
        str2cpy += "B"
        i+=1
    elif(col == "G"):
        str2 += "R"
        str2cpy += "G"
        i+=1
    elif(col == "O"):
        str2 += "B"
        str2cpy += "O"
        i+=1
    elif(col == "Y"):
        str2 += "U"
        str2cpy += "Y"
        i+=1
    elif(col == "W"):
        str2 += "D"
        str2cpy += "W"
        i+=1
    else:
        print("Invalid Input, please enter again ")
    print("\n")

# Checking Validation
result = check_B(str2cpy)
if(result == False):
    print("Invalid Cube Configuration. Aborting Program, please restart !")
    sys.exit()

print("Registered Face is as Below : \n ")
printCubeCustom(str2cpy)

#Moving on to color RED ***********************************************
print("Please register the Face with RED color at the center \n ")
i = 0
str3 = ""
str3cpy = ""
while(i < 9):
    print("Enter color at Face ",i+1)
    col = input()
    if(col == "R"):
        str3 += "F"
        str3cpy += "R"
        i+=1
    elif(col == "B"):
        str3 += "L"
        str3cpy += "B"
        i+=1
    elif(col == "G"):
        str3 += "R"
        str3cpy += "G"
        i+=1
    elif(col == "O"):
        str3 += "B"
        str3cpy += "O"
        i+=1
    elif(col == "Y"):
        str3 += "U"
        str3cpy += "Y"
        i+=1
    elif(col == "W"):
        str3 += "D"
        str3cpy += "W"
        i+=1
    else:
        print("Invalid Input, please enter again ")
    print("\n")

# Checking Validation
result = check_R(str3cpy)
if(result == False):
    print("Invalid Cube Configuration. Aborting Program, please restart !")
    sys.exit()

print("Registered Face is as Below : \n ")
printCubeCustom(str3cpy)

#Moving on to color GREEN ***********************************************

print("Please register the Face with GREEN color at the center \n ")
i = 0
str4 = ""
str4cpy = ""
while(i < 9):
    print("Enter color at Face ",i+1)
    col = input()
    if(col == "R"):
        str4 += "F"
        str4cpy += "R"
        i+=1
    elif(col == "B"):
        str4 += "L"
        str4cpy += "B"
        i+=1
    elif(col == "G"):
        str4 += "R"
        str4cpy += "G"
        i+=1
    elif(col == "O"):
        str4 += "B"
        str4cpy += "O"
        i+=1
    elif(col == "Y"):
        str4 += "U"
        str4cpy += "Y"
        i+=1
    elif(col == "W"):
        str4 += "D"
        str4cpy += "W"
        i+=1
    else:
        print("Invalid Input, please enter again ")
    print("\n")

# Checking Validation
result = check_G(str4cpy)
if(result == False):
    print("Invalid Cube Configuration. Aborting Program, please restart !")
    sys.exit()

print("Registered Face is as Below : \n ")
printCubeCustom(str4cpy)

#Moving on to color ORANGE ***********************************************

print("Please register the Face with ORANGE color at the center \n ")
i = 0
str5 = ""
str5cpy = ""
while(i < 9):
    print("Enter color at Face ",i+1)
    col = input()
    if(col == "R"):
        str5 += "F"
        str5cpy += "R"
        i+=1
    elif(col == "B"):
        str5 += "L"
        str5cpy += "B"
        i+=1
    elif(col == "G"):
        str5 += "R"
        str5cpy += "G"
        i+=1
    elif(col == "O"):
        str5 += "B"
        str5cpy += "O"
        i+=1
    elif(col == "Y"):
        str5 += "U"
        str5cpy += "Y"
        i+=1
    elif(col == "W"):
        str5 += "D"
        str5cpy += "W"
        i+=1
    else:
        print("Invalid Input, please enter again ")
    print("\n")

# Checking Validation
result = check_O(str5cpy)
if(result == False):
    print("Invalid Cube Configuration. Aborting Program, please restart !")
    sys.exit()

print("Registered Face is as Below : \n ")
printCubeCustom(str5cpy)

#Moving on to the final color WHITE ***************************************

print("Please register the Face with WHITE color at the center \n ")
i = 0
str6 = ""
str6cpy = ""
while(i < 9):
    print("Enter color at Face ",i+1)
    col = input()
    if(col == "R"):
        str6 += "F"
        str6cpy += "R"
        i+=1
    elif(col == "B"):
        str6 += "L"
        str6cpy += "B"
        i+=1
    elif(col == "G"):
        str6 += "R"
        str6cpy += "G"
        i+=1
    elif(col == "O"):
        str6 += "B"
        str6cpy += "O"
        i+=1
    elif(col == "Y"):
        str6 += "U"
        str6cpy += "Y"
        i+=1
    elif(col == "W"):
        str6 += "D"
        str6cpy += "W"
        i+=1
    else:
        print("Invalid Input, please enter again ")
    print("\n")

# Checking Validation
result = check_W(str6cpy)
if(result == False):
    print("Invalid Cube Configuration. Aborting Program, please restart !")
    sys.exit()

print("Registered Face is as Below : \n ")
printCubeCustom(str6cpy)

finalResult = checkFinalValidity(str1cpy,str2cpy,str3cpy,str4cpy,str5cpy,str6cpy)

if(finalResult == False):
    print("Configured Cube is NOT Valid! Aborting Program, Please Restart !")
    sys.exit()

print("Below is the configured Cube ")

printCube(str1cpy,str2cpy,str3cpy,str4cpy,str5cpy,str6cpy)

cubestring = str1 + str4 + str3 + str6 + str2 + str5

resultstring = sv.solve(cubestring,20,2)
print(resultstring)

finalsteps = resultstring
totalmoves = 0

matrixU = string_to_3x3_matrix(str1)
matrixR = string_to_3x3_matrix(str4)
matrixF = string_to_3x3_matrix(str3)
matrixD = string_to_3x3_matrix(str6)
matrixL = string_to_3x3_matrix(str2)
matrixB = string_to_3x3_matrix(str5)

resultstr = resultstring.split()

for char in resultstr:
    if(char[0] == '('):
        dig1 = 0
        dig2 = -1
        if(char[1] >='0' and char[1] <='9'):
            dig1 = int(char[1])
        if(char[2] >='0' and char[2] <='9'):
            dig2 = int(char[2])
        rs = 0
        if(dig2 != -1):
            rs = 10*dig1 + dig2
        else:
            rs = dig1
        
        totalmoves += rs

        print("Finished the moveset !")
        break

    if(char[0] == 'U'):
        nump = char[1]
        num = int(nump)
        moveU(num, matrixU, matrixR, matrixF, matrixL, matrixB)

    elif(char[0] == 'D'):
        nump = char[1]
        num = int(nump)
        moveD(num, matrixD, matrixR, matrixF, matrixL, matrixB)
    
    elif(char[0] == 'F'):
        nump = char[1]
        num = int(nump)
        moveF(num, matrixD, matrixR, matrixF, matrixL, matrixU)

    elif(char[0] == 'B'):
        nump = char[1]
        num = int(nump)
        moveB(num, matrixD, matrixR, matrixB, matrixL, matrixU)

    elif(char[0] == 'R'):
        nump = char[1]
        num = int(nump)
        moveR(num, matrixD, matrixR, matrixB, matrixF, matrixU)

    elif(char[0] == 'L'):
        nump = char[1]
        num = int(nump)
        moveL(num, matrixD, matrixL, matrixB, matrixF, matrixU)



strU = matrix_to_string(matrixU)
strD = matrix_to_string(matrixD)
strF = matrix_to_string(matrixF)
strB = matrix_to_string(matrixB)
strR = matrix_to_string(matrixR)
strL = matrix_to_string(matrixL)

cubestring = strU + strR + strF + strD + strL + strB

str1cpy = stringmod(strU)
str2cpy = stringmod(strL)
str3cpy = stringmod(strF)
str4cpy = stringmod(strR)
str5cpy = stringmod(strB)
str6cpy = stringmod(strD)

print(cubestring)
printCube(str1cpy,str2cpy,str3cpy,str4cpy,str5cpy,str6cpy)

while(cubestring != goal):
    resultstring = sv.solve(cubestring,20,2)
    print(resultstring)

    finalsteps += resultstring

    resultstr = resultstring.split()

    matrixU = string_to_3x3_matrix(strU)
    matrixR = string_to_3x3_matrix(strR)
    matrixF = string_to_3x3_matrix(strF)
    matrixD = string_to_3x3_matrix(strD)
    matrixL = string_to_3x3_matrix(strL)
    matrixB = string_to_3x3_matrix(strB)

    for char in resultstr:
        if(char[0] == '('):
            dig1 = 0
            dig2 = -1
            if(char[1] >='0' and char[1] <='9'):
                dig1 = int(char[1])
            if(char[2] >='0' and char[2] <='9'):
                dig2 = int(char[2])
            rs = 0
            if(dig2 != -1):
                rs = 10*dig1 + dig2
            else:
                rs = dig1
            
            totalmoves += rs

            print("Finished the moveset !")
            break

        if(char[0] == 'U'):
            nump = char[1]
            num = int(nump)
            moveU(num, matrixU, matrixR, matrixF, matrixL, matrixB)

        elif(char[0] == 'D'):
            nump = char[1]
            num = int(nump)
            moveD(num, matrixD, matrixR, matrixF, matrixL, matrixB)
    
        elif(char[0] == 'F'):
            nump = char[1]
            num = int(nump)
            moveF(num, matrixD, matrixR, matrixF, matrixL, matrixU)

        elif(char[0] == 'B'):
            nump = char[1]
            num = int(nump)
            moveB(num, matrixD, matrixR, matrixB, matrixL, matrixU)

        elif(char[0] == 'R'):
            nump = char[1]
            num = int(nump)
            moveR(num, matrixD, matrixR, matrixB, matrixF, matrixU)

        elif(char[0] == 'L'):
            nump = char[1]
            num = int(nump)
            moveL(num, matrixD, matrixL, matrixB, matrixF, matrixU)


    strU = matrix_to_string(matrixU)
    strD = matrix_to_string(matrixD)
    strF = matrix_to_string(matrixF)
    strB = matrix_to_string(matrixB)
    strR = matrix_to_string(matrixR)
    strL = matrix_to_string(matrixL)

    cubestring = strU + strR + strF + strD + strL + strB
    
    str1cpy = stringmod(strU)
    str2cpy = stringmod(strL)
    str3cpy = stringmod(strF)
    str4cpy = stringmod(strR)
    str5cpy = stringmod(strB)
    str6cpy = stringmod(strD)

    printCube(str1cpy,str2cpy,str3cpy,str4cpy,str5cpy,str6cpy)
    print(cubestring)

print("Goal state achived !")
print("Total MoveSet = ",finalsteps)
print("Total moves taken : ",totalmoves)