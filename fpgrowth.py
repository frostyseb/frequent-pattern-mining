from anytree import Node, RenderTree
from itertools import combinations
import operator
import re
#
# class NodeClass(object, NodeMixin);
#     def __init__



    # # constructor function
    # def __init__(self):
    #     self.value = 0
    #     self.children = []

def process(transRecord, minSupp):
    itemList = []
    mydict = {}
    largestKey = ''
    largestValue = 0
    dictList = []
    tempSortedList = []
    sortedList = []

    # print the transaction records input by user through terminal keyboard
    print('\nYour transaction record is as follows:')
    # print the transaction records
    for each in transRecord:
        print(each)
    print()

    for each in transRecord:
        eachList = each.split(',')
        prev = ''
        k = 2
        for item in eachList:
            item = str(item).replace(' ', '').replace('{', '').replace('}', '')
            if item == prev:
                # if the same item appear twice, the second one will be added with a number starting from 2
                item = str(item) + '(' + str(k) + ')'
                k += 1
            # add the items to dictionary with its respective count
            if item in mydict.keys():
                mydict[item] += 1
            else:
                mydict[item] = 1
            prev = item

    # print the 1-itemsets and their respective counts
    for key, value in mydict.items():
        print(str({key}) + ': ' + str(value))

    for key, value in mydict.items():
        temp = [key, value]
        dictList.append(temp)

    dictList.sort(key=lambda k: (-k[1], k[0]))

    print('\n--------- Sorted List --------')
    for each in dictList:
        print(each)

    buildTree(transRecord, dictList, minSupp)

        # sorted_dict = dict(sorted(mydict.items(), key=operator.itemgetter(1) and operator.itemgetter(0), reverse=True))
        # for key, value in sorted_dict.items():
        #     print(str({key}) + ': ' + str(value))

# function for printing tree
def showTree(node):
    print()
    for pre, _, node in RenderTree(node):
        if node.name == 'Null':
            print("%s%s" % (pre, node.name))
        else:
            print("%s%s: %s" % (pre, node.name, node.count))

# function for building tree
def buildTree(transRecord, dictList, minSupp):
    originalList = []

    # create root node called 'Null'
    root = Node("Null", count=None)

    for each in transRecord:
        # always start from root node
        node = root
        prev = ''
        k = 2
        tempList = []
        eachLine = each.split(',')
        for item in eachLine:
            item = str(item).replace(' ', '').replace('{', '').replace('}', '')
            if item == prev:
                item = str(item) + '(' + str(k) + ')'
                k += 1

            # get a the order of the items to be inserted into the tree
            # and append it to a list
            for each in dictList:
                if item == each[0]:
                    tempList.append([item, each[1]])
            tempList.sort(key=operator.itemgetter(1), reverse=True)

            prev = item

        # insert the nodes in the tree according to the list
        for each in tempList:
            # if node has no children, create a node as its children
            if node.is_leaf:
                child_node = Node(each[0], parent=node, count=1)
                node = child_node
            else:
                foundFlag = False
                for child in node.children:
                    if child.name == each[0]:
                        child.count += 1
                        node = child
                        foundFlag = True
                if foundFlag == False:
                    child_node = Node(each[0], parent=node, count=1)
                    node = child_node

    showTree(root)
    condPattBase(transRecord, dictList, root, minSupp)

