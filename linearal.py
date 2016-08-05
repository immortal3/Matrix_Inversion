list = [[4.0,7.0,3.0,5.0],[2.0,8.0,9.0,4.0],[3.0,2.0,7.0,8.0]]
#list = [[1.0,1.0,1.0,3.0],[2.0,2.0,2.0,6.0],[3.0,3.0,3.0,9.0]]
#list = [[1.0,0.0,1.0,6.0],[0.0,-3.0,1.0,7.0],[2.0,1.0,3.0,15.0]]



for x in range(len(list)):
     if x < len(list) -1:     
          const = (list[x+1][x+1] - 1) / list[x][x+1]
          for y in range(0,len(list[x])):
               list[x+1][y] = list[x+1][y] - (const)*(list[x][y])
     else:
          
          const =(list[x-len(list) + 1][x-len(list) + 1 ] - 1) / list[x][x-len(list) + 1]
          for y in range(len(list[x])):
               list[x - len(list) + 1][y] =  list[x - len(list) + 1][y] - (const)*(list[x][y])      

#print (list)



for x in range(len(list)-1):
     for y in range(x+1,len(list)):
          #print (y)
          if y < len(list):          
               const =(list[y][x] / list[x][x])
               for z in range(len(list[y])-1):
                    list[y][z] = list[y][z] - (const)*(list[x][z])




for x in range(1,len(list)):
     const = 1.0 / list[x][x]
     for z in range(len(list[x])):
         list[x][z] = list[x][z] * const



x = 2
while x > 0:
     y = x - 1
     while y >= 0: 
          const = list[y][x]
          for z in range(len(list[x])):
               list[y][z] = list[y][z] - const * list[x][z]
          y = y - 1
     x = x - 1

print (list)
