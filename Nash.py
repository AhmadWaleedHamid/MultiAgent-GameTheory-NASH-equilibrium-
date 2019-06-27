#!/usr/bin/env python
# coding: utf-8

# In[7]:


from random import randrange, uniform
import numpy as np
from array import *
import random


# In[8]:


def Random_Mode(Mode, nRows, nCols):
    Boundary_String = "------------------------------------"
    #Printing the format
    print(Boundary_String)
    print("Player: Player1's strategies ")
    print(Boundary_String)
    #End= makes sure that print does not change line
    print("{", end='')
    iterator=1
    while (iterator <= nRows):
        print("A" + str(iterator), end='')
        if iterator!=nRows:
            print( ", ",end='')    
        iterator +=1
    print("}")

    print('\n')
    print(Boundary_String)
    print("Player: Player1's payoffs")
    print(Boundary_String)

    Player1Utilities = []

    #Initializing the Utilities
    for i in range (0,nRows):
        Player1Utilities.append([])
        for j in range( 0, nCols):
            Player1Utilities[i].append(j)
            Player1Utilities[i][j] = random.randint(-99,+99)


    #Printing the Utitlities
    for i in range (0,nRows):  
        for j in range( 0, nCols):     
            print( "  "+ format(Player1Utilities[i][j], '^3d'), end='')
            if j!=nCols-1:
                print(',',end='')
                
        print('\n')

    print(Boundary_String)
    print("Player: Player2's strategies ")
    print(Boundary_String)
    #End= makes sure that print does not change line
    print("{", end='')
    iterator=1
    while (iterator <= nCols):
        print("B" + str(iterator) , end='')
        if iterator!=nCols:
            print( ", ",end='') 
        iterator +=1
    print("}")
    print('\n')
    print(Boundary_String)
    print("Player: Player2's payoffs")
    print(Boundary_String)
    Player2Utilities = []

    #Initializing the pay offs for the second player
    for i in range (0,nRows):
        Player2Utilities.append([])
        for j in range( 0, nCols):
            Player2Utilities[i].append(j)
            Player2Utilities[i][j] = random.randint(-99,+99)


    #Printing the pay offs for the second player
    for i in range (0,nRows):  
        for j in range( 0, nCols):     
            print( "  "+ format(Player2Utilities[i][j], '^3d')  , end='')
            if j!=nCols-1:
                print(',',end='')
        print('\n')

    print('\n')
    DisplayNormFormBoundary = "======================================="
    DisplayNormTitle = "Display Normal Form"

    print(DisplayNormFormBoundary)
    print(DisplayNormTitle)
    print(DisplayNormFormBoundary)

    
    DisplayNormBoundaryLineArray=["-----------------","------------------------------","-------------------------------------------","--------------------------------------------------------","---------------------------------------------------------------------","----------------------------------------------------------------------------------","-----------------------------------------------------------------------------------------------","------------------------------------------------------------------------------------------------------------","-------------------------------------------------------------------------------------------------------------------------"]
    DisplayLine = "|"

    
    iterator = 1
    print("         ", end= '')

    for i in range (0, nCols):
            
            print( "B" + str(iterator) +  "           " , end='')
            iterator += 1
    
    print('\n')
    print(DisplayNormBoundaryLineArray[nCols-1])

    i=0
    j=0
    for i in range (0, nRows):
        print("A" + str(i+1) + " " + DisplayLine , end='')
        for j in range ( 0, nCols):
            print( " " + "(" + format(Player1Utilities[i][j], '^3d') + "," + format(Player2Utilities[i][j],'^3d') + ")" , end = '' + "  " + DisplayLine )
                
        print('\n')
        print(DisplayNormBoundaryLineArray[nCols-1])
        
    print ('\n')
    print(DisplayNormFormBoundary)
    print("Nash Pure Equilibrium Locations")
    print(DisplayNormFormBoundary + "")
    DisplayLine = "|"
    
    #Printing the NASH table
    
    #AGENT 1:
    maximum=0
    nashlist=[] 
    r=0
    c=0
    for i in range(0,nCols):
        list1=[row[i] for row in Player1Utilities]
        maximum = max(list1)
        nashlist.append(maximum)
        for j in range(0,nRows):
            if(Player1Utilities[j][i]==maximum):
                Player1Utilities[j][i]='H'

        
    #Agent2
    list2=[]
    nashlist2=[]
    maximum2=0
    for i in range(0,nRows):
        del list2[:]
        for j in range(0,nCols):
            list2.append(Player2Utilities[i][j])             
        maximum = max(list2)
        nashlist2.append(maximum)
        for k in range(0,nCols):    
            if(Player2Utilities[i][k]==maximum):
                Player2Utilities[i][k]='H'


    #+=========================================================================#

    count=0
    iterator = 1
    print("         ", end= '')

    for i in range (0, nCols):
            
            print( "B" + str(iterator) +  "           " , end='')
            iterator += 1
    
    print('\n')
    print( DisplayNormBoundaryLineArray[nCols-1])

    i=0
    j=0
    for i in range (0, nRows):
        print("A" + str(i+1) + " " + DisplayLine , end='')
        for j in range ( 0, nCols):
            print( " (%3s,%3s)  %s" %(str(Player1Utilities[i][j]),str(Player2Utilities[i][j]),str(DisplayLine)),end='' )   
        print('\n')
        print( DisplayNormBoundaryLineArray[nCols-1])
        

   
    
    print('\n')
    print( DisplayNormBoundaryLineArray[nCols-1])
    
    #print("         ", end= '')
    print ("Nash Pure Equilibrium(s): ",end='')
    
    i=0
    j=0
    nashfound=False
    for i in range(0,nRows):
        for j in range(0,nCols):
            if(Player1Utilities[i][j]=='H' and Player2Utilities[i][j]=='H'):
                print ("("+"A"+str(i+1)+","+"B"+str(j+1)+")",end=' ') 
                nashfound=True
                print("  ")
    
    if(nashfound==False):
        if(nRows == 2 and nCols == 2):
            print ('\n')
            print ("------------------------------------------")
            print ("Player 1 & 2 Indifferent Mix Probabilities")
            print ("------------------------------------------")
            Player1Utilities=BackSubstituteValues1(Player1Utilities,nashlist,nRows,nCols)
            Player2Utilities=BackSubstituteValues2(Player2Utilities,nashlist2,nRows,nCols)
            IndifferenceProb(Player1Utilities,Player2Utilities,nRows,nCols)
        else:
            print ("Player 1 & 2 Have Different Sizes and No Pure Nash Equilibrium Exists")
            
    elif(nashfound==True):
        print ("------------------------------------------")
        print ("Player 1 & 2 Indifferent Mix Probabilities")
        print ("------------------------------------------")
        print ("Normal Form has Pure Strategy Equilibrium")
            
            
            
    
    print(DisplayNormBoundaryLineArray[nCols-1])
    Player1Utilities=BackSubstituteValues1(Player1Utilities,nashlist,nRows,nCols)
    Player2Utilities=BackSubstituteValues2(Player2Utilities,nashlist2,nRows,nCols)
    CalculatePayoffIndivisual(Player1Utilities,Player2Utilities,nRows,nCols)
    CalculateMixPayoff(Player1Utilities,Player2Utilities,nRows,nCols)
    

