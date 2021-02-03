from itertools import combinations

# function for the apriori algorithm processes
def apriori(lst, minSupp):
    mydict = {}
    totalList = []
    finalList = []
    k = 1

    # print the transaction records input by user through terminal keyboard
    print('\nYour transaction record is as follows:')
    # print the transaction records
    for each in lst:
        print(each)
    print()

    # split each row into array and append them to totalList
    for each in lst:
        totalList.extend(each.split(','))

    # prev acts as a check for same items
    prev = ''
    count = 2
    # count the frequency of each items and store as dictionary
    for each in totalList:
        each = str(each).replace(' ', '').replace('{', '').replace('}', '')
        if each == prev:
            # if the same item appear twice, the second one will be added with a number starting from 2
            each = str(each) + '(' + str(k) + ')'
            count += 1
        # add the items to dictionary with its respective count
        if each in mydict.keys():
            mydict[each] += 1
        else:
            mydict[each] = 1
        prev = each

    # border
    print('############################### 1-itemset ###############################')
    print('\nMin. Support Count: ' + str(minSupp))
    print('\n------------------------ Count of each 1-itemset ------------------------')

    # print the count of all 1-itemset
    for key, value in mydict.items():
        print(str({key}) + ': ' + str(value))

    print('\n--------------- 1-itemset that meets the min support count ---------------')

    # compare dictionary values with min. support count and
    # append to finalList as set
    for key, value in mydict.items():
        if value >= int(minSupp):
            finalList.append({key})
            print(str({key}) + ': ' + str(value))

