#STUDENT 340

from typing import List

def stringify_path(path: List):
    '''
    Build string to print
    '''
    ret = ''
    for id in path[:-1]:
        ret = f'{ret}{id}->'
    try:
        ret = f'{ret}{path[-1]}'
    except IndexError:
        pass

    return ret

def output(paths: List[List]):
    '''
    Prints all paths from the list in param
    '''
    paths_string = []
    for p in paths:
        paths_string.append(stringify_path(p))
    print(*paths_string, sep='\n')

'''
DO NOT CHANGE ABOVE
'''

def find_paths(graph,start,end,paths):
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            if new_path[-1]==end and adjacent not in path:
                paths.append(new_path)
            if adjacent not in new_path[:-1]:
                queue.append(new_path)

if __name__ == '__main__':

    '''
    Fetch starting and target node.
    '''
    start, target = [int(x) for x in input().split('->')]

    '''
    Fetch `;` separated twitter data. <id-1: str>, <follower_1-2: str>, ..<follower_1-2: str>; ... 
    i.e: 1, 2, 3; 2, 3, 1; 3, 2
    '''
    data = input()
    data = data.split('; ')
    graph = {}
    for d in data:
        id, followers = d.split(', ', 1)
        following_l: List = followers.split(', ')

        for f in following_l:
            if f == '':
                # node is not following other nodes.
                graph[int(id)] = []
                continue
            else:
                if int(id) not in graph:
                    graph[int(id)] = [int(f)]
                else:
                    graph[int(id)].append(int(f))

    '''
    TODO: Step 3: Call your 'find_paths` function with the parameters you defined.
    '''
    paths = []
    find_paths(graph,start,target,paths)
    '''
    Print the paths.
    '''
    output(paths)
