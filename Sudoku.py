matrix =   [[9,1,0,0,3,8,0,7,0],
            [0,0,0,6,0,0,0,0,8],
            [0,3,0,1,0,0,0,0,0],
            [0,0,0,8,0,0,0,0,0],
            [0,0,2,0,0,0,0,9,0],
            [0,6,0,0,5,4,0,0,7],
            [0,0,0,0,1,0,0,0,0],
            [6,0,0,0,0,0,5,0,0],
            [0,5,0,0,7,3,0,0,4]]
row = 9
column = 9

def print_matrix(matrix):
    for r in range(row):
        if(r%3 == 0):
            print(" ")
        for c in range(column):
            if((c+1)%3 == 0):
                print(matrix[r][c],end = "    ")
            else:
                print(matrix[r][c],end = "  ")    
        print()   

#find the next empty space
def find_empty(matrix): 
    for row in range(9): 
        for column in range(9): 
            if matrix[row][column] == 0: 
                return row, column 
    return None,None

#solving sudoku with recursion
def solve(matrix): 
    print(print_matrix(matrix))
    row, column = find_empty(matrix)
    #check if sudoku is completed
    if row is None : 
        if column is None: 
            return True

    for num in range(1,10):
        print(is_valid(matrix, num, row, column))
        
        if is_valid(matrix, num, row, column):
            matrix[row][column] = num   

            if solve(matrix):
                return True     
        matrix[row][column] = 0
    return False                  

#finds missing numbers in square
def missing_square(row,column,matrix):
    missing_square= [1,2,3,4,5,6,7,8,9]

    for i in range(row//3*3, row//3*3+3):
        for j in range(column//3*3,column//3*3+3):
            for k in range(1,10):
                if matrix[i][j] == k:
                    if k in missing_square:
                        missing_square.remove(k)
                    break
    return missing_square   

#finds missing numbers in row
def missing_row(row,column,matrix):
    missing_row = [1,2,3,4,5,6,7,8,9]
    for j in range(0, 9):
        for k in range(1,10):
            if matrix[row][j] == 0:
                break
            elif matrix[row][j] == k:
                if k in missing_row:
                    missing_row.remove(k)
                break
    return missing_row

#finds missing numbers in column
def missing_column(row,column,matrix):
    missing_column = [1,2,3,4,5,6,7,8,9] 
    for i in range(0, 9):
        for j in range(1,10):
            if matrix[i][column] == 0:
                break
            elif matrix[i][column] == j:
                if j in missing_column:
                    missing_column.remove(j)
                break
    return missing_column 

#checks if number fits into empty space
def is_valid(matrix,num,row,column):
    if num not in missing_square(row, column, matrix):
        return False
    elif num not in missing_row(row, column, matrix):
        return False
    elif num not in missing_column(row, column, matrix):
        return False        
    
    return True    


print(solve(matrix))
  
