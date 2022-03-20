def parChecker(parSeq):
    par = []
    for i in parSeq:
        if i == "(":
            par.append(i)
        elif i == ")":
            if par == []:
                return False
            else:
                par.pop()
    if par == []:
        return True
    else:
        return False


parSeq = input()
print(parChecker(parSeq))