#     processLoop(lst, finalList, minSupp, k)
#
# def processLoop(lst, finalList, minSupp, k):

    # repeat the loop when the frequent pattern is not found
    loopCheck = False
    while len(finalList) != 1:
    # while loopCheck == False:
    # for i in range(0, 4):
        nextList = []
        mydict = {}
        check = False
        checkFinal = False

        # k represents k-itemset
        k += 1
        # border
        print('\n\n############################### ' + str(k) + '-itemset ###############################')
        print('\nMin. Support Count: ' + str(minSupp))
        print('\n------------------------ Count of each ' + str(k) + '-itemset ------------------------')

        # join the (k-1)-itemset together to form k-itemsets
        for i in range(len(finalList)):
            for j in range(i, len(finalList)):
                if finalList[i] != finalList[j]:
                    # eliminate the possibility of (k+)-itemsets
                    if len(set.union(finalList[i], finalList[j])) == k:
                        # set union will not allow duplicates hence unique members
                        unionSet = set.union(finalList[i], finalList[j])
                        if unionSet not in nextList:
                            nextList.append(unionSet)

        # clear contents of finalList to be used for next loop
        finalList = []

        # count the frequency of each itemset and store in dictionary
        for eachSet in nextList:
            for eachRow in lst:
                #
                check = all(eachLetter in eachRow for eachLetter in eachSet)
                if check is True:
                    if str(eachSet) in mydict.keys():
                        mydict[str(eachSet)] += 1
                    else:
                        mydict[str(eachSet)] = 1
            # if the count meets the min. support count, it is appended to finalList
            if mydict[str(eachSet)] >= int(minSupp):
                if eachSet not in finalList:
                    finalList.append(eachSet)



        # for each, element in zip(nextList, lst):
        #     eachList = str(each).replace('{', '').replace('}', '').replace('\'', '').replace(' ', '').split(',')
        #     lstList = element.replace(' ', '').split(',')
        #     check = all(item in lstList for item in eachList)
        #     if check is True:
        #         if str(each).replace('{', '').replace('}', '').replace('\'', '').replace(' ', '') in dict.keys():
        #             dict[str(each).replace('{', '').replace('}', '').replace('\'', '').replace(' ', '')] += 1
        #         else:
        #             dict[str(each).replace('{', '').replace('}', '').replace('\'', '').replace(' ', '')] = 1


        # printing the k-itemsets and its count
        for key, value in mydict.items():
            print(key + ': ' + str(value))

        print('\n--------------- ' + str(k) + '-itemset that meets the min support count ---------------')



        # for key, value in dict.items():
        #     if value >= int(minSupp):
        #         finalList.append({key})
        #         print(str(key) + ': ' + str(value))


        # print the k-itemsets and their counts that meet the min. support count
    for each in finalList:
        print(str(each) + ": " + str(mydict[str(each)]))

    list_len = []
    list_len = [len(each) for each in finalList]

    listWithLargestK = []
    for each in finalList:
        if len(each) == max(list_len):
            listWithLargestK = each

    rulesList = []
    rulesCount = 1
    while rulesCount < len(listWithLargestK):
        rulesComb = combinations(listWithLargestK, rulesCount)
        rulesCount += 1
        rulesList.append(list(rulesComb))

    # print('\nthis is rulesList')
    # for each in rulesList:
    #     print(each)

    newRulesList = []
    for eachRow in rulesList:
        for each in eachRow:
            newRulesList.append(each)

    assocList = []
    assocCheck = False
    for i in range(len(newRulesList)):
        for j in range(i, len(newRulesList)):
            if i != j:
                assocCheck = any(element in newRulesList[i] for element in newRulesList[j])
                if assocCheck == False:
                    assocList.append([newRulesList[i], newRulesList[j]])
    #
    # print('\n this is assocList')
    # for each in assocList:
    #     print(each)

    totalRow = 0
    for each in lst:
        totalRow += 1

    # print('\n this is lst')
    # for each in lst:
    #     print(each)


    finalAssocList = []
    print('\n\n################### Association Rules ###################\n')
    for eachAssocRow in assocList:
        supportCheck = False
        supportCount = 0
        support = 0
        firstCheck = False
        firstCount = 0
        secondCheck = False
        secondCount = 0
        confidenceCount = 0
        for eachTransRow in lst:
            supportCheck = all(element in eachTransRow for element in eachAssocRow[0]) and all(element in eachTransRow for element in eachAssocRow[1])
            if supportCheck == True:
                supportCount += 1
            firstCheck = all(element in eachTransRow for element in eachAssocRow[0])
            if firstCheck == True:
                firstCount += 1
        print(str(eachAssocRow[0]) + ' => ' + str(eachAssocRow[1]), end='\t')
        print('support: ' + str(supportCount) + '/' + str(totalRow) + ' = ' + str(supportCount/totalRow), end='\t')
        print('confidence: ' + str(supportCount) + '/' + str(firstCount) + ' = ' + str(supportCount/firstCount))
        finalAssocList.append([str(eachAssocRow[0]) + ' => ' + str(eachAssocRow[1]), str(supportCount/totalRow), str(supportCount/firstCount)])

    supThreshold = 0
    confThreshold = 0
    supThreshold = input('\n\nPlease enter a minimum support threshold: ')
    confThreshold = input('Please enter a minimum confidence threshold: ')
    print('\n\n################### Strong Rules ###################\n')
    for each in finalAssocList:
        if float(each[1]) >= float(supThreshold) and float(each[2]) >= float(confThreshold):
            print(each[0] + '\t' + 'support: ' + each[1] + '\t' + 'confidence: ' + each[2])

        # loopCheck = all(mydict[str(each)] == mydict[list(mydict.values())[0]] for each in finalList)

    # largestK = -1
    # for eachSet in finalList:
    #     count = 0
    #     for each in eachSet:
    #         count += 1
    #     if count > largestK:
    #         largestK += 1
    #
    # print('k-itemset with the largest k: ' + str(finalList[largestK]))
    # tempList = []
    # for each in finalList[largestK]:
    #     tempList.append(each)
    #
    # combList = []
    # for i in range(1, len(tempList)):
    #     comb = combinations(tempList, i)
    #     for data in list(comb):
    #         combList.append(data)
    #
    # for each in combList:
    #     print(each)
    #
    # for each in combList:
    #     for eachRow in lst:
    #         check = all(item in eachRow for item in each)




    # checkFinal = all(dict[str(eachSet)] >= int(minSupp) for each in finalList)
    # if checkFinal is False:
    #     processLoop(lst, finalList, minSupp, k)


    # dict = {}
    # totalList = []
    # finalList = []
    # nextList = []
    # global k
    #
    # # split each transaction record into a list of items and
    # # append them to the totalList
    # for each in lst:
    #     if isinstance(each, set) == True:
    #         totalList.append(each)
    #     else:
    #         totalList.extend(each.split(','))
    #
    # # join the remaining items using union and
    # # append them to nextList
    # for i in range(len(finalList)):
    #     for j in range(i, len(finalList)):
    #         if finalList[i] != finalList[j]:
    #             nextList.append(set.union(finalList[i], finalList[j]))
    #
    # # # clean the data
    # # for each in totalList:
    # #     each = str(each).replace(' ', '')
    # #     print(each)
    #
    # print()
    #
    # # count the frequency of each items and store as dictionary
    # for each in totalList:
    #     each = str(each).replace(' ', '').replace('{', '').replace('}', '')
    #     if each in dict.keys():
    #         dict[each] += 1
    #     else:
    #         dict[each] = 1
    #
    # # for key, value in dict.items():
    # #     print(str(key) + ": " + str(value))
    #
    # # compare dictionary values with min. support count and
    # # append to finalList as set
    # for key, value in dict.items():
    #     if value >= int(minSupp):
    #         finalList.append({key})
    #
    # # print the items left in current iteration
    # for each in finalList:
    #     print(each)
    # print()
    #
    # # join the remaining items using union and
    # # append them to nextList
    # for i in range(len(finalList)):
    #     for j in range(i, len(finalList)):
    #         if finalList[i] != finalList[j]:
    #             nextList.append(set.union(finalList[i], finalList[j]))
    #
    # # print the the value of k
    # k += 1
    # print('================= ' + str(k) + '-itemset ====================')
    #
    # # print the items after joining
    # for each in nextList:
    #     print(each)
    # print()
    #
    # if k < 4:
    #     processLoop(nextList, minSupp)
