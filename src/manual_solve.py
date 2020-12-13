#!/usr/bin/python

### Student Name: Ahmed Abdelaziz
### Student ID: 20235539
### Github UR: https://github.com/ahmadsaaad/ARC

import os, sys
import json
import numpy as np
import re



### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.


### Assumptions:
### Any shape will be connected only horozntally or vertically but not diagonally ( otherwise, we would add more functions to the recrusive)
### Shapes have only cells of value 8, other wise we will our if condition


### Description:
### 1- we will find the number of connected shapes that have cells of value 8 
### 2- create an array of length and width = to the number of shapes 
### 3- Fill this matrix diagonally with value 8 

### Code Steps: 
### 1- clone the matrix into new matrix ( we could use the orginal one but just to not cause any effect on the orginal one)
### 2- find the first cell with value =8, increase the number of detected shapes by 1
### 3- clear all neighbour cells and recursively we will clear the neighbours of the neighbour.. untill we clear al the cells of this shape
### 4- continue the loop untill we find the next cell with value 8 ... and do repeated step 2 and 3
### 5- finally create a matrix with x and y equal to the number of shapes and fill it diagonally with 8.
### (hint) to avoid updating the original array or creating a new array and increase the space complixity, we could have create set of visited cells. 

### Python features and libraries:
### in the below function I used standard python with numpy library 
### I used numpy for clonning the 2D array, create an array with default values and to fill the output value diagonally.    
def solve_d0f5fe59(x):
    number_of_shapes=0
    clonned_array=np.copy(x)
    for i in range(len(clonned_array)):
        for j in range(len(clonned_array.T)):
            if clonned_array[i][j]==8:
                number_of_shapes+=1
                clear_cells(i, j, clonned_array)
    output=np.zeros(((number_of_shapes,number_of_shapes)),dtype=int)
    np.fill_diagonal(output, 8)
    return output


def clear_cells(row,column,arr):
    if row <0 or row>=len(arr) or column<0 or column>=len(arr.T):
        return
    if arr[row][column]==0:
        return
    arr[row][column]=0
    clear_cells(row,column+1,arr)
    clear_cells(row+1,column,arr)
    clear_cells(row-1,column,arr)
    clear_cells(row,column-1,arr)



### Assumptions:
### Cells can only have value 8 or zero, other wise we will our if condition

### Description:
### 1- we will find the first cells with value 8 in each row and column
### 2- connect between the first cell and last cell with value 8 in the same column
### 3- connect between the first cell and last cell with value 8 in the same row

### Code Steps: 
### 1- Clone the matrix into new matrix ( we could use the orginal one but just to not cause any effect on the orginal one)
### 2- We will go through every cell
### 3- Create 2 dictionaries rows and columns. rows contains a list of size 2 that contains the first and the last column index of cells that has value 8 in this specific row, while column contains list with size 2 that will have the first and last row index of cells that have value 8 in this sepicfic column.
### 4- The iteration is simple we iterate every row and if we found a cell with value 8, if the row dictionary doesnt have an entry for this row, we will create an entry with value [j,j]
### 5- Every time we find cell with value 8 in this row we will update the second element in the list with this the j of this cell. we will do the same for the columns. 
### 6- iterate over the those 2 dictionaries and connect between the first and last cell in the rows and columns that has value 8

### Python features and libraries:
### In the below function I used standard python with numpy library 
### I used numpy for clonning the 2D array.


def solve_ded97339(x):
    clonned_array=np.copy(x)
    columns={}
    rows={}
    for i in range(len(clonned_array)):
        for j in range(len(clonned_array.T)):
            if clonned_array[i][j]==8:
                if i in rows:
                    rows[i][1]=j
                else:
                    rows[i]=[j,j]
                if j in columns:
                    columns[j][1]=i
                else:
                    columns[j]=[i,i]
                    
    for key in rows.keys():
        row=rows[key]
        row_index=key
        start_column=row[0]
        end_column=row[1]
        if start_column==end_column:
            continue
        for j in range(start_column,end_column+1):
            clonned_array[row_index][j]=8
    
    for key in columns.keys():
        column=columns[key]
        column_index=key
        start_row=column[0]
        end_row=column[1]
        if start_row==end_row:
            continue
        for i in range(start_row,end_row+1):
            clonned_array[i][column_index]=8
            
    return clonned_array


### Assumptions:
### That the grid will have only complete vertical columns or complete horizontal rows and check which one exists.

### Description:
### 1- We will check if the grid in the horozintal mood or vertical mood
### 2- Record Columns/Rows and their colors
### 3- find solo cells that the same colors as the Columns/Rows
### 4- Push these cells to facing side of the column/row that has the same color
### 4- set all other cells to black.

### Code Steps: 
### 1- Create a new matrix with default value 0
### 2- Iterate over the matrix check if the matrix is vertical or horizontal mood.
### 3- Create a dictionary with row/column color and corspnding row/column number and clone these columns/rows to the newly created (zero) array.
### 4- Iterate over the orginal array untill if find a colored cell (non-zero cell) and check the the color has a record in the row_column_dictionary.
### 5- If yes,if the matrix in vertical mood, we will update the cell[row][column+1/column-1] of the clonned matrix with the current value
### 5- If the matrix in horizontal mood, we will update cell[row][column+1/column-1] of the clonned matrix with the current value.
### 6- clear the checked ( set the value of this cell to zero).

### Python features and libraries:
### In the below function, I used standard python with numpy library 
### I used numpy to create a new array with value zeros.


def solve_1a07d186(x):
    is_vertical=True;
    row_column_dictionary={}
    row_column_set=set()
    clonned_array=np.zeros((len(x),len(x.T)),dtype=int)

    for row_i in x:
        if np.all(row_i == row_i[0]) and row_i[0]!=0:
            is_vertical=False
            break;
    if is_vertical:
        for j in range(len(x.T)):
            if np.all(x.T[j] == x.T[j][0]) and x.T[j][0]!=0:
                row_column_dictionary[x.T[j][0]]=j
                row_column_set.add(j)
                clonned_array.T[j].fill(x.T[j][0])
    else:
        for i in range(len(x)):
            if np.all(x[i] == x[i][0]) and x[i][0]!=0:
                row_column_dictionary[x[i][0]]=i
                row_column_set.add(i)
                clonned_array[i].fill(x[i][0])
    for row in range(len(x)):
            if not is_vertical and row in row_column_set:
                continue
            for column in range (len(x[row])):
                if is_vertical and column in row_column_set:
                    continue
                cell=x[row][column]
                if cell in row_column_dictionary:
                    if is_vertical:
                        color_column=row_column_dictionary[cell]
                        if color_column<column:
                            clonned_array[row][color_column+1]=cell
                        else:
                              clonned_array[row][color_column-1]=cell
                    else:
                        color_row=row_column_dictionary[cell]
                        if color_row<row:
                            clonned_array[color_row+1][column]=cell
                        else:
                            clonned_array[color_row-1][column]=cell
    return clonned_array








def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    # if yhat has the right shape, then (y == yhat) is a bool array
    # and we test whether it is True everywhere. if yhat has the wrong
    # shape, then y == yhat is just a single bool.
        
    print(np.all(y == yhat))

if __name__ == "__main__": main()

