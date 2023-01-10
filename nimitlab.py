# from nirmalmamlab1 import get_neighb


def h(n):
    h_distance={'a':11,'b':9,'c':3,'d':5,'e':12}
    return h_distance[n]

g_node ={'a':[('b',9),('c',5),('e',12)],
        'b':[('a',9),('d',4)],
        'c':[('a',5),('d',4)],
        'd':[('b',4),('c',3),('e',5)],
        }
        
def astar(start_n,stop_n):
    opn_set=set(start_n)
    cls_set=set()

    g={}
    p_node={}
    g[start_n]=0
    p_node[start_n]=start_n

    while len(opn_set)>0:
        n=None
        for v in opn_set:
            if n==None or g[v]+h(v) < g[n]+h(n):
                n=v

        if n==stop_n or g_node[n]== None:
            pass
        else:
            for(m,weight) in get_neighb(n):



                if m not in opn_set and m not in cls_set:
                    opn_set.add(m)

                    p_node[m] =n

                    g[m]=g[n]+weight
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n] + weight
                        p_node[m]=n
                        if m in cls_set:
                            cls_set.remove(m)
                            opn_set.add(m)

        if n==None:
            print("path does not exist")
            return None
        if n==stop_n:
            path=[]
            while p_node[n]!=n:
                path.append(n)
                n=p_node[n]
            path.append(start_n)
            print("path found")
            path.reverse()
            print(path)
            return path
        opn_set.remove(n)
        cls_set.add(n)
    print("path does not exist")
    return None
def get_neighb(v):
    if v in g_node:
        return g_node[v]
    else:
        return None
astar('a','d')










#  The code is a function that calculates the distance between two nodes.
#  The code starts by creating an empty list called h_distance, which is used to store distances between nodes.
#  It then creates a dictionary called g_node, which stores information about each node in the graph.
#  The function astar takes two arguments: start and stop.
#  It iterates through all of the nodes in its argument and sets them as keys in their respective lists (opn_set and cls_set).
#  Then it iterates through all of the values in those lists until it finds one with a smaller value than what's stored for n (the current node) or if there are no more values left to compare against, then it stops looping.
#  The code is to calculate the shortest distance between two nodes in a graph.
#  The code starts by declaring an empty list called h_distance and then declares a function called h which takes no arguments and returns the value of the list.
#  The function is used to create a dictionary that maps each node to its distance from another node.
#  Next, a for loop iterates over all nodes in the graph and calculates their distances from other nodes using the get_neighb method on nirmalmamlab1 .
#  Finally, it creates an empty set called cls_set , sets up a dictionary with keys being names of classes and values being sets of all nodes in those classes, creates an empty set called g that will hold information about what has


















#  The code starts by creating a list of nodes, called g. The first node in the list is assigned the value 0, and all other nodes are set to their corresponding values based on their position in the list.
#  Next, the code loops through each item in the opn_set variable.
#  If n is not None (which means that n is not an empty string), then it checks to see if g[n] + h(n) equals g[n] + h(n).
#  If it does not, then n is added to the end of p_node and the loop continues.
#  The final part of this code sets up a couple variables: astar starts out with start_n as its input and stops at stop_n; opn_set holds all of the input data for astar; and cls_set stores a list of classes that will be used during training (in this case, only one class--neighbors).
#  Finally, g and p_node are initialized to empty lists.
#  The code first creates an empty list, called g, and sets the value of each element in the list to 0.
#  Next, it loops through all of the items in opn_set and compares the current item's value to that of g[n], which is set to 0.
#  If the current item's value is greater than or equal to g[n] then n is assigned the value of v and the loop terminates.
#  Otherwise, the loop continues by comparing v to g[n+1], which will be 1 if v is less than g[n+1] but not equal to it, or 2 if v is exactly equal to g[n+1].
#  This process repeats until n becomes None or all items in opn
