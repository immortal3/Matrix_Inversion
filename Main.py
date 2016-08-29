"""

    Program : program gets input of dynamic matrix from user and first it checks for matrix is invertible or not.
              If matrix is invertible and then it try's to find inverse with RREF algorithms


    Name : Patel Dipkumar p.
    Roll No. : 201501070

    for LA_Code_Submission_1


    Warning : In some cases,when Value of Matrix gets very very small....it creates overflow and inverse of matrix
            will not get correct.btw,It's not error of algorithms!!!!

"""

import RREF as rref
import Determinant as DM

print ("Enter a row of matrix(row = column):")
row = input(">>>")
col = row



list = []

for x in range(int(row)):
    list.append([])
    for y in range(2*int(col)):
        list[x].append(0)


print ('\n\n')

for x in range(int(row)):
    for y in range(int(col)):
        print ("Row %d Col %d"%(x+1,y+1))
        temp = input(">>>")
        list[x][y] = float(temp)

for x in range(int(row)):
    list[x][x+int(row)] = 1



print ("\n\nGiven Matrix:\n")
for i in range(len(list)):
    for j in range(0,int(len(list[i])/2)):
        print (list[i][j],end="\t")
    print ("\n")

print ("\n\n")

inverseflag = DM.finddeterminant(list)
if(inverseflag != 0):
    rref.findRREF(list)
else:
    print ("Inverse of Given Matrix is not possible!!")
