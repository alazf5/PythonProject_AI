# This is an Implementation of The A* Search FUnction
from queue import PriorityQueue

# Heuristics Table
heurstic = {
    "CMC": {
        "CMC": 0, "Megenagna": 125, "Gerji": 250, "Kazanchis": 385, "Hayahulet": 510,
        "Aratkilo": 510, "Bole": 360
    },
    "Megenagna": {
        "CMC": 125, "Megenagna": 0, "Gerji": 125, "Kazanchis": 260, "Hayahulet": 385,
        "Aratkilo": 385, "Bole": 385
    },
    "Gerji": {
        "CMC": 250, "Megenagna": 125, "Gerji": 0, "Kazanchis": 385, "Hayahulet": 385,
        "Aratkilo": 510, "Bole": 260
    },
    "Kazanchis": {
        "CMC": 385, "Megenagna": 260, "Gerji": 385, "Kazanchis": 0, "Hayahulet": 125,
        "Aratkilo": 125, "Bole": 385
    },
    "Hayahulet": {
        "CMC": 510, "Megenagna": 385, "Gerji": 385, "Kazanchis": 125, "Hayahulet": 0,
        "Aratkilo": 250, "Bole": 260
    },
    "Aratkilo": {
        "CMC": 510, "Megenagna": 385, "Gerji": 510, "Kazanchis": 125, "Hayahulet": 250,
        "Aratkilo": 0, "Bole": 510
    },
    "Bole": {
        "CMC": 360, "Megenagna": 385, "Gerji": 260, "Kazanchis": 385, "Hayahulet": 260,
        "Aratkilo": 510, "Bole": 0
    }
}

# Adjacency List
graph = {
    "CMC": [("Megenagna", 125), ("Bole", 360)],
    "Megenagna": [("CMC", 125), ("Gerji", 125), ("Kazanchis", 260)],
    "Gerji": [("Megenagna", 125), ("Kazanchis", 385), ("Bole", 260)],
    "Kazanchis": [("Megenagna", 260), ("Gerji", 385), ("Hayahulet", 125), ("Aratkilo", 125)],
    "Hayahulet": [("Kazanchis", 125), ("Aratkilo", 250), ("Bole", 260)],
    "Aratkilo": [("Kazanchis", 125), ("Hayahulet", 250), ("Bole", 510)],
    "Bole": [("CMC", 360), ("Gerji", 260), ("Hayahulet", 260), ("Aratkilo", 510)]
}


# A Star Search algorithm f(n) = g(n) + h (n, goal)
def a_star_search (start, goal):

     open_list = PriorityQueue()
     open_list.put((heurstic[start][goal], 0, start, [start])) # f, g, node, path

     closed_list = set()

     while not open_list.empty():
         f, gc, current, path = open_list.get()

         if current  == goal:
                return path, gc    # gc = total cost
         if current in closed_list:
             continue

         closed_list.add(current)

         for neighbor, cost in graph[current]:
             new_g = gc + cost
             new_f = new_g + heurstic[neighbor][goal]
             open_list.put((new_f, new_g, neighbor, path + [neighbor]))
     return None


# User Input s = start, g = goal
s = input("Enter Starting Location: ")
g = input("Enter Destination: ")

# p = path, c = cost
p, c = a_star_search(s, g)
print ("Optimal Path: ", " -> ".join(p))
print ("Total Cost: ", c)