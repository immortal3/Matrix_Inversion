"""

	Module : this module takes 2d-dynamic matrix(specially n*n) as input and return it's Determinant

"""
def finddeterminant(list):

    length_of_list = len(list)
    if (length_of_list > 2):
        i = 1
        j = 0
        sum = 0

        while j<=length_of_list-1:

            d = {}
            temp = 1

            while temp <= length_of_list-1:
                k = 0
                d[temp] = []

                while k <= length_of_list-1:
                    if (k == j):
                        u=0
                    else:
                        d[temp].append(list[temp][k])
                    k = k + 1
                temp = temp + 1

            submatrix = [ d[x] for x in d ]
			#recurssion
            sum = sum + i*(list[0][j])*(finddeterminant(submatrix))
            i = i * (-1)
            j = j + 1

        return sum
	# for 2*2 matrix
    else:
        return ( list[0][0]*list[1][1]-list[0][1]*list[1][0] )
