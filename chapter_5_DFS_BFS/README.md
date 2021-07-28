# ch05. DFS&BFS
<br>

Search : finding data in many data
<br>

The represent of the search algorithm was **DFS & BFS**

<br>

For understanding DFS & BFS, we have to know the data structure.
- data structure mean thr structure of handling data.
<br>
Stack and queue was basic functions of data structure.

- **push** : insert data 
- **pop** : delete data
<br>

Also, there are **overflow & underflow** in data structure functions.

- **overflow** : inserting data, when the storage space was full.
- **underflow** : delete data, when the satarage space was empty

### stack : First in last out structure or last in first out structure
when we use the stack in python, we don't need to install another library. <br>

Just, use **append & pop** function in python library

### queue : like waiting line, First in Frisr out structure
when we use the queue in python, we need to using collections library in deque.
<br>

**from collections import deque**

deque is more efficient than list and more simple than queue library. 
<br>

### Recursive Function : call myself
when we use Recursive(), we have to type the end point <br>
the same as **stack**
<br>

DFS using stack structure is the good method that use recursive Function.
<br>

### DFS(Depth-First search) : search the depth part at first using the stack structure
<br>

**the step of DFS**
<br>

1. insert the start node in stack.
2. the toppest node in stack that don't visit near nodes, put the near nodes in stack and count the visit mark. if there are no visit near nodes, up to the toppest node.
3. repeat 2 untill end

### BFS(Breadth first search) : search closer node, using the queue structure

<br>

**the step of BFS**
<br>

1. insert the start node in queue
2. put out the node in queue and then, insert the closest nodes and put in the queue.
3. repeat 2 untill end

## Table of Contents
<br>
5-1.example_DFS
<br>
5-2.example_BFS
<br>
5-3.ice_eat
<br>
5-4.maze_problem