#Depth First Search

graph={

'0':['1','2'],

'1':['3','4'],

'2':['5','6'],

'5':[],

'6':[],

'3':[],'4':[]

}

visited=[]

queue=[]

def dfs(visited,graph,node):

        visited.append(node)

        queue.append(node)

        while queue:

                m = queue.pop(0)

                print(m, end=" ")

                for val in graph[m]:

                        if (val[0]):

                                dfs(visited,graph,val[0])

print("Path After DFS Traversal")

dfs(visited,graph,'0')