#=======================================================================================================#
# Substituting Back the Values
#=======================================================================================================#

def BackSubstituteValues1(PlayerUtilities,Nashlist,rows,cols):
    count=0
    for i in range(0,cols):
        for j in range(0,rows):
            if(PlayerUtilities[j][i]=='H'):
                PlayerUtilities[j][i]=Nashlist[count]
                count+=1
    return PlayerUtilities
    
def BackSubstituteValues2(PlayerUtilities,Nashlist,rows,cols):
    count=0
    for i in range(0,nRows):
        for j in range(0,nCols):
            if(PlayerUtilities[i][j]=='H'):
                PlayerUtilities[i][j]=Nashlist[count]
                count+=1
    return PlayerUtilities

#=======================================================================================================#
# def CalculateMIXPayoff(Agent1,Agent2,row,col) Starts
#=======================================================================================================#
def CalculateMixPayoff(Agent1,Agent2,row,col):
    i=0
    j=0
    DisplayNormFormBoundary = "======================================="
    iterator=1
    bestPayoff=-100
    bestprob2=[]
    bestProb=[]
    #Agent1 PayOff
    for a in range(0,row):
        payoffAgent1=0
        bestiter=0

         
        ProbAgent1 = GetProb(row)
        ProbAgent2 = GetProb(col)
        
        for i in range (0,row):
            for j in range (0,col):
                payoffAgent1+=(Agent1[i][j]*ProbAgent1[0][i]*ProbAgent2[0][j])
        if(payoffAgent1>bestPayoff):
            bestPayoff=payoffAgent1
            bestProb=ProbAgent1
            bestprob2=ProbAgent2
            bestiter=iterator
        iterator+=1
    print('\n')
    
    print("----------------------------------------------------")
    print("Player 1 & Player 2 Playoffs with both player Mixing")
    print("----------------------------------------------------")
    
    print ("Player 1-> "+"A"+str(bestiter)+"(",np.around(bestProb,2),")","("+str(np.around(bestProb,2))+")"+" = "+str(np.around(bestPayoff,2))) 
    
    #Agent2 PayOff
    iterator=1
    bestPayoff=-100
    bestProb=[]
    for a in range(0,row):
        payoffAgent2=0
        bestiter=0
        
        ProbAgent1 = GetProb(row)
        ProbAgent2 = GetProb(col)       
                
        for i in range (0,col):
            for j in range (0,row):
                payoffAgent2+=(Agent2[j][i]*ProbAgent1[0][j]*ProbAgent2[0][i])
        if(payoffAgent2>bestPayoff):
            bestPayoff=payoffAgent2
            bestProb=ProbAgent2
            bestiter=iterator
        iterator+=1
        
    print ("Player 2-> "+"B"+str(bestiter)+"(",np.around(bestProb,2),")","("+str(np.around(bestProb,2))+")"+" = "+str(np.around(bestPayoff,2)))
    
    print (DisplayNormFormBoundary)

    
