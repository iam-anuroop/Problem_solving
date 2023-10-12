# def generator(n):
#     for i in range(n):
#         yield i

# a=generator(5)
# print(list(a))


# class abcd:
#     def a():
#         x='hi'
#         return x
    
# def z():
#     y='hello'
#     return y

# b = abcd()
# b.a = z
# v=b.a
# print(v)

# # leetcode prblm one
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         a=[]
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     a.append(i)
#                     a.append(j)
#                     return a
#                     break;



# # leetcode
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         a=[i for i in s]
#         value=0
#         prev=0
#         b={x:y for x,y in zip(('I','V','X','L','C','D','M'),(1,5,10,50,100,500,1000))}
#         for i in a:
#             if prev<b[i] and prev!=0:
#                 x=b[i]-prev*2
#                 value = value+x
#             elif b[i]==1000:
#                 value+=1000
#             elif b[i]==500:
#                 value+=500
#             elif b[i]==100:
#                 value+=100
#             elif b[i]==50:
#                 value+=50
#             elif b[i]==10:
#                 value+=10
#             elif b[i]==5:
#                 value+=5
#             elif b[i]==1:
#                 value+=1
#             prev = b[i]
            
#         return abs(value)


## leetcode   
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         x = 1
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 nums[x] = nums[i]
#                 x += 1
#         return x


# # leetcode 27
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         count = 0
#         for i in range(len(nums)):
#             if nums[i]!=val:
#                 nums[count]=nums[i]
#                 count+=1
#         return count

# # leetcode 28
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         try:
#             return haystack.index(needle)
#         except:
#             return -1

# def climbStairs(n: int) -> int:
#         if n == 0 or n == 1:
#             return 1
#         prev, curr = 1, 1
#         for i in range(2, n+1):
#             temp = curr
#             curr = prev + curr
#             prev = temp
#         return curr

# print(climbStairs(4))


# node in python
# class Node:
#     def _init_(self,data):
#         self.data = data
#         self.next = None
        
# class LinkedList:
#     def _init_(self):
#         self.head = None
        
#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         n = self.head
#         while n.next:
#             n = n.next
#         n.next = new_node    
        
              
#     def print(self):
#         current = self.head
#         while current:
#             print(current.data)
#             current = current.next
            
    
#     def _len_(self):
#         count = 0
#         current = self.head
#         list1 = []
#         while current is not None:
#             current = current.next
#             count +=1
#         return count