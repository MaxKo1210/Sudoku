# SudokuSolver

## How it works:

1. The program looks for an empty cell
2. Looping numbers 1 through 9 and checking for each number if it is missing in square, row and column. If it is missing the number gets placed into the      cell else the next number is tried.
3. If all cells are filled the solved grid will be displayed like this:

```python
9  1  5    2  3  8    4  7  6    
7  2  4    6  9  5    1  3  8    
8  3  6    1  4  7    9  5  2    
 
5  7  3    8  2  9    6  4  1    
4  8  2    7  6  1    3  9  5    
1  6  9    3  5  4    2  8  7    
 
3  4  8    5  1  6    7  2  9    
6  9  7    4  8  2    5  1  3    
2  5  1    9  7  3    8  6  4    
```
Alternatively, if no number can be placed into any of the empty cells the program returns false.
