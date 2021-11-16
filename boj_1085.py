#직사각형에서 탈출 백준
#1085
x, y, w, h = map(int, input().split())

if x >= w-x:
    wide = w-x
else:
    wide = x

if y >= h-y:
    height = h-y

else:
    height = y

if wide >= height:
    short = height
else:
    short = wide

print(short)
