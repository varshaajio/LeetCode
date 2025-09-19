class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        self.rows = rows
        self.grid = {}  # Dictionary to store cell values keyed by cell reference like "A1"

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        self.grid[cell] = value

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        if cell in self.grid:
            del self.grid[cell]

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        def parse_token(token):
            if token[0].isalpha():
                return self.grid.get(token, 0)
            else:
                return int(token)

        # Remove '=' and split by '+'
        tokens = formula[1:].split('+')
        return parse_token(tokens[0]) + parse_token(tokens[1])

