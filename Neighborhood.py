from matplotlib import pyplot as plt


class Neighborhood():
    def __init__(self, n=2, h=11, w=11, filled_cells=[]) -> None:
        """ Class to construct, solve, and visualize problem.

        Args:
            n (int, optional): Max steps to take from a positive number. Defaults to 2.
            h (int, optional): Number of rows. Defaults to 11.
            w (int, optional): Number of columns. Defaults to 11.
            filled_cells (list[tuple], optional): Cells to fill with positive numbers. Defaults to [].
        """
        self.n = n
        self.h = h
        self.w = w

        # Construct 2d array filling cells with 1 if
        # they were designated as positive in filled_cells.
        self.neighborhood = [
            [1 if (r, c) in filled_cells else 0 for c in range(w)] for r in range(h)]

        # Uniquely stores cells in range of positive values.
        self.in_range = set()

        # This is only used in show() to help with visualization.
        self.filled = filled_cells

    def __repr__(self) -> str:
        return('\n'.join(['  '.join([str(cell) for cell in row]) for row in self.neighborhood]))

    def manhattan(self, x1, y1, x2, y2):
        """Heuristic for bfs_search. 

        Args:
            x1 (int): x1 value.
            y1 (int): y2 value.
            x2 (int): x2 value.
            y2 (int): y2 value.

        Returns:
            int: Manhattan distance between two coordinates.
        """
        return abs(x1-x2) + abs(y1-y2)

    def bfs_search(self, r, c):
        """Conducts a breadth-first search on self.neighborhood. 
        For values 0 to n steps from the root (r,c). Stores all 
        coordinates in its neighborhood in self.in_range.

        Args:
            r (int): Row number of root coordinate.
            c (int): Column number of root coordinate.
        """
        root = (r, c)
        frontier = [root]
        visited = set()

        # Makes checking directions more readable,
        # determines if a coordinate is in-bounds.
        def _in_bounds(row, col):
            return -1 < row < self.h and -1 < col < self.w

        # Breadth-first search logic
        while frontier:
            curr = frontier.pop(0)
            if 0 <= self.manhattan(*curr, *root) <= self.n:
                self.in_range.add(curr)

                # Move in cardinal directions.
                tmp_r, tmp_c = curr
                for direction in [(tmp_r-1, tmp_c), (tmp_r+1, tmp_c), (tmp_r, tmp_c+1), (tmp_r, tmp_c-1)]:
                    if _in_bounds(*direction) and direction not in visited:
                        frontier.append(direction)
                        visited.add(direction)

    def solve(self):
        """ Iterates over all cells, calls bfs_search on positive values.

        Returns:
            int: Number of cells within n-steps of positive values.
        """
        for r in range(self.h):
            for c in range(self.w):
                if self.neighborhood[r][c] > 0:
                    self.bfs_search(r, c)
        return len(self.in_range)

    def show(self, title=None):
        """ Useful for testing. Should be called after solve.
        Populates out of range cells with 0, in-range cells with -1, 
        and positive cells with 1.

        Args:
            title (str, optional): Custom title for the graph, useful when running multiple test cases. Defaults to 'n={self.n}, in_range={len(self.in_range)}'.
        """

        # Copy neighborhood
        grid = self.neighborhood

        # Distinguish in-range cells
        for r, c in self.in_range:
            if (r, c) not in self.filled:
                grid[r][c] = -1

        if title is None:
            title = f'n={self.n}, in_range={len(self.in_range)}'

        plt.pcolor(grid, edgecolors='k', linewidths=.5)
        plt.title(title)
        plt.show()


if __name__ == '__main__':
    # Example in README.md
    n = Neighborhood(n=10, h=101, w=101 ,filled_cells=[(x, y) for x in range(0, 100, 2) for y in range(0,100,2)])
    n.solve()
    n.show()
