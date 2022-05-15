# from collections import deque
# def isPrime(P):
#     prime = True
#     for i in range(2,P):
#         if (P%i==0):
#             prime = False
#     return prime
    
# N=input()
# A=[int (x) for x in input().split()]
# stack=deque()
# queue=deque()
# for i in range(len(A)):
#     if isPrime(A[i]):
#         queue.append(A[i])
#     else:
#         stack.appendleft(A[i])

# print("Stack:",end=" ")
# for i in range(len(stack)):
#     print(stack[i],end=" ")

# print("\nQueue:",end=" ")
# for i in range(len(queue)):
#     print(queue[i],end=" ")



from cmath import sqrt
from collections import deque

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n%f == 0:
            return False
        if n%(f+2) == 0:
            return False
        f +=6
    return True

def queue_method(A):
    q = deque()
    stk = deque()
    inLst=A
    for n in inLst:
        if is_prime(n):
            q.append(n)
        else:
            stk.append(n)
    print("Stack:",end=" ")        
    print(" ".join([str(stk.pop()) for i in range(len(stk))]))
    print("Queue:",end=" ")
    print(" ".join([str(q.popleft()) for i in range(len(q))]))
n=input()
A=[int (x) for x in input().split()]
queue_method(A)
# N=input()
# A=[int (x) for x in input().split()]   
# n = max(A)
# prime = [True for i in range(n+1)] 
# p = 2
# while (p * p <= n):  
#     if (prime[p] == True): 
#         for i in range(p * p, n+1, p): 
#             prime[i] = False
#     p += 1

# queu, stack = [], []
# for i in A:
#     if prime[i]:
#         queu.append(i)
#     else:
#         stack.append(i)
# print("Stack:",end=" ") 
# for i in stack[::-1]:
#     print(i, end = " ")
# print("\nQueue:",end=" ")
# for i in queu:
#     print(i, end = " ")
# print()


    

           
        
