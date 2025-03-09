my_list = [1,22,3,4,5,6,7,8,9,10] #range(0,11(!)) OR range(11)
print(list(enumerate(my_list)))

#result3 = {k:i for i in enumerate(my_list)}

result1 = []
for i in my_list:
    result1.append(i**2)

result2 = [i**2 for i in my_list]

for i in range(5):
    for j in range(5):
        for k in range(8):
            print(i,j,k)


#i=0
#while i < len(my_list):
    #result.append(my_list[i]**2)
    #i += 1

#for i in my_list:
    #if i ==5:
        #continue
    #else:
        #result.append(i)
    #print(f"value {i}")



#print(result1)