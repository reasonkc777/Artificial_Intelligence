class Node:
    def __init__(self, city, parent=None):
        self.city = city
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

def a_star_search(graph, start_city, goal_city):
    open_list = []
    closed_list = []

    start_node = Node(start_city)
    start_node.g = 0
    start_node.h = graph[start_city]
    start_node.f = start_node.g + start_node.h

    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda node: node.f)

        if current_node.city == goal_city:
            path = []
            while current_node:
                path.insert(0, current_node.city)
                current_node = current_node.parent
            return path

        open_list.remove(current_node)
        closed_list.append(current_node)

        for neighbor_city in graph[current_node.city]:
            neighbor_node = Node(neighbor_city, parent=current_node)
            neighbor_node.g = current_node.g + graph[current_node.city][neighbor_city]
            neighbor_node.h = graph[neighbor_city]
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            if neighbor_node in closed_list:
                continue

            if neighbor_node in open_list:
                open_node = open_list[open_list.index(neighbor_node)]
                if neighbor_node.g < open_node.g:
                    open_list.remove(open_node)
                    open_list.append(neighbor_node)
            else:
                open_list.append(neighbor_node)

    return None


graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Bucharest': 0,
    'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': 161,
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Giurgiu': 77,
    'Hirsova': {'Eforie': 86, 'Urziceni': 98},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Neamt': 234,
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Urziceni': {'Hirsova': 98, 'Vaslui': 142, 'Bucharest': 85},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Zerind': {'Arad': 75, 'Oradea': 71}
}

start_city = 'Arad'
goal_city = 'Bucharest'

path = a_star_search(graph, start_city, goal_city)
if path:
    print(f"Optimal Path from {start_city} to {goal_city}: {' -> '.join(path)}")
else:
    print("Path not found.")
