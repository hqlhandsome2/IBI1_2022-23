#two ribbits can produce two ribbits,four can produce four... so the total number is 2**n
# the total number should less than 100
#Because we should find out which generation exceeds 100 rabbits, we should caculate how many rabbits in each generation

#repeat
    #for total <100
    #run
    #running
    #next generation
    #if total >100
    #break, this generation exceeds 100 rabbits.



n=1
while 2**n<100:#if the number of rabbits exceeds 100
    s=2**n # the number of rabbits
    print("{} generation，has {} rabbits".format(str(n),str(s)))
    n=n+1#next generation
print("{} generation exceeds 100 rabbits".format(n))
# 1 generation，has 2 rabbits
# 2 generation，has 4 rabbits
# 3 generation，has 8 rabbits
# 4 generation，has 16 rabbits
# 5 generation，has 32 rabbits
# 6 generation，has 64 rabbits
# 7 generation exceeds 100 rabbits