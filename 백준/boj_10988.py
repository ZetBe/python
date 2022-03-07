#10988 팰린드롬인지 확인하기
word = input()
word = list(word)
wrong = 0
for i in range(len(word)):
    if word[i] != word[len(word)-i-1]:
        wrong = 1

if wrong == 1:
    print(0)
else:
    print(1)