#=======================================================================================================#
# def CalculateMixPayoff(Agent1,Agent2,row,col) Ends
#=======================================================================================================#

def CalculatePayoffIndivisual(Agent1,Agent2,row,col):
    DisplayNormFormBoundary = "======================================="
    iterator=1
    bestPayoff=-100
    bestProb=[]
    print("----------------------------------------------")
    print("Player 1 Expected Payoffs with Player 2 Mixing")
    print("----------------------------------------------") 
    #Agent1 PayOff
    for a in range(0,row):
        payoffAgent1=0
        bestiter=1
        
        ProbAgent1 = GetProb(row)
        ProbAgent2 = GetProb(col)
             
        for i in range (0,row):
            for j in range (0,col):
                payoffAgent1+=(Agent1[i][j]*ProbAgent1[0][i])
        print ("U(A"+str(iterator)+","+"("+str(np.around(ProbAgent1,2))+")"+" = "+str(np.around(payoffAgent1,2)))
        if(payoffAgent1>bestPayoff):
            bestPayoff=payoffAgent1
            bestProb=ProbAgent1
            bestiter=iterator
        iterator+=1
    print ('\n')
    print ("-------------------------------------------")
    print ("Player 1 Best Response with Player 2 Mixing")
    print ("-------------------------------------------")
    print ("BR("+str(np.around(bestProb,2))+" = "+"{"+"A"+str(np.around(bestiter,2))+"}")
    print ('\n')
    print ('\n')

    #Agent2 PayOff
    iterator=1
    bestPayoff=-100
    bestProb=[]
    print("----------------------------------------------")
    print("Player 2 Expected Payoffs with Player 1 Mixing")
    print("----------------------------------------------") 
    for a in range(0,row):
        payoffAgent2=0
        bestiter=1
        ProbAgent1 = GetProb(row)
        ProbAgent2 = GetProb(col)
                
        for i in range (0,col):
            for j in range (0,row):
                payoffAgent2+=(Agent2[j][i]*ProbAgent2[0][i])
        print ("U(B"+str(iterator)+","+"("+str(np.around(ProbAgent2,2))+")"+" = "+str(np.around(payoffAgent2,2)))
        if(payoffAgent2>bestPayoff):
            bestPayoff=payoffAgent2
            bestProb=ProbAgent2
            bestiter=iterator
        iterator+=1
    print ('\n')
    print ("-------------------------------------------")
    print ("Player 2 Best Response with Player 1 Mixing")
    print ("-------------------------------------------")
    print ("BR("+str(np.around(bestProb,2))+" = "+"{"+"B"+str(np.around(bestiter,2))+"}")
    
    print( DisplayNormFormBoundary)
    
