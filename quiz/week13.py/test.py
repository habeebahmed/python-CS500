# initializing list
input = [10,20,30,40,50,60]
  
# printing input list
print("The input list is : " + str(input))
res = [sum(sub) for sub in zip(input, input[1:])]  

arr_new = [input[idx]+input[idx+1] if idx+1 < len(input) else input[idx] for idx, i in enumerate(input) if idx%2 == 0]
  
#Printing result 
print("The list after initializing the sum of two adjacent numbers : " + str(arr_new))