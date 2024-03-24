import matplotlib.pyplot as plt 
import numpy as np 
import statistics
import seaborn as sns
#reading from file and creating lists.
with open('output.txt','r') as file:
    node_ids = []
    adjacency_lists = []
    pageranks = []
    for line in file:
        parts = line.strip().split(',')
        node_id = int(parts[0])
        adjacency_list = []
        for c in parts[1]:
            if c == '[' or c == ']' or c == ';':
                continue
            adjacency_list.append(int(c))        
        pagerank = float(parts[2])
        node_ids.append(node_id)
        adjacency_lists.append(adjacency_list)
        pageranks.append(pagerank)

 # rounding off page rank values
for i in range(0,7,1):
    pageranks[i] = round(pageranks[i],3)
# Page Rank Distribution
plt.bar(node_ids, pageranks)
plt.xlabel('Nodes')
plt.ylabel('pageranks')
plt.title('pageranks Distribution')
plt.show()
# sorting the nodes by descending order.
for i in range(0,6,1):
    for j in range(i+1,7,1):
        if (pageranks[i] < pageranks[j]):
            temp1 = node_ids[i]
            temp2 = adjacency_lists[i]
            temp3 = pageranks[i]

            node_ids[i] = node_ids[j]
            adjacency_lists[i] = adjacency_lists[j]
            pageranks[i] = pageranks[j]

            node_ids[j] = temp1 
            adjacency_lists[j] = temp2 
            pageranks[j] = temp3
#calculating indegree of each nodes.
in_degree = [0,0,0,0,0,0,0]
for i in range(0,7,1):
    temp_list = adjacency_lists[i]
    for i in temp_list:
        in_degree[i-1] = in_degree[i-1] + 1

# indegree distribution
nodes = [1, 2, 3, 4, 5, 6, 7]
plt.plot(nodes, in_degree, marker='o', linestyle='-')
plt.xlabel('Nodes')
plt.ylabel('In-Degree')
plt.title('In-Degree Distribution')
plt.show()
# Descriptive statistics
mean = round(np.mean(pageranks),3)
median = round(np.median(pageranks),3)
mode   = round(statistics.mode(pageranks),3)
standard_deviation = round(np.std(pageranks),3)
variance           = round(np.var(pageranks),3)

print("descriptive statistics")
print("mean ",mean)
print("median ",median)
print("mode ",mode)
print("standard_deviation",standard_deviation)
print("variance",variance)

#Kernel density estimation of pagerank values.
sns.kdeplot(pageranks, color='blue')
plt.xlabel('Pageranks')
plt.ylabel('Density')
plt.title('Kernel Density Estimate Plot of Pageranks')
plt.show()