#=======================================================================================================#
# def CalculatePayoffIndivisual(Agent1,Agent2,row,col) Ends
#=======================================================================================================#

#=======================================================================================================#
# def IndifferenceProb(Agent1,Agent2,row,col)
#=======================================================================================================#

def IndifferenceProb(Agent1,Agent2,nRows,nCols):
    ProbAgent1 = GetProb(nRows)
    ProbAgent2 = GetProb(nCols)
    payoffAgent1=0
    payoffAgent2=0
    #Agent1
    iterator=1
    #Agent1 PayOff
    for i in range (0,nRows):
        for j in range (0,nCols):
            payoffAgent1+=(Agent1[i][j]*ProbAgent1[0][i]*ProbAgent2[0][j])
        print("Player 1 Probability of strategies A("+str(iterator)+")"+" = "+str(np.around(payoffAgent1,2)))
        iterator+=1

    #Agent2
    iterator=1
    #Agent2 PayOff
    for i in range (0,nCols):
        for j in range (0,nRows):
            payoffAgent2+=(Agent2[j][i]*ProbAgent1[0][j]*ProbAgent2[0][i])
        print("Player 2 Probability of strategies B("+str(iterator)+")"+" = "+str(np.around(payoffAgent2,2)))
        iterator+=1
    print('\n')

#=======================================================================================================#
# def IndifferenceProb(Agent1,Agent2,row,col) Ends
#=======================================================================================================#


# In[9]:


def GetProb(nRows):
    ProbAgent1 = np.random.dirichlet(np.ones(nRows),1)
    ProbAgent1=np.around(ProbAgent1,2)
    rows = ProbAgent1.shape[0]
    cols = ProbAgent1.shape[1]
    ProbAgent1 = ProbAgent1.tolist()
    for i in range(rows):
        for j in range(cols):
            if(ProbAgent1[i][j]<0.01):
                ProbAgent1[i][j]=round(ProbAgent1[i][j],1)
    return ProbAgent1


# In[10]:


def Manual_Mode(Mode, nRows, nCols):
    Player1Utilities = []
    number=0
    #Initializing the Utilities
    for i in range (0,nRows):
        Player1Utilities.append([])
        for j in range( 0, nCols):
            Player1Utilities[i].append(j)
            number=int(input("Enter the value at A["+str(i)+"]"+"["+str(j)+"] ="))
            while(number>=99 or number <=-99):
                number=int(input("Enter the value at A["+str(i)+"]"+"["+str(j)+"]"+"Ranging from -99 to 99 = "))
            Player1Utilities[i][j]=number

    Boundary_String = "------------------------------------"
    #Printing the format
    print(Boundary_String)
    print("Player: Player1's strategies ")
    print(Boundary_String)
    #End= makes sure that print does not change line
    print("{", end='')
    iterator=1
    while (iterator <= nRows):
        print("A" + str(iterator) , end='')
        if iterator!=nRows:
            print( ", ",end='') 
        iterator +=1
    print("}")

    print('\n')
    print(Boundary_String)
    print("Player: Player1's payoffs")
    print(Boundary_String)

   
    #Printing the Utitlities
    for i in range (0,nRows):  
        for j in range( 0, nCols):   
            print( "  "+ format(Player1Utilities[i][j], '^3d') , end='')
            if j!=nCols-1:
                print(',',end='')
        print('\n')


    Player2Utilities = []

    #Initializing the pay offs for the second player
    Player2Utilities = []
    number1=0
    #Initializing the Utilities
    for i in range (0,nRows):
        Player2Utilities.append([])
        for j in range( 0, nCols):
            Player2Utilities[i].append(j)
            number1=int(input("Enter the value at B["+str(i)+"]"+"["+str(j)+"] ="))
            while(number1>=99 or number1 <=-99):
                number1=int(input("Enter the value at B["+str(i)+"]"+"["+str(j)+"]"+"Ranging from -99 to 99: "))
            Player2Utilities[i][j]=number1

    #====Print Player 2 Strategy====#        
    print(Boundary_String)
    print("Player: Player2's strategies ")
    print(Boundary_String)
    #End= makes sure that print does not change line
    print("{", end='')
    iterator=1
    while (iterator <= nCols):
        print("B" + str(iterator) , end='')
        if iterator!=nCols:
            print( ", ",end='') 
        iterator +=1
    print("}")
    print('\n')

    #Printing the pay offs for the second player
    print(Boundary_String)
    print("Player: Player2's payoffs")
    print(Boundary_String)
    for i in range (0,nRows):  
        for j in range( 0, nCols):     
            print( "  "+ format(Player2Utilities[i][j], '^3d') , end='')
            if j!=nCols-1:
                print(',',end='')
        print('\n')


    DisplayNormFormBoundary = "======================================="
    DisplayNormTitle = "Display Normal Form"

    print(DisplayNormFormBoundary)
    print(DisplayNormTitle)
    print(DisplayNormFormBoundary)

    
    DisplayNormBoundaryLineArray=["-----------------","------------------------------","-------------------------------------------","--------------------------------------------------------","---------------------------------------------------------------------","----------------------------------------------------------------------------------","-----------------------------------------------------------------------------------------------","------------------------------------------------------------------------------------------------------------","-------------------------------------------------------------------------------------------------------------------------"]
    DisplayLine = "|"

    
    iterator = 1
    print("         ", end= '')

    for i in range (0, nCols):
            
            print( "B" + str(iterator) +  "           " , end='')
            iterator += 1
    
    print('\n')
    print("   " + DisplayNormBoundaryLineArray[nCols-1])

    i=0
    j=0
    for i in range (0, nRows):
        print("A" + str(i+1) + " " + DisplayLine , end='')
        for j in range ( 0, nCols):
            print( " " + "(" + format(Player1Utilities[i][j], '^3d') + "," + format(Player2Utilities[i][j],'^3d') + ")" , end = '' + "  " + DisplayLine )
                
        print('\n')
        print( DisplayNormBoundaryLineArray[nCols-1])


    print(DisplayNormFormBoundary)
    print("Nash Pure Equilibrium Locations")
    print(DisplayNormFormBoundary + "\n")


    DisplayLine = "|"
