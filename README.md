# Romania Map Shortest Path Finder

A Python application that models the classic Romania road map as a weighted graph and provides an interactive graphical interface to calculate the shortest route between two cities. The project uses the NetworkX library for graph representation and shortest path computation, while Tkinter provides a simple desktop GUI for user interaction.

---

## Overview

This project represents the well-known Romania map used in Artificial Intelligence courses as a weighted, undirected graph. Each city is represented as a node, and each road is represented as an edge with an associated distance.

Users can select an origin and destination city through a graphical interface, and the application computes:

- The shortest route between both cities.
- The total travel distance.
- Error handling for invalid cities and impossible routes.

The shortest path is calculated using the algorithm implemented internally by the NetworkX library for weighted graphs.

---

## Features

- Representation of the Romania road map as a weighted graph.
- Graphical user interface developed with Tkinter.
- Shortest path computation between any two connected cities.
- Automatic total distance calculation.
- Validation of user input.
- Error handling for invalid cities.
- Detection when origin and destination are identical.
- Simple and intuitive interface.

---

## Technologies Used

- Python 3
- NetworkX
- Tkinter

---

## Project Structure

```
Romania-Map-Shortest-Path-Finder/
│
├── src/
│   └── romania_shortest_path.py
│
├── assets/
│   └── images/
│       ├── main_window.png
│       ├── route_example.png
│       └── invalid_city.png
│
├── LICENSE
├── .gitignore
└── README.md
```

---

## Graph Representation

The application models the Romania transportation network as an undirected weighted graph.

- Vertices represent cities.
- Edges represent roads.
- Edge weights correspond to road distances.

Example:

```
Arad ──140── Sibiu
 │
118
 │
Timisoara
```

---

## Included Cities

- Arad
- Bucharest
- Craiova
- Dobreta
- Eforie
- Fagaras
- Giurgiu
- Hirsova
- Iasi
- Lugoj
- Mehadia
- Neamt
- Oradea
- Pitesti
- Rimnicu Vilcea
- Sibiu
- Timisoara
- Urziceni
- Vaslui
- Zerind

---

## Example

Origin:

```
Arad
```

Destination:

```
Bucharest
```

Possible output:

```
Shortest route:

Arad
→ Sibiu
→ Rimnicu Vilcea
→ Pitesti
→ Bucharest

Total cost: 418
```

---

## How It Works

1. The Romania map is loaded into a NetworkX weighted graph.
2. Cities become graph nodes.
3. Roads become weighted edges.
4. The user enters the origin city.
5. The user enters the destination city.
6. NetworkX computes the shortest weighted path.
7. The application displays:
   - Complete route.
   - Total distance.

---

## Algorithm

The project uses the shortest path algorithm provided by NetworkX for weighted graphs.

For positive edge weights, NetworkX internally applies Dijkstra's shortest path algorithm.

Time Complexity:

- **O((V + E) log V)**

Where:

- **V** = number of vertices
- **E** = number of edges

---

## User Interface

The graphical interface includes:

- Origin city input.
- Destination city input.
- Search button.
- Route visualization.
- Total distance display.
- Error dialogs for invalid inputs.

---

## Error Handling

The application validates:

- Nonexistent cities.
- Origin equal to destination.
- Disconnected paths (if applicable).

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Romania-Map-Shortest-Path-Finder.git
```

Go to the project directory:

```bash
cd Romania-Map-Shortest-Path-Finder
```

Install dependencies:

```bash
pip install networkx
```

Run the application:

```bash
python src/romania_shortest_path.py
```

---

## Screenshots

### Main Window

```
assets/images/main_window.png
```

Displays the graphical interface with origin and destination input fields.

---

### Route Calculation

```
assets/images/route_example.png
```

Shows a successfully computed shortest route and its total travel cost.

---

### Invalid City

```
assets/images/invalid_city.png
```

Illustrates the validation message when the user enters a city that is not part of the Romania map.

---

## Educational Objectives

This project demonstrates:

- Graph modeling.
- Weighted graphs.
- Shortest path computation.
- Artificial Intelligence search problems.
- NetworkX graph library.
- Desktop GUI development with Tkinter.
- Event-driven programming.
- User input validation.

---

## Future Improvements

Possible extensions include:

- Interactive graph visualization.
- Displaying the explored route on the map.
- Manual implementation of Dijkstra's algorithm.
- Comparison with Breadth-First Search (BFS).
- Comparison with Depth-First Search (DFS).
- Comparison with A* Search.
- Animated route visualization.
- Dynamic loading of maps from external files.

---

## License

This project is released under the MIT License.

---

## Author

**Jose Luis Alva Salazar**

Computer Systems Engineering

GitHub Portfolio Project
