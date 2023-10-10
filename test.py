import itertools
import re
from collections import Counter

def main():
    rule = [2,3]
    rule2 = [2,3]
    #test = [1,2,4,5]
    sample = [2,3,'X','X','X','X','X']
    #combinations = list(itertools.combinations_with_replacement(sample, 7))
    combinations = list(itertools.product(sample,sample,sample,sample,sample,sample,sample))
    validCombos = []

    for i in combinations:
        if ruleInList(rule,i):
            #if not ruleInList(i, validCombos):
            validCombos.append(i)
    validCombos = list(set(validCombos))
    #for i in range(len(combinations)):
    #    if(ruleInList(rule,combinations[i])):
    #        if(not ruleInList(combinations[i],validCombos)):
    #            validCombos.append(combinations[i])

    print(validCombos)
    #print(combinations)
    print(len(validCombos), len(combinations))
    #print(ruleInList(rule,sample))

def ruleInList(x,y):
    x_str = ' '.join(map(str, x))
    y_str = ' '.join(map(str, y))
    instances = re.findall(x_str, y_str)

    temp = Counter(y)
    temp2 = Counter(x)
    #order = []
    valid = 0
    for i in range(len(x)):
        if temp[x[i]] == temp2[x[i]]:
            valid = valid + 1
            #order.append(x[i])
    return len(instances) > 0 and valid == len(x) #and x == order


if __name__ == "__main__":
    main()
