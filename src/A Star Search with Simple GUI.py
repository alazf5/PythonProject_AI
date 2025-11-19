from queue import PriorityQueue
import tkinter as tk
from tkinter import ttk

heurstic = {
    "CMC": {
        "CMC": 0, "Megenagna": 125, "Gerji": 250, "Kazanchis": 385, "Hayahulet": 510,
        "Aratkilo": 510, "Bole": 360
    },
    "Megenagna": {
        "CMC": 125, "Megenagna": 0, "Gerji": 125, "Kazanchis": 260, "Hayahulet": 125,
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
        "CMC": 510, "Megenagna": 125, "Gerji": 385, "Kazanchis": 125, "Hayahulet": 0,
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
    "Megenagna": [("CMC", 125), ("Gerji", 125), ("Kazanchis", 260), ("Hayahulet", 125), ("Aratkilo", 260)],
    "Gerji": [("Megenagna", 125), ("Bole", 260)],
    "Kazanchis": [("Megenagna", 260), ("Aratkilo", 125), ("Hayahulet", 125)],
    "Hayahulet": [("Kazanchis", 125), ("Bole", 260),("Megenagna", 125)],
    "Aratkilo": [("Kazanchis", 125), ("Megenagna", 260)],
    "Bole": [("CMC", 360), ("Gerji", 260), ("Hayahulet", 260)]
}

def a_star_search(start, goal):

        open_list = PriorityQueue()
        open_list.put((heurstic[start][goal], 0, start, [start]))  # f, g, node, path

        closed_list = set()

        while not open_list.empty():
            f, gc, current, path = open_list.get()

            if current == goal:
                return path, gc  # gc = total cost
            if current in closed_list:
                continue

            closed_list.add(current)

            for neighbor, cost in graph[current]:
                new_g = gc + cost
                new_f = new_g + heurstic[neighbor][goal]
                open_list.put((new_f, new_g, neighbor, path + [neighbor]))
        return None

# GUI Using the tkinter starts from here
def run_search (start_var, goal_var, result_label):

    start_node = start_var.get()
    goal_node = goal_var.get()

    if start_node == goal_node:
        result_text = "Start and Destination are the Same: 0 Cost. "
    elif start_node in graph and goal_node in graph:
        path, cost = a_star_search(start_node, goal_node)

        if path:
            path_str = " -> " . join(path)
            result_text = f"Optimal Path (A*): {path_str}\nTotal Cost: {cost}"
        else:
            result_text = "Path not found between {start_node} and {goal_node}"
    else:
        result_text = "Error Invalid Start or Destination Location."
    result_label.config(text=result_text)

def create_gui():
    root = tk.Tk()
    root.title("A* Search for Addis Ababa")
    root.geometry("405x250")

    locations = sorted(list(graph.keys()))

    start_label = ttk.Label(root, text="Start Location:")
    start_label.grid(column=0, row=0, padx=10, pady=10, sticky="w")

    start_var = tk.StringVar(root)
    start_var.set(locations[0])

    start_dropdown = ttk.Combobox(root, textvariable=start_var, values=locations, state="readonly")
    start_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    goal_label = ttk.Label(root, text="Destination Location:")
    goal_label.grid(column=0, row=1, padx=10, pady=10, sticky="w")

    goal_var = tk.StringVar(root)
    goal_var.set(locations[1] if len(locations) > 1 else locations[0])

    goal_dropdown = ttk.Combobox(root, textvariable=goal_var, values=locations, state="readonly")
    goal_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    result_label = ttk.Label(root, text="Select Locations and click 'Find Path'")
    result_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10, sticky="w")

    search_button = ttk.Button(root, text="Find Optimal Path (A*)", command=lambda: run_search(start_var, goal_var, result_label))
    search_button.grid(row=2, column=0, padx=10, pady=10)

    root.grid_columnconfigure(1, weight=1)

    root.mainloop()

if __name__ == "__main__":
    create_gui()



















