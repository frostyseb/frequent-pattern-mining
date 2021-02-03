import apriori
import fpgrowth
import sys
import os

print('Frequent Pattern Mining\n')

inputChoice = 0
# inputFlag 1 indicates iterate the input choice prompt
inputFlag = 1
# inputFlag 1 indicates iterate the algorithm choice prompt
freqFlag = 1
specialChars = "\'\"~!@#$%^&*()`-=_+<>,.?/:;{}[]|\\"
transRecord = []
minSupp = 0

# the function for entering minimum support count
def supportCount():
    global minSupp
    minSupp = input('\nPlease enter a minimum support count: ')

# the function for choosing the desired frequent pattern mining algorithm
def freqAlgo():
    print(' ------------------------------------- ')
    print('|Please select your desired algorithm |')
    print('|1. Apriori                           |')
    print('|2. FP-Growth                         |')
    print(' ------------------------------------- ')

    freqChoice = input('Enter the number of your choice: ')
    if freqChoice.isalpha() or any(c in specialChars for c in freqChoice):
        print('\nPlease enter an integer.\n')
        freqFlag = 1
    else:
        freqChoice = int(freqChoice)
        if freqChoice == 1:
            print('*** You selected Apriori algorithm. ***\n')
            freqFlag = 0
            supportCount()
            apriori.apriori(transRecord, minSupp)
        elif freqChoice == 2:
            print('*** You selected FP-Growth algorithm. ***\n')
            freqFlag = 0
            supportCount()
            fpgrowth.process(transRecord, minSupp)
        else:
            print('\n*** Please choose between 1 or 2 and try again. ***\n')
            freqFlag = 1

# the function for manual input of transaction records
def manualInput():
    temp = ""
    print('Please enter the transaction records (press q to quit)')
    while True:
        temp = input()
        if temp == 'q':
            print('\n*** You have chosen to stop the manual input. ***\n')
            break
        transRecord.append(temp) #append each record to a list
    freqAlgo()

def fileInput():
    filePath = ''
    check = False

    while check == False:
        filePath = input('Please enter your full file path: ')

        assert os.path.exists(filePath), 'Unfortunately, the file is not found at ' + str(filePath)
        if os.path.exists(filePath) == True:
            check = True
            f = open(filePath, "r")

            while True:
                line = f.readline()
                if not line:
                    break
                transRecord.append(line.strip('\n'))
            freqAlgo()
            # with open(filePath) as f:
            #     transRecord = f.readlines()
            # freqAlgo()


while inputFlag == 1:
    print(' ------------------------------- ')
    print('|Please select an input method: |')
    print('|1. Manual input                |')
    print('|2. File input                  |')
    print(' ------------------------------- ')

    inputChoice = input('Enter the number of your choice: ')
    if inputChoice.isalpha() or any(c in specialChars for c in inputChoice):
        print('\n*** Please enter an integer. ***\n')
        inputFlag = 1
    else:
        inputChoice = int(inputChoice)
        if inputChoice == 1:
            print('*** You selected manual input. ***\n')
            inputFlag = 0
            manualInput()
        elif inputChoice == 2:
            print('*** You selected file input. ***\n')
            inputFlag = 0
            fileInput()
        else:
            print('\n*** Please choose between 1 or 2 and try again. ***\n')
            inputFlag = 1
