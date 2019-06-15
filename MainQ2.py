from random import randrange
N = 6
max_width = max(2*N-1,3)
half_width = max_width//2
print(" "*half_width+"+")
def create_row(size):
    row = "*"
    #Come back to decorisation randomisation
    for i in range(size-2):
        if row[-1] == "*" and randrange(0,5)<2:
            row = row+"o"
        else:
            row = row+"*"
    row = row + "*"
    return row
for i in range(1,N):
    print(" "*(half_width-i)+create_row(1+2*i))
print(" "*half_width+"#")
if N>=12:
    print(" "*half_width+"#")
K = max(1,N//6)
base_size = int(1+2*(K))
print(" "*(half_width-K)+"="*base_size)
