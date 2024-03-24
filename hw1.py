#TASK 1
def most_common_key(list_of_dicts: list[dict[str, int]]) -> tuple[str, int]:
    ### add types above
    key_dict = {}
    for each in list_of_dicts:
        for key, _ in each.items():
            if key in key_dict.keys():
                key_dict[key] += 1
            else:
                key_dict[key] = 1
    
    for key, val in key_dict.items():
        if val == max(key_dict.values()):
            return (key, val)

#TASK 2
class Board:
    """
    Class to represent a game board.

    Attributes:
        rows (int): number of rows
        cols (int): number of columns
        location_of_pieces (dictionary): maps player to list of locations of
            their pieces

    Methods:
        add_piece: add a piece represented by a string to the board
        on_board: determine if a location is within the bounds of the board
        adjacent: find coordinates of cells to the north, east, south, and west
            of the given location
    """
    def __init__(self, rows: int, cols: int) -> None:
        """
        Constructor for empty board

        Inputs:
            rows [int]: number of rows
            cols [int]: number of columns
        """

        self.rows = rows
        self.cols = cols
        self.location_of_pieces = {}

    def add_piece(self, piece: str, location: tuple[int, int]) -> bool:
        """
        Add a piece represented by a string to the board.

        Inputs:
            piece [string]: the piece to add
            location [tuple]: the (row, column) location of where to add
                the piece
            
        Returns [bool]: True if the piece was added successfully,
            False otherwise
        """
        if not self.on_board(location):
            return False
        
        for player, locations in self.location_of_pieces.items():
            if location in locations:
                return False
        
        if piece in self.location_of_pieces:
            self.location_of_pieces[piece].append(location)
        else:
            self.location_of_pieces[piece] = [location]
        return True
        
    def on_board(self, location: tuple[int, int]) -> float:
        """
        Determine if a location is within the bounds of the board

        Inputs:
            location [tuple]: the (row, column) location in question
            
        Returns [bool]: True if the location is on the board, False otherwise
        """
        row, col = location
        return row >= 0 and row < self.rows and \
               col >= 0 and col < self.cols

    def adjacent(self, location: tuple[int, int]) -> list[tuple[int, int]]:
        """
        Find coordinates of cells to the north, east, south, and west of the
            given location
            
        Inputs:
            location [tuple]: the (row, column) location in question
                
        Returns [list]: coordinates of adjacent spots
        """
        rv = []
        row, col = location
        
        deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dr, dc in deltas:
            adj = (row + dr, col + dc)
            if self.on_board(adj):
                rv.append(adj)
        
        return rv


class TreeNode:
    """ A node in a tree."""
    value: int
    children: list["TreeNode"]

    def __init__(self, value: int):
        self.value = value
        self.children = []

    def add_child(self, child: "TreeNode") -> None:
        self.children.append(child)

    def is_leaf(self) -> bool:
        return len(self.children) == 0
    
        


def get_paths(t: "TreeNode", weight: int) -> list[list[int]]:
    paths = paths_helper(t)
    equal_path = []
    for path in paths:
        if int(sum(path)) != weight:
            path.pop()
        else: 
            equal_path.append(path)
    return equal_path
        

def paths_helper(t: "TreeNode") -> list[list[int]]:
    '''
    This is a helper function to the get_paths function, it creates
    a list of all the root to leaf node and then returns that list
    
    inputs: 
    t: "TreeNode" - instance of TreeNode Class
    
    returns:
    list[list[int]] - list of lists of integers
    '''
    if t.is_leaf():
        return [[t.value]]
    else:
        root_list = []
        for child in t.children:
            current_path = paths_helper(child)
            root_list += current_path
        for i, path in enumerate(root_list):
            root_list[i] = [t.value] + path   
        return root_list
        
