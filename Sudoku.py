matrix =  []
row = 9
column = 9

in_range = True

print("Welcome to the Sudoku Solver")
print("Please enter numbers between 1 and 9. If the field is empty put in a 0")

#creating matrix
def create_matrix(matrix):
    while in_range:
        for i in range(row):    
            a = []
            print("Enter the numbers for row {}".format(i+1))   
    
            for j in range(column):
            
                num = int(input())
                if(num < 0 or num > 9):
                    in_range = False
                    print("Error.Please enter a number between 0 and 9")
                    num = int(input())
                else:
                    in_range = True
                    a.append(num)
                in_range = False        
            matrix.append(a)
    return matrix        

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

def find_empty(matrix): 
    for row in range(9): 
        for column in range(9): 
            if matrix[row][column] == 0: 
                return row, column 
    return 0,0 

def solve(matrix): 
    matrix = create_matrix(matrix)
    print(print_matrix(matrix))
    row, column = find_empty(matrix)
    if row == 0 : 
        if column == 0: 
            return True

    for num in range(1,10):
        if(is_valid(matrix, num, row,)):
            matrix[row][column] = num   

            if solve(matrix):
                return True     
        matrix[row][column] = 0
    return False                  

def missing_square(row,column,matrix):
    missing_square= [1,2,3,4,5,6,7,8,9]
    for i in range(row//3*3, row//3*3+3):
        for j in range(column//3*3,column//3*3+3):
            for k in range(1,10):
                if matrix[i][j] == k:
                    missing_square.remove(k)
                    break
    return missing_square   

def missing_row(row,column,matrix):
    missing_row = [1,2,3,4,5,6,7,8,9]
    for j in range(column, column +9):
        for k in range(1,10):
            if matrix[row][j] == 0:
                break
            elif matrix[row][j] == k:
                missing_row.remove(k)
                break
    return missing_row

def missing_column(row,column,matrix):
    missing_column = [1,2,3,4,5,6,7,8,9] 
    for i in range(row, row +9):
        for j in range(1,10):
            if matrix[i][column] == 0:
                break
            elif matrix[i][column] == j:
                missing_column.remove(j)
                break
    return missing_column 

def is_valid(matrix,num,row,column):
    if num in missing_square(row, column, matrix):
        return False
    elif num in missing_row(row, column, matrix):
        return False
    elif num in missing_column(row, column, matrix):
        return False        
    else:
         return True    

print(solve(matrix))