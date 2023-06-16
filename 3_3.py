"""peach = 1
day = 9
while day > 0:
    peach = (peach + 1) * 2
    day -= 1
total = peach
print("total=", total)"""
def peach(time,numble):
    if time==0:
        return 1
    else:
        return (peach(time-1,numble) + 1) * 2
print(peach(9,1))