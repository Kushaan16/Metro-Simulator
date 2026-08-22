# Delhi Metro Route and Schedule Simulator

A lightweight Python-based metro system simulator that models real-world operations, routes, schedules, and fares for the Delhi Metro network. Built entirely from scratch using C-style file handling and core data structures without external libraries.

The simulator models network topology, train schedules, and transfer dynamics across the Blue Line (Noida & Vaishali branches), Magenta Line, and Airport Express Line.

## Features

* **Real-time Train Schedule Engine:** Calculates precise next and subsequent train arrival times based on dynamic peak/off-peak frequencies.
* **Intelligent Journey Planner:** Computes complete trip itineraries across single and multi-line routes with dynamic arrival estimates[cite: 1, 2].
* **Automatic Line Interchanges:** Identifies transfer stations (e.g., Janakpuri West, Yamuna Bank, Dwarka Sector 21) and accounts for rush-hour transfer delays[cite: 1, 2].
* **Distance-Based Fare Engine:** Calculates total travel distance between any two stations and determines the exact ticket price based on official DMRC slabs[cite: 1, 2].
* **Service Bounds Enforcement:** Handles edge cases, off-hour service warnings (before 06:00 AM / after 11:00 PM), and line boundary validation[cite: 1, 2].
* **Zero External Dependencies:** Implemented purely with standard Python using structured plain-text parsing (`metro.txt`)[cite: 1, 2].

## Tech Stack

* **Python 3.x** — Core algorithm design, route graph traversal, and timing calculations
* **Built-in File I/O** — Lightweight dataset storage and line-by-line file parsing (`metro.txt`)
* **Custom Data Structures** — Nested dictionary structures (`d`) for multi-branch network representation

## Key Concepts

The project explores low-level algorithm design and simulation mechanics, including:

* **File-Based Network Storage:** Reading station orders, travel times, and inter-station distances directly from plain text files[cite: 1, 2].
* **Dynamic Time Calculations:** Converting time formats (`HH:MM`) to minute offsets for modular arithmetic and frequency calculations.
* **Peak vs Off-Peak Scheduling Logic:** Adjusting train intervals dynamically (4 mins during peak hours vs 8 mins off-peak).
* **Transfer Delay Modeling:** Factoring extra waiting times (5–10 mins) when switching between different metro lines.
* **Branching & Interchange Route Traversal:** Handling complex line splits such as the Blue Line's Noida and Vaishali branches[cite: 1, 2].

## Running the Simulator

### Prerequisites

* Python 3.x installed on your system.

### Running the Application

1. Ensure `metro_simulator.py` and `metro.txt` are in the same directory.
2. Run the main script via terminal:

bash
python metro_simulator.py
