from itertools import permutations
import nltk
string=input("Enter the  required string\n")
permut=[]
two_letter=[]
thr_letter=[]
fr_letter=[]
five_letter=[]
six_letter=[]
sev_letter=[]
all_words = set(nltk.corpus.words.words())
for i in range(2,len(string)+1):
    for p in permutations(string,r=i):
        t="".join(p)
        permut.append(t)
set(permut)
print("Output:")
for i in permut:
    if i in all_words:
        if(len(i)==2):
            two_letter.append(i)
        elif(len(i)==3):
            thr_letter.append(i)
        elif(len(i)==4):
            fr_letter.append(i)
        elif(len(i)==5):
            five_letter.append(i)
        elif(len(i)==6):
            six_letter.append(i)
        elif(len(i)==7):
            sev_letter.append(i)
print("Two Letter Words :")
for i in set(two_letter):
    print(i,end=' ')
print("\nThree Letter Words :")
for i in set(thr_letter):
    print(i,end=' ')
print("\nFour Letter Words :")
for i in set(fr_letter):
    print(i,end=' ')
print("\nFive Letter Words :")
for i in set(five_letter):
    print(i,end=' ')
print("\nSix Letter Words :")
for i in set(six_letter):
    print(i,end=' ')
print("\nSeven Letter Words :")
for i in set(sev_letter):
    print(i,end=' ')
