#STUDENT 340

from typing import List, Tuple
import itertools

class Node:
    def __init__(self, v, weight: int):
        self.v = v
        self.cost = float("inf")
        self.weight = weight
        self.following = []
        self.parents = PriorityQueue()

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def put(self, data):
        self.queue.append(data)
        self.size += 1
        self.merge_sort(self.queue)

    def get(self):
        if not self.empty():
            data = self.queue.pop(0)
            self.size -= 1
            return data
        else:
            print("Can't get from an empty queue")

    def empty(self):
        return self.size == 0

    def merge_sort(self, array):
        if len(array)>1:
            mid = len(array)//2
            left = array[:mid]
            right = array[mid:]

            self.merge_sort(left)
            self.merge_sort(right)
            self.merge(array, left, right)

    def merge(self, array, left, right):
        i, j, k = 0, 0, 0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i<len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j<len(right):
            array[k] = right[j]
            j += 1
            k += 1

    def print_queue(self):
        while not self.empty():
            print(self.get(), end=" ")
    

def output(stack):
    '''
    Will print the path stored in the `stack` global variable.
    You are free to modify it to be a parameter.
    '''
    for id in stack[:-1]:
        print(f'{id} ', end='')
    try:
        print(f'{stack[-1]}')
    except IndexError:
        pass
    print("\n")
    
def dijkstra(graph, source):
    seen = set()
    q = PriorityQueue()
    graph[source].cost = 0

    q.put((graph[source].cost, source))

    while q.size > 0:
        cost, node = q.get()
        seen.add(node)
        for conn in graph[node].following:
            if conn not in seen:
                d = cost + graph[conn].weight
                if d < graph[conn].cost:
                    graph[conn].cost = d
                    q.put((d,conn))
            graph[conn].parents.put((cost,node))


if __name__ == '__main__':
    
    '''
    Fetch starting and target node.
    '''
    start_id, end_id = [int(i) for i in input().split(' ')]

    data = input()
    data = data.split('; ')
    graph = {}
    for counter, d in enumerate(data):
        id, num_likes, following = d.split(', ', 2)
        following_l = following.split(', ')

        for f in following_l:
            if f == '':
                continue
            else:
                if int(id) not in graph:
                    node = Node(int(id),1/int(num_likes))
                    node.following.append(int(f))
                    graph[node.v] = node
                else:
                    graph[int(id)].following.append(int(f))

    '''
    TODO: Call the `dijkstra` function with the parameters you defined.
    '''
    dijkstra(graph,start_id)
    path = []
    while graph[end_id].cost!=0:
        path.append(end_id)
        end_id = graph[end_id].parents.get()[1]
    path.append(start_id)
    
    output(path[::-1])
