# Termsweeper

A terminal-based rendition of the classic game, Minesweeper.

## Prerequisites

### Python

Requires python3 or higher.

### Termcolor

Using pip: ```pip install termcolor```

## How to play

You begin with a grid consisting of numbers and gray squares.
The numbers tell you how many land mines are adjacent to the given square (horizontally, vertically, or diagonally).
Based on the given numbers, you can either flag or dig a gray square.

To dig:
```d [x-cor] [y-cor]```

To flag:
```f [x-cor] [y-xor]```

The goal is to flag all of the land mines. If you dig a land mine, you automatically lose. Good luck! 