# function for extracting frequent pattern
def freqPattern(CFPTlist, transRecord):
    totalTempList = []

    print('\n################### Frequent Pattern ###################')

    for eachRow in CFPTlist:
        print('\n------------------- ' + eachRow[0] + ' -------------------')
        tempList = []
        # if len(eachRow[1]) > 1:
        #     count = 2
        #     tempDict = {}
        #     tempList = []
        #     for eachList in eachRow[1]:
        #         tempCount = -1
        #         for each in eachList:
        #             tempCount += 1
        #             if tempCount % 2 == 0:
        #                 if each not in tempDict.keys():
        #                     tempDict[each] = eachList[tempCount + 1]
        #                 else:
        #                     tempDict[each] += eachList[tempCount + 1]
        #         for key in tempDict.keys():
        #             tempList.append(key)
        #         tempList.append(eachRow[0])
        #         print('this is tempList')
        #         for each in tempList:
        #             print(each)
        #         print('end')
            # while count <= len(tempList):
            #     comb = combinations(tempList, count)
            #     for i in list(comb):
            #         if eachRow[0] in i:
            #             tempValue = 0
            #             for item in i:
            #                 for key, value in tempDict.items():
            #                     if item == key:
            #                         tempValue = value
            #             print(str(i) + ': ' + str(tempValue))
            #     count += 1
        # else:
        #     count = 2
        if len(eachRow[1]) == 1:
            for eachList in eachRow[1]:
                count = 2
                tempList = eachList[0].split(',')
                tempList.append(eachRow[0])
                while count <= len(tempList):
                    comb = combinations(tempList, count)
                    for i in list(comb):
                        if eachRow[0] in i:
                            print(str(i) + ': ' + str(eachList[1]))
                    count += 1
        else:
            count = 2
            for eachList in eachRow[1]:
                tempCount = -1
                for eachItem in eachList:
                    tempCount += 1
                    if tempCount % 2 == 0:
                        if eachItem not in tempList:
                            tempList.append(eachItem)
            tempList.append(eachRow[0])
            while count <= len(tempList):
                comb = combinations(tempList, count)
                for i in list(comb):
                    if eachRow[0] in i:
                        tempValue = 0
                        if count == 2:
                            for item in i:
                                for eachList in eachRow[1]:
                                    for data in eachList:
                                        if data == item:
                                            tempValue += eachList[eachList.index(data)+1]
                        else:
                            lst = []
                            lst = list(i)
                            lst.remove(eachRow[0])
                            check = False
                            for eachList in eachRow[1]:
                                check = all(data in lst for data in eachList[::2])
                                if check == True:
                                    tempValue = eachList[1]
                                    for data in eachList[1::2]:
                                        if data < tempValue:
                                            tempValue = data
                                check = False
                        print(str(i) + ': ' + str(tempValue))
                count += 1
        totalTempList.append(tempList)

    # generating association rules
    list_len = []
    listWithLargestK = []
    rulesList = []
    rulesCount = 1

    list_len = [len(each) for each in totalTempList]

    for each in totalTempList:
        if len(each) == max(list_len):
            listWithLargestK = each

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

    # print('\nthis is newRulesList')
    # for each in newRulesList:
    #     if len(each) == 1:
    #         each = str(each).replace(',', '')
    #     print(each)

    assocList = []
    assocCheck = False
    for i in range(len(newRulesList)):
        for j in range(i, len(newRulesList)):
            if i != j:
                assocCheck = any(element in newRulesList[i] for element in newRulesList[j])
                if assocCheck == False:
                    assocList.append([newRulesList[i], newRulesList[j]])

    # print('\nthis is assocList')
    # for each in assocList:
    #     print(each)
    #
    # print('\nthis is transRecord')
    # for each in transRecord:
    #     print(each)

    totalRow = 0
    for each in transRecord:
        totalRow += 1

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
        for eachTransRow in transRecord:
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


    # for eachRow in assocList:
    #     print()

    # while count < 6:
    #     print('\n------------------- ' +  + ' -------------------')
    #     for eachList in CFPTlist[count]:
    #         tempList.extend(eachList[0].split(','))
    #     tempList.append(CPBlist[count][0])
    #     comb = combinations(tempList, 2)
    #     tempComb = comb
    #     for i in list(tempComb):
    #         if CPBlist[count][0] in i:
    #             print(i, end=': ')
    #     count += 1

    # comb = combinations(list(tempComb))
        # for eachRow in CFPTlist:
        #     for eachList in eachRow:
        #         lst = []
        #         lst = eachList[0].split(',')
        #         for each in lst:
        #             unionSet = set.union({eachCPBrow[0]}, {each})


