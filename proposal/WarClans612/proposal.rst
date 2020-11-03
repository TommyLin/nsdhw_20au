===========================
Proposal for [Sparse Graph Library]
===========================

Basic information
=================

`The GitHub repository <https://github.com/WarClans612/Sparse-Graph-Library>`__

In computer science, graph is usually used as mathematical representations of real world data.
For instance, communication network, transporation network, data organization, website link can be
represented using graph.

Problem to solve
================

Industry Problem
-----------------

In this modern world, abundant amount of data could be collected from every action made. Therefore,
the size requirements for graph has also been increasing. This creates problem for storing the graph
in memory. For small enough graph, it is usually stored as flattened grid which is efficient in its
I/O usage with sacrifice of storage size.

Manipulating graph usually means dealing with matrix computation which is quite expensive to do.
Therefore, there is a demand to improve efficiency in dealing with this kind of graph data. Many real
world problems do not consists of dense matrix due to its nature.

Example for this usage is for linguistics research. Since natural language often lends itself well
of discrete structures. We can decompose semantics into tree-based structures or hierarchical graph.
Another way to represents syntax for natural language can be modeled with directed acyclic graphs. The
advantage of using graph is added by the fact that visualization if the tasks could help better understanding
for the topic. Currently, mathematics for natural language related tasks has been used especially in
artificial intelligence research, such as WordNet, VerbNet, TextGraphs, and etc.

Math Behind the Problem
-----------------

Matrix calculation is the core math problem for graph manipulation. In this library, we would like
extend support for matrix calculation especially for sparse matrix.

There is 2 main methods to store sparse matrix, which is CSC (Compressed Sparse Column) and CSR 
(Compressed Sparse Row). These 2 methods are quite similar except that values in CSC are read first by
column, a row index is stored for each value, and column pointers are stored, while values in CSR are
read first by row, a column index is stored for each value, and row pointers are stored. 

Numerical Method to be Applied
-----------------

The main idea is to store sparse matrix using 2 supported method (CSC and CSR), and providing
library that is able to do calculation with those 2 storage method. The graph class will then
inherit from the matrix class to be used as further extension. However, in this project, we will
focus more of feature implementation for the matrix rather than the graph.

Perspective users
=================

- Research focus operation related to sparse matrix
- Data analytic team that operates with huge nodes in graph
- Company with huge amount of graph relation data collection that would like to decrease its storage usage

System architecture
===================

Input:

- Graph can be initialized as an empty graph
- Provided method to add nodes into the graph
- Provided method to add edges into the graph

Output:

- Provided method to store the matrix into a text file
- Provided method to manipulate the matrix

Modularization
-----------------

- SparseMatrix Class
    - SparseMatrix Manipulation
    - Storage
    - Computation
- Graph Class (inherit from Matrix Class):
    - Graph Manipulation
    - Storage (similar to matrix, graph can be represented as matrix)
- Testing Module
- Config Module
- Example Module

API description
===============

- SparseMatrix Class
    - ``SparseMatrix()``
    - ``SparseMatrix(vector&)``
    - ``SparseMatrix(vector<vector>&)``
    - ``SparseMatrix(SparseMatrix&)``
    - ``void loadSparseMatrix(string)``
    - ``void saveSparseMatrix(string)``
    - ``void resetSparseMatrix()``
    - 
    - ``const float&  operator()(int, int)``
    - ``void          operator()(int, int, float)``
    - ``SparseMatrix& operator=(const SparseMatrix&)``
    - ``SparseMatrix  operator+(const SparseMatrix&)``
    - ``SparseMatrix  operator-(const SparseMatrix&)``
    - ``SparseMatrix  operator*(const float&)``
    - ``SparseMatrix  operator*(const SparseMatrix&)``
    - ``SparseMatrix  operator*(const SparseMatrix&)``
    - ``SparseMatrix  operator/(const SparseMatrix&)``
    - 
    - ``addNode(int, float)``
    - ``removeNode(int)``
    - ``addEdge(int, float)``
    - ``removeEdge(int)``
    - 
    - ``findIndex(float)``
    - ``int dim(float)``

- Graph Class (currently Wrapper for SparseMatrix Class)

Engineering infrastructure
==========================

SparseMatrix class will be implemented first with Graph Class inheriting its module.
Initialization, loading, and saving module will be the most critical parts at the beggining.
The above modules will enable us to verify the correctness of CSC and CSR implementation
by comparing it with python Scipy Package (used as testing purposes).

The next part is implementing its computation operator, which also will be verified with
Scipy Package.

PyBind11 will be used to glue C++ module and Python called to be tested.
Pytest will then be used to implement unittest capability.
Git will be used to track and maintain version.

Schedule
========

- 11/02 - 11/08 -> Implementing SparseMatrix module shell
- 11/09 - 11/15 -> Implementing PyBind11 integration for continuous testing
- 11/16 - 11/29 -> Implementing CSC and CSR
- 11/30 - 12/13 -> Implementing Testing Module
- 12/14 - 12/20 -> Last test

Squashing Bug and Refactoring done in each step.

References
==========

- `Sparse Matrix Wikipedia <https://en.wikipedia.org/wiki/Sparse_matrix#Compressed_sparse_column_(CSC_or_CCS)>`__
- `Graph Theory Wikipedia <https://en.wikipedia.org/wiki/Graph_theory#Computer_science>`__
- `Sparse Matrix Calculation <http://www.mathcs.emory.edu/~cheung/Courses/561/Syllabus/3-C/sparse.html>`__
- `Sparse Matrix Scipy <https://docs.scipy.org/doc/scipy/reference/sparse.html>`__