###=================================================================================================###
    #AGENT 1:
    maximum=0
    nashlist=[] 
    r=0
    c=0
    for i in range(0,nCols):
        list1=[row[i] for row in Player1Utilities]
        maximum = max(list1)
        nashlist.append(maximum)
        for j in range(0,nRows):
            if(Player1Utilities[j][i]==maximum):
                Player1Utilities[j][i]='H'

        
    #Agent2
    list2=[]
    nashlist2=[]
    maximum2=0
    for i in range(0,nRows):
        del list2[:]
        for j in range(0,nCols):
            list2.append(Player2Utilities[i][j])             
        maximum = max(list2)
        nashlist2.append(maximum)
        for k in range(0,nCols):    
            if(Player2Utilities[i][k]==maximum):
                Player2Utilities[i][k]='H'


    #+=========================================================================#
        count=0
    iterator = 1
    print("         ", end= '')

    for i in range (0, nCols):
            
            print( "B" + str(iterator) +  "           " , end='')
            iterator += 1
    
    print('\n')
    print( DisplayNormBoundaryLineArray[nCols-1])

    i=0
    j=0
    for i in range (0, nRows):
        print("A" + str(i+1) + " " + DisplayLine , end='')
        for j in range ( 0, nCols):
            print( " (%3s,%3s)  %s" %(str(Player1Utilities[i][j]),str(Player2Utilities[i][j]),str(DisplayLine)),end='' )   
        print('\n')
        print( DisplayNormBoundaryLineArray[nCols-1])
        

   
    
    print('\n')
    print( DisplayNormBoundaryLineArray[nCols-1])
    #==========================================================================#


    print(DisplayNormFormBoundary)
   
    print (" Nash Pure Equilibrium(s): ",end='')
    i=0
    j=0
    nashfound=False
    for i in range(0,nRows):
        for j in range(0,nCols):
            if(Player1Utilities[i][j]=='H' and Player2Utilities[i][j]=='H'):
                print ("(","A",i+1,",","B",j+1,")",end=' ')
                nashfound=True
    if(nashfound==False):
        if(nRows == 2 and nCols == 2):
            print ('\n')
            print ("------------------------------------------")
            print ("Player 1 & 2 Indifferent Mix Probabilities")
            print ("------------------------------------------")
            Player1Utilities=BackSubstituteValues1(Player1Utilities,nashlist,nRows,nCols)
            Player2Utilities=BackSubstituteValues2(Player2Utilities,nashlist2,nRows,nCols)
            IndifferenceProb(Player1Utilities,Player2Utilities,nRows,nCols)
        else:
            print ("Player 1 & 2 Have Different Sizes and No Pure Nash Equilibrium Exists")
            
    elif(nashfound==True):
        print ('\n')
        print ("------------------------------------------")
        print ("Player 1 & 2 Indifferent Mix Probabilities")
        print ("------------------------------------------")
        print ("Normal Form has Pure Strategy Equilibrium")
            
            
            
    
    print(DisplayNormBoundaryLineArray[nCols-1])
    Player1Utilities=BackSubstituteValues1(Player1Utilities,nashlist,nRows,nCols)
    Player2Utilities=BackSubstituteValues2(Player2Utilities,nashlist2,nRows,nCols)
    CalculatePayoffIndivisual(Player1Utilities,Player2Utilities,nRows,nCols)
    CalculateMixPayoff(Player1Utilities,Player2Utilities,nRows,nCols)
    

