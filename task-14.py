#STUDENT 340

from typing import List

def output(stack):
    '''
    Will print the path stored in the `stack` global variable.
    You are free to modify it to be a parameter.
    '''
    for id in stack[:-1]:
        print(f'{id}->', end='')
    try:
        print(f'{stack[-1]}')
    except IndexError:
        pass


def find_path(start, end, graph):
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
if __name__ == '__main__':
    '''
    Fetch starting and target nodes.
    '''
    start, target = [int(x) for x in input().split('->')]
    
    '''
    Fetch `;` separated twitter data. <id-1: u_int>, <following: u_int>, ..<following: u_int>; ... 
    i.e: 1, 2; 2, 3; 3, 4; 4, 5; 5,
    '''
    data   = input()
    data_l: List = data.split('; ')

    graph = {}

    for d in data_l:
        id, followers = d.split(', ', 1)
        following_l: List = followers.split(', ')

        for f in following_l:
            if f == '':
                # node is not following other nodes.
                continue
            else:
                if int(id) not in graph:
                    graph[int(id)] = [int(f)]
                else:
                    graph[int(id)].append(int(f))
    '''
    TODO: Step 3: Call your 'find_path` function with the parameters you defined.
    '''
    stack = find_path(start, target, graph)
    
    '''
    TODO: Step 4: Use the `output` function to print your result to stdout.
    '''
    output(stack)
