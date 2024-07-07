

#task1
# def maximumCount(lst):
#     lst1 = []
#     for x in lst:
#         if x < 0:
#             a = lst.pop(x)
#             lst1.append(a)
#     print(len(lst1))
#     lst2 = []
#     for y in lst:
#         if y > 0:
#             lst2.append(y)
#     print(len(lst2))
# maximumCount([-2,-1,-1,0,0,1,2])
# maximumCount([5,20,66,1314])


#task2

# def iihf(lst):
#     lst1 = []
#     for x in range(len(lst)):
#         if lst[x] in lst:
#             lst1.append(lst[x])
#             return True
#         return False
# print(iihf([1,2,3,1]))
# print(iihf([1,2,3,4]))
