# Romania Shortest Path Finder

A Python application that models the classic **Romania Road Map** as a weighted graph and computes the shortest route between two cities through a simple graphical user interface.

The project uses the **NetworkX** library to represent the graph and calculate the minimum-cost route according to road distances, while **Tkinter** provides an intuitive desktop interface for user interaction.

---

# Features

- Weighted graph representation of the Romania road map.
- Shortest path computation between two cities.
- Automatic travel cost calculation.
- Desktop graphical interface using Tkinter.
- Validation of invalid city names.
- Validation when origin and destination are the same.
- Educational implementation of graph search on weighted graphs.
- Clean and easy-to-use interface.

---

# Technologies Used

- Python 3
- NetworkX
- Tkinter

---

# Project Structure

```
Romania-Shortest-Path-Finder/
│
├── src/
│   └── romania_shortest_path_finder.py
│
├── assets/
│   └── images/
│       ├── main_interface.jpg
│       ├── shortest_route.jpg
│       ├── second_route.jpg
│       ├── invalid_city.jpg
│       └── same_origin_destination.jpg
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# Algorithm Overview

The application models the Romania road map as an **undirected weighted graph**.

- Each city is represented as a graph node.
- Each road is represented as a weighted edge.
- The edge weight corresponds to the distance between two cities.

After the user enters an origin and a destination city, the application computes the shortest route using NetworkX's weighted shortest path algorithm and calculates the total travel distance by summing the weights of each road along the selected path.

---

# Program Workflow

1. Create an empty graph.
2. Add every city as a graph node.
3. Add every road with its corresponding distance.
4. Display the graphical interface.
5. Read the origin city.
6. Read the destination city.
7. Validate user input.
8. Compute the shortest path.
9. Calculate the total travel cost.
10. Display the resulting route.

---

# Graph Representation

The project represents the classical Romania map frequently used in Artificial Intelligence and Graph Theory courses.

Each node corresponds to a city.

Each weighted edge represents a road connecting two cities.

Example:

```
Arad ----140---- Sibiu
 |
118
 |
Timisoara
```

---

# Running the Project

Run the application with:

```bash
python romania_shortest_path_finder.py
```

A graphical interface will open where the user can enter the origin city and destination city.

---

# Example

Input

```
Origin:
Arad

Destination:
Bucharest
```

Output

```
Shortest Route

Arad
→ Sibiu
→ Rimnicu Vilcea
→ Pitesti
→ Bucharest

Total Cost:
418
```

---

# Screenshots

## 1. Main Interface

The application starts by displaying a graphical interface where the user can enter the origin and destination cities before searching for the shortest route.

![Main Interface](assets/images/main_interface.jpg)

---

## 2. Shortest Route Found

Example of a successful search showing the shortest route from **Arad** to **Bucharest**, including the total travel cost.

![Shortest Route](assets/images/shortest_route.jpg)

---

## 3. Another Route Example

A second successful search demonstrating the shortest path computation between different cities in the Romania road map.

![Second Route Example](assets/images/second_route.jpg)

---

## 4. Invalid City Validation

If the user enters a city that does not exist in the graph, the application displays an informative error message instead of attempting the search.

![Invalid City](assets/images/invalid_city.jpg)

---

## 5. Same Origin and Destination

When the origin and destination cities are identical, the application notifies the user instead of calculating an unnecessary route.

![Same Origin and Destination](assets/images/same_origin_destination.jpg)

---

# Complexity Analysis

Let:

- **V** = Number of cities
- **E** = Number of roads

The shortest path is computed using the weighted shortest path algorithm implemented internally by NetworkX.

### Time Complexity

```
O((V + E) log V)
```

### Space Complexity

```
O(V + E)
```

---

# Educational Objectives

This project demonstrates practical applications of:

- Graph Theory
- Weighted Graphs
- Shortest Path Algorithms
- Route Planning
- Path Finding
- Graph Traversal
- Artificial Intelligence Fundamentals
- Desktop GUI Development with Tkinter
- Python Programming

---

# Repository Topics

```
python
networkx
graphs
graph-theory
weighted-graph
shortest-path
pathfinding
route-planning
artificial-intelligence
search-algorithms
tkinter
desktop-application
romania-map
algorithms
computer-science
```

---

# License

This project is licensed under the MIT License.

---

# Author

**Jose Luis Alva Salazar**

Computer Engineering Student

GitHub Portfolio
