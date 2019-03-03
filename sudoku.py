#libraries
import threading
import time

#global variables
result=True
grid_list=list(list(0 for i in range(9))for j in range(9))
column_list=[]
grid_thread_list=[]
#functions

def row_check(sudoku):
    global result
    for row in sudoku:
        row_set=set(row)
        if len(row_set)!=len(row):
            result=False
            
def col_check(sudoku):
    for i in range (0,9):
        inner_list=[]
        for j in range (0,9):
            inner_list.append(sudoku[j][i])
        column_list.append(inner_list)
    row_check(column_list)

def make_grid(sudoku):
    m=0
    n=0
    for i in range(0,3):
        for k in range(0,3):
            n=0
            for j in range(0,3):
                for l in range(0,3):
                    grid_list[m][n]=sudoku[3*i+j][3*k+l]
                    n+=1
            m+=1

def grid_check(grid_list):
    global result
    grid_list_set=set(grid_list)
    if len(grid_list_set)!=len(grid_list):
        result=False

#main body

sudoku=[]
print('Enter the sudoku')
for i in range(0,9):
    row=list(map(int,input().split()))
    sudoku.append(row)
make_grid(sudoku)
start=time.time()
r_thread=threading.Thread(target=row_check,args=(sudoku,))
r_thread.start()
c_thread=threading.Thread(target=col_check,args=(sudoku,))
c_thread.start()
for i in range(9):
    g_thread=threading.Thread(target=grid_check,args=(grid_list[i],))
    g_thread.start()
    grid_thread_list.append(g_thread)
r_thread.join()
c_thread.join()
for i in grid_thread_list:
    i.join()
print('\n')
print('checking sudoku using 11 threads\n')
#printing result
if result==False:
    print('This sudoku is invalid')
else:
    print('sudoku is valid')
end=time.time()
print(f'Time taken to check the sudoku is {end-start}')
print('\n')
# checking the same sudoku using same functions without multithreading
print('\nchecking the validity of sudoku using same functions without multithreading\n')
start2=time.time()
row_check(sudoku)
col_check(sudoku)
row_check(grid_list)

if result==True:
    print('sudoku is valid')
else:
    print('sudoku is Invalid')
end2=time.time()
print(f'Time taken to check the sudoku without threads is {end2-start2}')
print('\n')
#checking the sudoku using 3 threads

start3=time.time()
r_thread2=threading.Thread(target=row_check,args=(sudoku,))
r_thread2.start()
c_thread2=threading.Thread(target=col_check,args=(sudoku,))
c_thread2.start()
g_thread2=threading.Thread(target=row_check,args=(grid_list,))
g_thread2.start()
r_thread2.join()
c_thread2.join()
g_thread2.join()
print('checking sudoku using 3 threads\n')
if result==True:
    print('sudoku is valid')
else:
    print('sudoku is Invalid')
end3=time.time()
print(f'time taken to check using 3 threads is {end3-start3}')
input()

'''
#sudoku for validation
valid sudoku
6 2 4 5 3 9 1 8 7
5 1 9 7 2 8 6 3 4
8 3 7 6 1 4 2 9 5
1 4 3 8 6 5 7 2 9
9 5 8 2 4 7 3 6 1
7 6 2 3 9 1 4 5 8
3 7 1 9 5 6 8 4 2
4 9 6 1 8 2 5 7 3
2 8 5 4 7 3 9 1 6

invalid
6 2 4 5 3 9 1 8 7
5 1 9 7 2 8 6 3 4
8 3 7 6 1 4 2 9 5
1 4 3 8 6 5 7 2 9
9 5 8 2 4 7 3 6 1
7 6 2 3 9 1 4 5 8
3 7 1 9 5 6 4 4 2
4 9 6 1 8 2 5 7 3
2 8 5 4 7 3 9 1 6

invalid
6 2 4 5 3 9 1 8 7
5 1 9 7 2 8 6 3 4
8 3 7 6 1 4 2 9 5
1 4 3 8 6 5 7 2 9
9 5 8 2 4 5 3 6 1
7 6 2 2 9 1 4 5 8
3 7 1 9 5 6 8 4 2
4 9 6 1 8 2 5 7 3
2 8 5 4 7 3 9 1 6

invalid
6 2 4 5 3 9 1 8 7
5 1 9 7 2 8 6 3 4
8 3 7 6 1 4 2 9 5
1 4 3 8 6 5 7 2 9
9 5 8 2 3 7 3 6 1
7 6 2 3 9 1 4 5 8
3 7 1 9 5 6 8 4 2
4 8 6 1 8 2 5 7 3
2 8 5 4 7 3 9 1 6
'''
