# colors using ANSI escape codes:
# https://en.wikipedia.org/wiki/ANSI_escape_code


# define text colors
textcolor_dict = {
    'black':  30,
    'red':    31,
    'green':  32,
    'yellow': 33,
    'blue':   34,
    'purple': 35,
    'cyan':   36,
    'white':  37
}

# define background colors
bgcolor_dict = {
    'black':  40,
    'red':    41,
    'green':  42,
    'yellow': 43,
    'blue':   44,
    'purple': 45,
    'cyan':   46,
    'white':  47
}

# define text style
style_dict = {
    'none':      0,
    'bold':      1,
    'underline': 2
}


class Cell:
    def __init__(self, text=' ', textcolor='white', bgcolor='black', style='none'):
        """initializes the single cell
        """
        # set all the properties
        self.text = text
        self.textcolor = textcolor
        self.bgcolor = bgcolor
        self.style = style
        # update the color using a method
        self._updatecolor()
    
    def _updatecolor(self):
        """private function to update the ansicolorstring
        use the dicts to convert the selected text color, background color and style
        into an ANSI escape code
        note that you could just use the numbers, but it's easier to just map
        the names to numbers using a dict
        """
        self.ansicolorstring = f'\33[{style_dict[self.style]};{textcolor_dict[self.textcolor]};{bgcolor_dict[self.bgcolor]}m'

    def setcolor(self, textcolor=None, bgcolor=None, style=None):
        """function to set one or more of the styling/coloring options
        """
        if textcolor != None:
            self.textcolor = textcolor
        if bgcolor != None:
            self.bgcolor = bgcolor
        if style != None:
            self.style = style
        # update the color using a method
        self._updatecolor()

    def __str__(self):
        """this returns a printable string (in this scenario just a character
        which has been colored using the ANSI escape code)
        """
        return f'{self.ansicolorstring}{self.text}'
    

class Grid:
    def __init__ (self, text=''):
        if type(text) == str:
            textlist = text.splitlines()
        else:
            textlist = text
        self.grid = []
        for line in textlist:
            row = []
            for char in line:
                if char != '\n':
                    row.append(Cell(char))
            self.grid.append(row)
        
    def __str__(self):
        result = ''
        for row in self.grid:
            for cel in row:
                result += str(cel)
            result += '\n'
        return result


with open('example.txt') as infile:
    text = infile.readlines()


grid = Grid(text)

print(grid)