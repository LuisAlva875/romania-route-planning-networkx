import networkx as nx
import tkinter as tk
from tkinter import messagebox

# Crear un grafo vacío
G = nx.Graph()

# Agregar nodos (ciudades)
cities = [
    "Oradea", "Zerind", "Arad", "Timisoara", "Lugoj", "Mehadia", 
    "Dobreta", "Craiova", "Rimnicu Vilcea", "Sibiu", "Fagaras", 
    "Pitesti", "Bucharest", "Giurgiu", "Urziceni", "Hirsova", 
    "Vaslui", "Iasi", "Neamt", "Eforie"
]
G.add_nodes_from(cities)

# Agregar bordes (conexiones) con los costos
connections = [
    ("Oradea", "Sibiu", 151), ("Oradea", "Zerind", 71),
    ("Zerind", "Arad", 75),
    ("Arad", "Sibiu", 140), ("Arad", "Timisoara", 118),
    ("Timisoara", "Lugoj", 111),
    ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Dobreta", 75),
    ("Dobreta", "Craiova", 120),
    ("Craiova", "Rimnicu Vilcea", 146),
    ("Rimnicu Vilcea", "Sibiu", 80),
    ("Craiova", "Pitesti", 138),
    ("Rimnicu Vilcea", "Pitesti", 97),
    ("Sibiu", "Fagaras", 99),
    ("Fagaras", "Bucharest", 211),
    ("Bucharest", "Pitesti", 101),
    ("Bucharest", "Giurgiu", 90),
    ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Hirsova", 98),
    ("Urziceni", "Vaslui", 142),
    ("Vaslui", "Iasi", 92),
    ("Iasi", "Neamt", 87),
    ("Hirsova", "Eforie", 86)
]
G.add_weighted_edges_from(connections)

def shortest_path(start, end):
    return nx.shortest_path(G, start, end, weight='weight')

def find_shortest_path():
    start_city = start_entry.get().strip().capitalize()
    end_city = end_entry.get().strip().capitalize()

    if start_city not in cities or end_city not in cities:
        messagebox.showerror("Error", "Ciudad no encontrada en el mapa.")
        return

    if start_city == end_city:
        messagebox.showinfo("Información", "La ciudad de origen y destino son iguales.")
        return

    try:
        path = shortest_path(start_city, end_city)
        total_cost = sum(G[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))
        result_label.config(text=f"Ruta más corta: {' -> '.join(path)}\nCosto total: {total_cost}")
    except nx.NetworkXNoPath:
        messagebox.showerror("Error", f"No hay ruta posible de {start_city} a {end_city}.")

# Interfaz gráfica
root = tk.Tk()
root.title("Mapa de Rumania")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

start_label = tk.Label(frame, text="Ciudad de origen:")
start_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

start_entry = tk.Entry(frame)
start_entry.grid(row=0, column=1, padx=5, pady=5)

end_label = tk.Label(frame, text="Ciudad de destino:")
end_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

end_entry = tk.Entry(frame)
end_entry.grid(row=1, column=1, padx=5, pady=5)

find_button = tk.Button(frame, text="Buscar ruta", command=find_shortest_path)
find_button.grid(row=2, columnspan=2, padx=5, pady=5)

result_label = tk.Label(frame, text="")
result_label.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop()