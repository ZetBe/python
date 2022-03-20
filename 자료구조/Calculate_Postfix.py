
def compute_postfix(postfix):
    lists = postfix.split(" ")
    stack = []
    out = []
    num = float(0)
    num_1 = float(0)
    for i in lists:
        if i == '+':
            num = out.pop()
            num += out.pop()
            out.append(num)
            num = float(0)
        elif i == '-':
            num -= out.pop()
            num += out.pop()
            out.append(num)
            num = float(0)
        elif i == '*':
            num += out.pop()
            num *= out.pop()
            out.append(num)
            num = float(0)
        elif i == '/':
            num = out.pop()
            num_1 = out.pop()
            num_1 = num_1 / num
            out.append(num_1)
            num = float(0)
            num_1 = float(0)
        elif i == '^':
            num = out.pop()
            num_1 = out.pop()
            for n in range(num):
                num_1 *= num_1
            out.append(num_1)
            num = float(0)
            num_1 = float(0)
        else:
            z = float(i)
            out.append(z)
    return out.pop()

postfix = input()
value = compute_postfix(postfix)
print("{:.4f}".format(value))