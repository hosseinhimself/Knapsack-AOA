# Knapsack Problem Solver using Archimedes Optimization Algorithm

This repository contains a Python implementation of solving the binary knapsack problem using the Archimedes Optimization Algorithm (AOA). The AOA is a metaheuristic algorithm inspired by Archimedes’ Principle, which simulates the buoyant force exerted on an object immersed in a fluid. This principle is adapted to solve optimization problems.

## Table of Contents

1. [Introduction](#introduction)
2. [Usage](#usage)
3. [Files](#files)
4. [Libraries](#libraries)
5. [References](#references)

## Introduction

The binary knapsack problem is a classic optimization problem where a knapsack has a limited weight capacity, and a set of items with associated weights and values must be selected to maximize the total value without exceeding the knapsack's capacity. The Archimedes Optimization Algorithm is employed to tackle this problem.

For more information on the Archimedes Optimization Algorithm and its application to the knapsack problem, refer to [the article](https://link.springer.com/article/10.1007/s10489-020-01893-z/).

## Usage

To use this knapsack problem solver, you can follow these steps:

1. Install the necessary libraries (Numpy, Matplotlib).
2. Use the `knapsack.py` module to define the problem's initial conditions, such as the number, mass, and value of the objects, as well as the capacity of the knapsack.
3. Generate random solutions and calculate the cost function using the functions provided in the `knapsack.py` module.
4. Utilize the Archimedes Optimization Algorithm functions defined in `AOA.py`.
5. Customize the conditions required for the problem in the `main.py` file.

## Files

- `knapsack.py`: Defines the initial conditions of the knapsack problem and includes functions for generating random solutions and calculating the cost function for each solution.
- `AOA.py`: Contains functions related to the Archimedes Optimization Algorithm.
- `main.py`: Defines conditions required for the problem and utilizes the defined functions to solve the knapsack problem.

## Libraries

The following libraries are used in this program:
- [Numpy](https://numpy.org/): For numerical operations and array manipulations.
- [Matplotlib](https://matplotlib.org/): For generating plots and visualizations.

## References

- [Archimedes Optimization Algorithm](https://link.springer.com/article/10.1007/s10489-020-01893-z/): An article describing the Archimedes Optimization Algorithm and its application.
