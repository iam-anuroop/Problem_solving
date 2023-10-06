# print("hellooo worlddddd")
# x=11

# for r in range(x):
    # for c in range(x):


# s="anuroop"
# for i in s:
#     print(i)

# for i in  range(3328,3450):
#     print(chr(i),"-----",i)


# n = 10
# star = []

# for i in range(1, n + 1):
#     if i == 5:
#         star.append("\n")
#     else:
#         star.append("*")

# result = ''.join(star)
# print(result)

# x= {
#     'a':'x',
#     'b':'y',
#     'c':'z'
# }
# for i in x:
#     print(i)
# for x,y in x.items():
#     print(x,"=",y)


# ma = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened = [x for i in ma for x in i ]
# print(flattened)


# rows = 3
# columns = 3
# identity_matrix = [[1 if i == j else 0 for j in range(columns)] for i in range(rows)]

# for raw in identity_matrix:
#     print(raw)


# def f(n):
#     if n==0:
#         return 1
#     else:
#         return n+f(n-1)
# print(f(5))




# class CallableClass:
#     def __init__(self, value,a):
#         self.value = value * 2
#         self.a = a

#     def abc(self):
#         return self.value+self.a

# instance = CallableClass(10,5)

# print(instance.abc())  # This will print 15





# numbers = [1, 2, 3, 4, 'hdhdh', 6, 'dndndn', 8, 'djdd']

# def is_even_or_non_empty_string(x):
#     if isinstance(x, int) and x % 2 == 0:
#         return True
#     if isinstance(x, str) and len(x) > 0:
#         return True
#     # return False
# filtered_numbers = filter(is_even_or_non_empty_string, numbers)
# filtered_numbers_list = list(filtered_numbers)
# print(filtered_numbers_list)

# import copy

# x=[10,20,30,60]
# y=copy.copy(x)
# x[0] = 100
# print(x)
# print(y)


# n = [1,2,3,4]
# def ok(n):
#     if n%2==0:
#         return n
# x=filter(ok,n)
# print(list(x))


# n = [1,2,3,4]
# y = [1,2,3,4]
# def ok(a,b):
#     return a+b
# x=map(ok,n,y)
# print(list(x))

# from functools import reduce
# n = [1,2,3,4]
# def ok(a,b):
#     print(a,b)
#     return a+b
# x=reduce(ok,n)
# print(x)



# i = [1,2,3,4]
# x=iter(i)
# print(next(x))
# print(next(x))


# i = [1,2,3,4]
# def fun(a):
#     for j in i:
#         yield j+1
# x=fun(i)
# print(next(x))
# print(list(x))
# print(x)
# for k in x:
#     print(k)



# l = [1,2,3,4]
# def dec(fun):
#     def inner(a):
#         m = 1  
#         print('sum = ',sum(a))
#         for i in a:
#             m=m*i
#         print('multiple = ', m)
#         return m
#     return inner
# @dec
# def hai(l):
#     return l
# hai(l)


# monkey patch
# class MyClass:
#     def greet(self):
#         return "Hello"
# def new_greet(self):
#     return "Hola"
# MyClass.greet = new_greet
# obj = MyClass()
# print(obj.greet())



# from itertools import combinations,permutations

# items = ['A', 'B', 'C', 'D']
# for combo in permutations(items, 4):
#     print(combo)


# a,b,*args = (1,2,3,4,5,6,7,8,9)
# print(args)

# n=10
# a,b=0,1
# for _ in range(n):
#         b = a + b
#         a = b 
#         print(b, end=" ")


# rows = 5

# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print("*", end=' ')
#     print()
# for i in range(rows, 0, -1):
#     for j in range(1, i):
#         print("*", end=' ')
#     print()




# Define the size of the butterfly pattern
# size = 5
# for i in range(1, size + 1):
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(2 * (size - i)):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     print()

# # Lower part of the butterfly
# for i in range(size, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(2 * (size - i)):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     print()


# Call the function to print the butterfly pattern


# size = 5

# # Upper part of the butterfly
# for i in range(1, size + 1):
#     print("* " * i + "  " * (2 * (size - i)) + "* " * i)

# # Lower part of the butterfly
# for i in range(size, 0, -1):
#     print("* " * i + "  " * (2 * (size - i)) + "* " * i)


# def decfun(fun):
#     def wrap(b):
#         z=fun(b)
#         print('hellooo',z)
#     return wrap

# @decfun
# def hai(n):
#     a='anuroop'+str(n)
#     return a
# hai(5)

# def loop(n):
#     for i in range(n):
#         yield i
# a = loop(5)
# for j in a:
#     print(j)

# from rest_framework.views import APIView
# from serialiser import userserialiser 
# class manage(APIView):
#     def get(self,request,pk=None):
#         if pk is not None:
#             user = 'model.objets.get(id=pk)'
#             serializer = 'userserializer(user)'
#             return Response(serializer.data,status='status')
#         users = 'model.objects.all()'
#         serializer = 'userserializer(user,many=True)'
#         return Response(serializer.data,status = 'status')
    
#     def post(self,request):
#         serilizer = 'userserializer(data = request.data)'
#         if serilizer.is_vailid():
#             serilizer.save()
#             return Response(serilizer.data,status='status')
#         return Response(serializer.error,status = 'status')

#     def patch(self,request,pk=None):
#         if pk is not None:
#             user = 'model.objects.get(pk=pk)'
#             serializer = 'userserializer(user,data=request.data,partial=True)'
#             if serializer.is_valid():
#                 return Response(serializer.data,status = 'status')
#         else:
#             return Response(serializer.error,status = 'status')
    
#     def delete(self,request,pk=None):
#         if pk is not None:
#             user = 'model.objetcs.get(id=pk)'
#             user.delete()

    

        

# n = 4
# for r in range(1,2*n):
#     for c in range(1,2*n):
#         if r+c==n+1 or abs(r-c)==abs(n-1) or abs(r+c)==abs(n*3-1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print('*',end='')
#     for k in range(2*n-2*i):
#         print('-',end='')
#     for l in range(i):
#         print('*',end='')
#     print()
# for j in range(n):
#     for k in range(n-j-1):
#         print('*',end='')
#     print()



