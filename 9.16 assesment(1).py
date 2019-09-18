import random
FileHandle=open("AS_CS_opt2_gradebook.txt","w")
Name=["Daniel","Julian","Lisa","Shirley","Nico","Tim","James","Andy","Cathy","Brian","Harry","Jack"]
LastName=["Chu","Ye","Xu","Zeng","Jiang","Xing","Liu","Zhang","Yang","Shan","Fang","Jin"]
MathScore=[0,0,0,0,0,0,0,0,0,0,0,0]
CSScore=[0,0,0,0,0,0,0,0,0,0,0,0]
PhyScore=[0,0,0,0,0,0,0,0,0,0,0,0]
#print(Name, LastName, CSScore)



People=[0,1,2,3,4,5,6,7,8,9,10,11]

for n in range (1080):
    i=random.choice(People)
    while MathScore[i] == 100:
        i=random.choice(People)
    MathScore[i]+=1


for n in range (1140):
    i=random.choice(People)
    while CSScore[i] == 100:
        i=random.choice(People)
    CSScore[i]+=1
    
for n in range (1056):
    i=random.choice(People)
    while PhyScore[i] == 100:
        i=random.choice(People)
    PhyScore[i]+=1
    
#print(MathScore, CSScore, PhyScore)

#mission 1
for i in range (12):
    
    FileHandle.write(str(Name[i])+ " "+ str(LastName[i])+" "+ str(MathScore[i])+" "+str(CSScore[i])+" "+str(PhyScore[i])+"\n")
    
FileHandle.close()

#mission 2
FileHandle=open("AS_CS_opt2_gradebook.txt","r")
AllScore = FileHandle.readlines()
FileHandle.close()
FileHandle=open("AS_CS_opt2_gradebook.txt","w")
n=1
for line in AllScore:
    FileHandle.write(str(n)+" "+line)
    n+=1
FileHandle.close()

#mission 3

FileHandle=open("AS_CS_opt2_gradebook.txt","r")
AllScore = FileHandle.readlines()
FileHandle.close()
FileHandle=open("AS_CS_opt2_gradebook.txt","w")

for line in AllScore:
    
    LineLst = line.strip().split()
    Mean = 0
    for i in range(3):
        Mean = Mean + int(LineLst[i+3])
    Mean = int(Mean/3)
    
    FileHandle.write(line.replace("\n", " ")+str(Mean)+"\n")
   
FileHandle.close()

#mission 4

FileHandle=open("AS_CS_opt2_gradebook.txt","r")
AllScore = FileHandle.readlines()
FileHandle.close()
FileHandle=open("AS_CS_opt2_gradebook.txt","w")

for line in AllScore:
    aFind = line.find("Daniel")
    Out = ""
    if aFind > 0:

        LineLst = line.strip().split()
        LineLst[3]=str(int(float(LineLst[3])*1.1))
        if int(LineLst[3]) > 100:
            LineLst[3]= "100"
        for i in range(7):
            Out = Out + " " +LineLst[i]
        Out = Out.strip()+"\n"
    if aFind < 0 :

        Out = line
    
    FileHandle.write(Out)

FileHandle.close()

#mission 5

FileHandle=open("AS_CS_opt2_gradebook.txt","r")
AllScore = FileHandle.readlines()
FileHandle.close()
FileHandle=open("new_gradebook.txt","w")

PhyLow = 100

for i in range(len(AllScore)):
    
    LineLst = AllScore[i].strip().split()
    if int(LineLst[5]) < PhyLow:
        PhyLow = int(LineLst[5])
        IdLow = i

for i in range(len(AllScore)):
    if i != IdLow:
        FileHandle.write(AllScore[i])

   
FileHandle.close()
    
   

