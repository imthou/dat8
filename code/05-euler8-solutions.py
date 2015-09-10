#see question here: https://projecteuler.net/problem=8

#optional library for fancy code
import numpy as np

#copy and past text straight from the website
#create a list directly from cleaned string 
char_list = list("""
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
""".replace("\n",""))

#list comprehension on list, convert all string components to integer
num_list = [int(i) for i in char_list]

#set a variable to zero, it will hold and test for the greatest product as you iterate through the list
#SOLUTION 1
#FOR LOOP - steps through the list of integers
max_prod = 0
for i in range(len(num_list)-12):
    nums = num_list[i:i+13]
    temp = np.prod(nums)
    if temp > max_prod: # if-then statement to test and hold max product
        max_prod = temp
print(max_prod)

#SOLUTION 2
#FOR LOOP - Uses numpy package imported in top. 
products = [] #set to zero before the loop. append will add, not replace values in this list
for index in range(len(num_list)-12):
       prod = numpy.prod(num_list[index:index+13])
       products.append(prod)
print(max(products)) # tests for max product outside the loop

#SOLUTION 3 - A nested FOR LOOP iterates through groups of 13 
products=[]
for num in range(len(num_list)-12):
 t=1   
 for n in range(nun,num+13):
     t=t*(num_list[n])
 products.append(t)    
print(max(products))

# SOLUTION 4 -- least fanciest but it can do the JOB!  
biggest = 0
i = 1
while i < (len(num_list) - 12): #WHILE LOOP will keep going until it hits a criteria
    product = int(num_list[i]) * int(num_list[i+1]) * int(num_list[i+2]) * int(num_list[i+3]) * int(num_list[i+4]) * \
      int(num_list[i+5]) * int(num_list[i+6]) * int(num_list[i+7]) *int(num_list[i+8]) * int(num_list[i+9]) * \
      int(num_list[i+10]) * int(num_list[i+11]) * int(num_list[i+12]) 
    if product > biggest:
        biggest = product
    i += i+1 
print(biggest)


# SOLUTION 5 -- one line, using two list comprehensions
#  Finds the max of a list of products

max(np.prod([int(char_list[j]) for j in range(i,i+13)]) for i in range(len(char_list)-13))