# function for building conditional FP tree
def condFPtree(CPBlist, transRecord, minSupp):
    CFPTlist = []


    print('\n################### Conditional FP Tree ###################')
    for eachRow in CPBlist:
        print('\n------------------- ' + eachRow[0] + ' -------------------')
        nodes = []
        nodePath = ''
        pathList = []
        count = 0
        root = Node('Null', count=None)

        for eachPath in eachRow[1]:
            node = root
            if eachPath[0] != 'null':
                pathCount = eachPath[1]
                nodes = eachPath[0].split(',')
                for eachNode in nodes:
                    if node.is_leaf:
                        child_node = Node(eachNode, parent=node, count=pathCount)
                        node = child_node
                    else:
                        foundFlag = False
                        for child in node.children:
                            if child.name == eachNode:
                                child.count += pathCount
                                node = child
                                foundFlag = True
                        if foundFlag == False:
                            child_node = Node(eachNode, parent=node, count=pathCount)
                            node = child_node
        showTree(root)
        print()
        for eachNode in root.descendants:
            if eachNode.is_leaf:
                if eachNode.name != 'Null':
                    check = False
                    while check == False:
                        if eachNode.count >= int(minSupp):
                            tempList = []
                            parentList = []

                            try:
                                nodePath = re.search('(.+?/Null/' + eachNode.name + ')\', count', str(eachNode.path[-1])).group(1)
                            except Exception as e:
                                nodePath = re.search('(.+?/Null/.+?' + eachNode.name + ')\', count', str(eachNode.path[-1])).group(1)

                            nodePath = nodePath.replace('Node(\'/Null/', '').replace('/', ',')
                            tempNodePath = re.search('(.+?/' + eachNode.parent.name + ')', str(eachNode.path[-1])).group(1)
                            tempNodePath = tempNodePath.replace('Node(\'/Null/', '').replace('/', ',')
                            # if eachNode.parent.count != eachNode.count and eachNode.parent.count >= int(minSupp):
                            #     parentCheck = False
                            #     currentNode = eachNode
                            #     while parentCheck == False:
                            #         nodePathParent = re.search('(.+?/' + currentNode.parent.name + ')\', count', str(currentNode.parent.path[-1])).group(1)
                            #         nodePathParent = nodePath.replace('Node(\'/Null/', '').replace('/', ',')
                            #         tempList.append(nodePathParent)
                            #         tempList.append(currentNode.parent.count)
                            #         if currentNode.parent.parent.count != currentNode.count and currentNode.parent.parent.count >= int(minSupp) and currentNode.parent.parent.name != 'Null':
                            #             currentNode = currentNode.parent
                            #         else:
                            #             parentCheck = True
                            #     tempList.append(nodePath)
                            #     tempList.append(eachNode.count)
                            #     pathList.append(tempList)
                            parentList = tempNodePath.split(',')
                            parentCheck = False
                            for element in parentList:
                                for tempNode in root.descendants:
                                    if element == tempNode.name:
                                        if tempNode.count >= int(minSupp) and tempNode.count != eachNode.count:
                                            parentCheck = True
                                            tempList.append(tempNode.name)
                                            tempList.append(tempNode.count)
                            if parentCheck == True:
                                tempList.append(eachNode.name)
                            else:
                                tempList.append(nodePath)
                            tempList.append(eachNode.count)
                            pathList.append(tempList)
                            check = True
                        else:
                            if eachNode.parent.name == 'Null':
                                check = True
                            else:
                                eachNode = eachNode.parent

        for everyRow in pathList:
            if len(everyRow) == 2:
                print(everyRow[0] + ': ' + str(everyRow[1]))
            else:
                count = 1
                for each in everyRow:
                    if count % 2 != 0:
                        print(each, end=': ')
                    else:
                        if count == len(everyRow):
                            print(each, end='')
                        else:
                            print(each, end=', ')
                    count += 1
            print()

        CFPTlist.append([eachRow[0], pathList])

    freqPattern(CFPTlist, transRecord)


# function for conditional pattern base
def condPattBase(transRecord, dictList, root, minSupp):
    CPBlist = []
    #reverse the items order of dictList
    dictList.reverse()

    for each in dictList:
        nodePathList = []
        for eachNode in root.descendants:
            if eachNode.name == each[0]:
                nodePath = ''
                # pathNodesList = []
                # print(eachNode.path[-1])
                # for node in eachNode.path[-1]:
                #     if node != root and node != eachNode.name:
                #         pathNodesList.append(node.name)
                nodePath = re.search('\'/Null/(.+?)\'', str(eachNode.path[-1])).group(1)
                # nodePath = nodePath.replace('Node(\'/Null/', '').replace('Node(\'/Null', 'null').replace('/', ',')
                nodePath = nodePath.replace('/' + eachNode.name, '').replace(eachNode.name, 'null').replace('/', ',')

                # CPBlist.append([pathNodesList, eachNode.count])
                if nodePath == 'null':
                    nodePathList.append([nodePath])
                else:
                    nodePathList.append([nodePath, eachNode.count])
        CPBlist.append([each[0], nodePathList])

    print('\n################### Conditional Pattern Base ###################')
    for eachRow in CPBlist:
        print('\n------------------- ' + eachRow[0] + ' -------------------')
        for eachPath in eachRow[1]:
            if len(eachPath) == 1:
                print(eachPath[0])
            else:
                print(eachPath[0] + ': ' + str(eachPath[1]))

    condFPtree(CPBlist, transRecord, minSupp)
