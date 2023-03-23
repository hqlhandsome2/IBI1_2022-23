#
a = -3.19
b = -118.24
c = 116.39
# use d as the distance between a and b
d = abs(a-b)
# use e as the distance between a and c
e = abs(a-c)
# use if to judge which distance is greater
if d > e:
    print( 'Rob travel further to Los Angeles')#Los Angeles is further than Haining
# if d=<e, compare them again
elif d<e: print ('Rob travel further to Haining')#Haining is further than Los Angeles
else: print("same distance")
#Haining is further

X=True
Y=False
W=X and Y
Z=X or Y
print(W,Z)
#W is false and Z is True

