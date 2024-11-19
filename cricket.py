import random 

t1 = dict()
t2 = dict()
w1=0
w2=0
tt1=0
tt2=0

b = 0
pre=0
run = 0

print("TEAM - 1")
print("____________")
for i in range(11):
    play = "Player "+str(i+1)

    while(True):
        r = random.randint(0,7)
        if r == pre:
            b=b+1
            w1 = w1+1
            break
        b = b+1
        run = run + r  
        pre = r  
    #print(run)
    t1[play]= run,b
    tt1 = tt1 + run
    run = 0
    b=0
for i in t1:
    print(i , end="\t")
    print(t1[i][0], "\t", t1[i][1], "\t", round(((t1[i][0]/t1[i][1])*100 ),2))
print()
print("Total Score of Team ", tt1,"/",w1)
print("======================================")
print("TEAM - 2")
print("____________")
########################################################################
for i in range(11):
    play = "Player "+str(i+1)

    while(True):
        r = random.randint(0,7)
        if r == pre:
            b=b+1
            w2 = w2+1
            break
        b = b+1
        run = run + r  
        pre = r  
    #print(run)
    t2[play]= run,b
    tt2 = tt2 + run
    if(tt2>tt1):
        break
    run = 0
    b=0
for i in t2:
    print(i , end="\t")
    print(t2[i][0], "\t", t2[i][1], "\t", round(((t2[i][0]/t2[i][1])*100),2) )
print()

print("Total Score of Team ", tt2,"/",w2)
print()
print("Team 1 Win", tt1-tt2) if(tt1>tt2) else print("Team 2 Win", tt2-tt1)