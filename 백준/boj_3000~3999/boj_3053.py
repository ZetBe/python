#택시 기하학 백준
#3053
import math
r = int(input())
euclid, taxi = float(), float()
euclid = (r**2)*math.pi
taxi = (r**2)*2
euclid = round(euclid, 6)
taxi = round(taxi, 6)
print(format(euclid, ".6f"))
print(format(taxi, ".6f"))