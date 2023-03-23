# n is the order of figure
#for each n, we can caluclate the number of plots by formula 2n(2n-1)/2 and print it
#n is from 1 to 5, so we ues "while" to calculate each one
#

n=1
# use the while-loop to calculate first five plots
while n<6:# first five
    # use formula to calculate 
    h = 2 * n * (2 * n - 1) / 2
    n=n+1 # next figure

    print(h)
#first: 1.0 second: 6.0 third:15.0 forth:28.0 fifth: 45.0





