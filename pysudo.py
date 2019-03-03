import _thread
import time
#row_check
def row_check():
    for i in range(9):
        if not ''.join(sorted(row[i]))=='123456789':
            ok=False
def col_check():
    for j in range(9):
        if not ''.join(sorted([x for i in range(9) for x in row[i][j]]))=='123456789':
            ok= False
def grid_check():
    for g in range(9):
        if not ''.join(sorted([x for i in range(3) for j in range(3) for x in row[g//3*3+i][g%3*3+j]))=='123456789':
            ok= False 
row=[]
for i in range(9): row.append(input())

ok= True
if ok: print("Correct!!")
else: print("Wrong!")
