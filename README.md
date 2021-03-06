# Grid-Cell Search Problem
<p>This repo contains a solver for the grid-cell search problem written in Python 3.8.2.</p>
<hr />

<h2>The Problem</h2>

<p>Given a 2d-array (H x W in dimension) filled with numbers find the number of cells within n steps of a cell containing a positive number moving in only cardinal directions. Each in-range cell should be counted toward the total only once.</p>

<p>The following assumptions are made about the problem.</p>

<ol>
<li> H > 0
<li> W > 0
<li> N >= 0
<li> The location of the positive values is initially unknown.
<li> Coordinates are given in the format (Y, X) aka (row, column).
</ol>

<h2>The Solver</h2>
<p>The solver is implemented as the class Neighborhood inside of Neighborhood.py. The constructor takes four parameters: n, h, w, and filled_cells. The first three parameters have identical definitions to their problem statement counterparts. The fourth (filled_cells) is a list of coordinates to be filled with a positive value. This parameter is not used by the search algorithm. The list is only used to initialize the problem and display the solution.</p>
<p>Once an instance of the class has been initialized it can be solved using the solve() function, this function will return the number of cells in the neighborhood of positive values. The solution can then be displayed with show(). As a demo the following code:</p>

```
n = Neighborhood(filled_cells=[(5, 5)])
n.solve()
n.show()
```
<p>Will show the following solution:</p>
<img src="./Figure_1.png">
<p>Note the first three parameters default to two, eleven and eleven respectively.</p>

