#Write a program to find Factorial of given no using  iterative #and recursive algorithm.
#Iterative Approach
def fib_iter(n):
  a=1
  b=1
  if n==1:
   print('0')
  elif n==2:
   print('0','1')
  else:
   print("Iterative Approach: ")
   print('0',a,b)
   for i in range(n-3):
    total = a + b
    b=a
    a= total
    print(total)
  
    return b
fib_iter(5)


#Recursive Approach
def fib_rec(n):
  if n == 1:
   return [0]
  elif n == 2:
   return [0,1]
  else:
   x = fib_rec(n-1)
# the new element the sum of the last two elements
   x.append(sum(x[:-3:-1]))
   return x
x=fib_rec(5)
print("Recursive Approach: ")
print(x)

#Dynamic Programming Approach
#There is a slight modification to the iterative approach. We use an additional array.
def fib_dp(num):
 arr = [0,1]
 print("Dynamic Programming Approach: ")
 if num==1:
  print('0')
 elif num==2:
  print('[0,','1]')
 else:
  while(len(arr)<num):
   arr.append(0)
  if(num==0 or num==1):
    return 1
  else:
    arr[0]=0
    arr[1]=1
    for i in range(2,num):
     arr[i]=arr[i-1]+arr[i-2]
    print(arr)
    return arr[num-2]
fib_dp(5)