#=======================================================================================================#
# Substituting Back the Values
#=======================================================================================================#

def BackSubstituteValues1(PlayerUtilities,Nashlist,rows,cols):
    count=0
    for i in range(0,cols):
        for j in range(0,rows):
            if(PlayerUtilities[j][i]=='H'):
                PlayerUtilities[j][i]=Nashlist[count]
                count+=1
    return PlayerUtilities
    
def BackSubstituteValues2(PlayerUtilities,Nashlist,rows,cols):
    count=0
    for i in range(0,nRows):
        for j in range(0,nCols):
            if(PlayerUtilities[i][j]=='H'):
                PlayerUtilities[i][j]=Nashlist[count]
                count+=1
    return PlayerUtilities

#=======================================================================================================#
# def CalculateMIXPayoff(Agent1,Agent2,row,col) Starts
#=======================================================================================================#
def CalculateMixPayoff(Agent1,Agent2,row,col):
    i=0
    j=0
    DisplayNormFormBoundary = "======================================="
    iterator=1
    bestPayoff=-100
    bestprob2=[]
    bestProb=[]
    #Agent1 PayOff
    for a in range(0,row):
        payoffAgent1=0
        bestiter=0

         
        ProbAgent1 = GetProb(row)
        ProbAgent2 = GetProb(col)
        
        for i in range (0,row):
            for j in range (0,col):
                payoffAgent1+=(Agent1[i][j]*ProbAgent1[0][i]*ProbAgent2[0][j])
        if(payoffAgent1>bestPayoff):
            bestPayoff=payoffAgent1
            bestProb=ProbAgent1
            bestprob2=ProbAgent2
            bestiter=iterator
        iterator+=1
    print('\n')
    
    print("----------------------------------------------------")
    print("Player 1 & Player 2 Playoffs with both player Mixing")
    print("----------------------------------------------------")
    
    print ("Player 1-> "+"A"+str(bestiter)+"(",np.around(bestProb,2),")","("+str(np.around(bestProb,2))+")"+" = "+str(np.around(bestPayoff,2))) 
    
    #Agent2 PayOff
    iterator=1
    bestPayoff=-100
    bestProb=[]
    for a in range(0,row):
        payoffAgent2=0
        bestiter=0
        
        ProbAgent1 = GetProb(row)
        ProbAgent2 = GetProb(col)       
                
        for i in range (0,col):
            for j in range (0,row):
                payoffAgent2+=(Agent2[j][i]*ProbAgent1[0][j]*ProbAgent2[0][i])
        if(payoffAgent2>bestPayoff):
            bestPayoff=payoffAgent2
            bestProb=ProbAgent2
            bestiter=iterator
        iterator+=1
        
    print ("Player 2-> "+"B"+str(bestiter)+"(",np.around(bestProb,2),")","("+str(np.around(bestProb,2))+")"+" = "+str(np.around(bestPayoff,2)))
    
    print (DisplayNormFormBoundary)

    
#=======================================================================================================#
# def CalculateMixPayoff(Agent1,Agent2,row,col) Ends
#=======================================================================================================#

