### Genetic algo to reach a target string from nothing
import random
import math
def fitness(population):##appends a fitness score at the end of ach chromosome
    megafitness=0
    global target 
    for i in population:
        if len(i) is not n:
            continue
        
        fitness=0
        #print(i,target)
        for j,k in zip(i,target):
            if j!=k:
                fitness+=1
                megafitness+=1
        i.append(fitness)
    print(megafitness,'meeegggafiitness')
    return population   
def mate(cr1,cr2):
    #print(cr1,cr2)
    global valid
    cr3=[]
    #print(' P',p)
    for i in range(n):
        p=random.random()
        if p<0.90:
            cr3.append(random.choice([cr1[i],cr2[i]])) #crossingover
        else:
            cr3.append(random.choice(valid)) ##mutation
    return cr3        
            
valid='''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''            
n=int(input('enter the length of the string'))
t=input('enter target string')
target=[x for x in t]
number=100
population=[[random.choice(valid) for z in range(n)] for i in range(number)] 
        #population initialization complete
population =fitness(population) #returns a fitness score and sort population 
population=sorted(population,key=lambda x:x[-1])
gen=1
for p in range(100):#population[1][-1] =!0: ##certatin value:
    if population[0][:-1]==target:
        print('reached in gen-',gen-1)
        break
    print('''new popopopopop''',gen)
    newpop=population[0:math.floor(0.1*number)]##copy best 10% popu
   ## print(population,'pop')
    #print(newpop,'newpop')
    
    for i in range(math.floor(0.1*number),number-math.floor(0.1*number)):##cross  till 90% the best 50%
        newpop.append(mate(random.choice(population[:math.floor(0.4*number)]),random.choice(population[:math.floor(0.4*number)])))
    newpop=fitness(newpop)
    #print(newpop,'newpop b4 sort')
    newpop=sorted(newpop,key=lambda x:x[-1])    
    print(newpop,'newpopafter sort')
    gen+=1
    population=newpop

    
