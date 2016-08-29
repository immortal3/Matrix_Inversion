""""

    Module: It's small module which take 2d-dynamic array as input and try to convert it into RREF form.
            It's follows RREF algorithms.

"""
def findRREF(list):


    for i in range(len(list)-1):
        count = i

        for x in list[i:]:
            if x[i]>0:
                break
            count = count + 1

        #STEP 2:Select non-zero entry in the pivot column as a pivot.If necessary,Interchange rows
        #       to move this entry into pivot column

        if i == 0 :
            list[i],list[count] = list[count],list[i]


        #STEP 3:Use row replacement operations to create zeros in all positions below the pivots

        #STEP  4:Cover the row containiing the pivot positions and covers all rows,if any above it.
        #       Apply step 1-3 to submatrix that remains.repeat the process until there are no more non-zeros
        #       rows to modify

        for x in list[i+1:]:
            if list[i][i] != 0:
                const = x[i] / list[i][i]
                for z in range(len(x)):
                    x[z] = x[z] - ((const)*list[i][z])




    temp = len(list) - 1


    #STEP 5:Beginning with the rightmost pivot and working upward and to left,creates zeros
    #       above each pivot.If a pivot is not 1,make it 1 by scaling operation.

    while temp>=0:
        for x in list[temp]:
            if x != 0:
                const = 1.0 / x
                for z in range(len(list[temp])):
                    list[temp][z] = const * list[temp][z]
                break
        temp = temp - 1





    temp = len(list) - 1


    while temp>=0:

        count = 0

        for x in list[temp]:
            if x==1:
                break
            count = count + 1


        if(count <= len(list[temp])  - 1):
            for x in range(temp):
                if list[x][count] is not 0:

                    const = list[x][count]

                    for z in range(len(list[x])):
                        list[x][z] = list[x][z] - (const * list[temp][z])
        temp = temp - 1



    #printing only A Inverse not whole matrix which is I|A Inverse


    print ("\n\nInverse Matrix:\n")

    for i in range(len(list)):
        for j in range(int(len(list[i])/2),len(list[i])):
            print (list[i][j],end="\t")
        print ("\n")
