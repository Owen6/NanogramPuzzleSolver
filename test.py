import itertools
import re

def main():
    rule = [2,3]
    test = [1,2,4,5]
    sample = [2,3,'X','X','X','X','X']
    combinations = list(itertools.combinations_with_replacement(sample, 7))
    validCombos = []

    for i in range(len(combinations)):
        if(ruleInList(rule,combinations[i])):
            validCombos.append(combinations[i])

    print(validCombos)
    print(len(validCombos), len(combinations))
    #print(ruleInList(rule,sample))

def ruleInList(x,y):
    x_str = ' '.join(map(str, x))
    y_str = ' '.join(map(str, y))
    instances = re.findall(x_str, y_str)

    return len(instances) > 0


if __name__ == "__main__":
    main()
