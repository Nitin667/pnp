import math
import random 
#minimax class
def minimax (currentDepth, nodeIndex, 
             maxTurn, score,  
             tarDepth): 
  
    # base case : tarDepth reached 
    if (currentDepth == tarDepth):  
        return score[nodeIndex] 
      
    if (maxTurn): 
        return max(minimax(currentDepth + 1, nodeIndex * 2,  
                    False, score, tarDepth),  
                   minimax(currentDepth + 1, nodeIndex * 2 + 1,  
                    False, score, tarDepth)) 
      
    else: 
        return min(minimax(currentDepth + 1, nodeIndex * 2,  
                     True, score, tarDepth),  
                   minimax(currentDepth + 1, nodeIndex * 2 + 1,  
                     True, score, tarDepth)) 
      
# Driver code 
score = random.sample(range(1, 50), 4)
print(str(score))  
treeDepth = math.log(len(score), 2) 
  
print("The optimal value is : ", end = "") 
print(minimax(0, 0, True, score, treeDepth)) 



# import math
# def minmax(tree,depth):
#     max_turn = bool(depth%2)
#     for i in range(int(depth)):
#         zipped = zip(tree[::2],tree[1::2])
#         print(tree[::2],tree[1::2])
#         if max_turn:
#             tree = [max(a,b) for a,b in zipped]
#         else:
#             tree = [max(a,b) for a,b in zipped]
#         max_turn = not max_turn
#     return tree[0]
# A = [3,5,2,9,12,5,23,23]
# depth = math.ceil(math.log(len(A)))
# print(A)
# print(minmax(A,depth))