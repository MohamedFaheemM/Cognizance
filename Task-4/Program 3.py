list1 = [ ] 
n = int(input("Enter number of elements : ")) 
  
for x in range(0, n): 
    ele = [input('Enter the name:'),input('Enter the branch:'),int(input('Enter the year joined:'))] 
    list1.append(ele) 
      
print(list1)
print("Name",'\t','Branch','\t','Year Joined')
for x in list1:
    print(x[0],'\t',x[1],'\t\t ',x[2])

print('')

for x in range(len(list1)):
    if x==1:
        print(list1[x][0],'\t',list1[x][1],'\t',list1[x][2])
   
        

