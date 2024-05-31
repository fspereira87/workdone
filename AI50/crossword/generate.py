import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)


    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for variable in self.domains:
            variable_len = variable.length
            remove = set()

            for val in self.domains[variable].copy():
                if len(val) != variable_len:
                    remove.add(val)

            self.domains[variable] -= remove

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        rev = False

        # Check overlap
        if self.crossword.overlaps[x, y]:
            x_index, y_index = self.crossword.overlaps[x, y]

            # Iterate over values in the domain of x
            for valx in list(self.domains[x]):
                if not any(valx[x_index] != valy[y_index] for valy in self.domains[y]):
                    continue

                # If a conflict is found, remove the value from the domain of x
                self.domains[x].remove(valx)
                rev = True

        return rev



    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        queue = list(arcs) if arcs else list((x,y) for x in self.crossword.variables for y in self.crossword.neighbors(x))


        while queue:
            x,y = list(queue).pop(0)

            if self.revise(x,y):
                if not self.domains[x]:
                    return False

            # Add arcs (x, z) for all neighbors z of x, excluding y
            queue.extend((x,z) for z in self.crossword.neighbors(x) if z!= y)

        return True


    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # Check if every variable in the crossword is present in the assignment

        return all(variable in assignment for variable in self.crossword.variables)


    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # Check if values are distinct
        values = set(assignment.values())

        if len(values) != len(assignment):
            return False

        # Check the length of every value
        for variable, word in assignment.items():
            if variable.length != len(word):
                return False

        # Check for conflicts between neighboring variables
        for x, y in self.crossword.overlaps:
            if x in assignment and y in assignment:
                overlap = self.crossword.overlaps[x, y]

                # Check if there is an overlap
                if overlap:
                    overlap_x, overlap_y = overlap
                    if assignment[x][overlap_x] != assignment[y][overlap_y]:
                        return False

        return True


    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # Helper function to count the number of values ruled out for neighboring unassigned variables.
        def ruled_out_values(var, value, assignment):
            count = 0
            for neighbor in self.crossword.neighbors(var):
                # Check if is unassigned
                if neighbor not in assignment:
                    # Check the overlap
                    overlap = self.crossword.overlaps[var, neighbor]
                    if overlap:
                        var_index, neighbor_index = overlap
                        neighbor_domain = set(word for word in self.crossword.words if len(word) == neighbor.length)

                        for neighbor_value in neighbor_domain:
                            # Check if indices are within the valid range
                            if (
                                0 <= var_index < len(var.cells) and
                                0 <= neighbor_index < len(neighbor_value) and
                                var_index < len(value) and
                                neighbor_index < len(value) and
                                neighbor_value[neighbor_index] != value[var_index]
                            ):
                                count += 1
            return count

        # Get the domain values of `var` based on its length
        domain_values = [word for word in self.crossword.words if len(word) == var.length]

        # Order the domain values based on least-constraining values heuristic
        domain_values.sort(key=lambda value: ruled_out_values(var, value, assignment))

        return domain_values


    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        unassigned_variables = [var for var in self.crossword.variables if var not in assignment]

        # Sort the unassigned variables based on the minimum remaining value heuristic
        # and then the degree heuristic
        unassigned_variables.sort(
            key=lambda var: (len(self.crossword.words.intersection(var.cells)), -len(self.crossword.neighbors(var)))
        )

        # Return the variable with the fewest remaining values and highest degree
        return unassigned_variables[0]

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            # If the assignment is complete, return it
            return assignment

        # Select an unassigned variable using the minimum remaining value and degree heuristic
        var = self.select_unassigned_variable(assignment)

        for value in self.order_domain_values(var, assignment):
            # Try assigning the value to the variable
            new_assignment = assignment.copy()
            new_assignment[var] = value

            # Check if the assignment is consistent
            if self.consistent(new_assignment):
                # Recursively call backtrack with the new assignment
                result = self.backtrack(new_assignment)

                # If a complete assignment is found, return it
                if result is not None:
                    return result

        # If no assignment is possible, return None
        return None



def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