def CalculatePayoffIndivisual(Agent1,Agent2,row,col):
    DisplayNormFormBoundary = "======================================="
    iterator=1
    bestPayoff=-100
    bestProb=[]
    print("----------------------------------------------")
    print("Player 1 Expected Payoffs with Player 2 Mixing")
    print("----------------------------------------------") 
    #Agent1 PayOff
    for a in range(0,row):
        payoffAgent1=0
        bestiter=1
        
        ProbAgent1 = GetProb(row)
        ProbAgent2 = GetProb(col)
             
        for i in range (0,row):
            for j in range (0,col):
                payoffAgent1+=(Agent1[i][j]*ProbAgent1[0][i])
        print ("U(A"+str(iterator)+","+"("+str(np.around(ProbAgent1,2))+")"+" = "+str(np.around(payoffAgent1,2)))
        if(payoffAgent1>bestPayoff):
            bestPayoff=payoffAgent1
            bestProb=ProbAgent1
            bestiter=iterator
        iterator+=1
    print ('\n')
    print ("-------------------------------------------")
    print ("Player 1 Best Response with Player 2 Mixing")
    print ("-------------------------------------------")
    print ("BR("+str(np.around(bestProb,2))+" = "+"{"+"A"+str(np.around(bestiter,2))+"}")
    print ('\n')
    print ('\n')

    #Agent2 PayOff
    iterator=1
    bestPayoff=-100
    bestProb=[]
    print("----------------------------------------------")
    print("Player 2 Expected Payoffs with Player 1 Mixing")
    print("----------------------------------------------") 
    for a in range(0,row):
        payoffAgent2=0
        bestiter=1
        ProbAgent1 = GetProb(row)
        ProbAgent2 = GetProb(col)
                
        for i in range (0,col):
            for j in range (0,row):
                payoffAgent2+=(Agent2[j][i]*ProbAgent2[0][i])
        print ("U(B"+str(iterator)+","+"("+str(np.around(ProbAgent2,2))+")"+" = "+str(np.around(payoffAgent2,2)))
        if(payoffAgent2>bestPayoff):
            bestPayoff=payoffAgent2
            bestProb=ProbAgent2
            bestiter=iterator
        iterator+=1
    print ('\n')
    print ("-------------------------------------------")
    print ("Player 2 Best Response with Player 1 Mixing")
    print ("-------------------------------------------")
    print ("BR("+str(np.around(bestProb,2))+" = "+"{"+"B"+str(np.around(bestiter,2))+"}")
    
    print( DisplayNormFormBoundary)
    
#=======================================================================================================#
# def CalculatePayoffIndivisual(Agent1,Agent2,row,col) Ends
#=======================================================================================================#

#=======================================================================================================#
# def IndifferenceProb(Agent1,Agent2,row,col)
#=======================================================================================================#

def IndifferenceProb(Agent1,Agent2,nRows,nCols):
    ProbAgent1 = GetProb(nRows)
    ProbAgent2 = GetProb(nCols)
    payoffAgent1=0
    payoffAgent2=0
    #Agent1
    iterator=1
    #Agent1 PayOff
    for i in range (0,nRows):
        for j in range (0,nCols):
            payoffAgent1+=(Agent1[i][j]*ProbAgent1[0][i]*ProbAgent2[0][j])
        print("Player 1 Probability of strategies A("+str(iterator)+")"+" = "+str(np.around(payoffAgent1,2)))
        iterator+=1

    #Agent2
    iterator=1
    #Agent2 PayOff
    for i in range (0,nCols):
        for j in range (0,nRows):
            payoffAgent2+=(Agent2[j][i]*ProbAgent1[0][j]*ProbAgent2[0][i])
        print("Player 2 Probability of strategies B("+str(iterator)+")"+" = "+str(np.around(payoffAgent2,2)))
        iterator+=1
    print('\n')

#=======================================================================================================#
# def IndifferenceProb(Agent1,Agent2,row,col) Ends
#=======================================================================================================#


# In[11]:


#Taking input for the mode
Mode = input("Enter (R)andom or (M)anual payoff entires : ")

#Taking as input the number of rows and columns
nRows=int(input("Enter the number of rows : "))
nCols=int(input("Enter the number of cols : "))

if(Mode == 'M' or Mode == 'm'):
    Manual_Mode(Mode,nRows,nCols)
elif(Mode == 'R' or Mode == 'r'):
    Random_Mode(Mode,nRows,nCols)
else:
    print("Wrong Values Entered! Please select Between M or R")


# #### 
