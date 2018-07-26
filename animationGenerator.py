# print ("hello world")
# import sys
# print(sys.version)

# columns = [0,2,4,6,8,10,12,14,16,18,20,22,24,25,27,29,31,33,35,37,39,41,43,45,47,49,50,52,54,56,58,60,62,64,66,68,70,72,74,75,77,79,81,83,85,87,89,91,93,95,97,]

for x in range(0, 125):
    print('P[c:{0}] (0,255,0), '.format(x%125), end='') # Green
    print('P[c:{0}] (255,255,0), '.format((x+25)%125), end='') # Yellow
    print('P[c:{0}] (255,255,255), '.format((x+50)%125), end='') # White
    print('P[c:{0}] (127,0,255), '.format((x+75)%125), end='') # Purple
    print('P[c:{0}] (0,0,255)'.format((x+100)%125), end='') # Blue
    print(';')