import random

f = open('occupations.csv', 'r')
s=f.read()
f.close()
s=s.split("\n")
s=s[1:len(s)-3]
d={}
for occupation in s:
    occupation=occupation.split(',')
    if occupation[0][0:1]== '"':#checks for commas
        while len(occupation)>2:#makes a list with occupation name and percent
            occupation[0]=occupation[0]+','+occupation[1]
            occupation.pop(1)
    d[occupation[0]]=float(occupation[1])

def pickRandom():
    listOfJobs=d.keys()
    weightedList=[]
    for jobs in listOfJobs:
        weightedList.extend([jobs]*int((d[jobs]*10)))#adds in jobs based on percent of population
    return random.choice(weightedList)

print pickRandom()
