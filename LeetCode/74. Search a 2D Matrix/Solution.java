/**
 * Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
 * 
 * Integers in each row are sorted from left to right.
 * The first integer of each row is greater than the last integer of the previous row.
 * 
 * Example 1:
 * Input:
 *  matrix = [
 * [1,   3,  5,  7],
 * [10, 11, 16, 20],
 * [23, 30, 34, 50]
 * ]
 * 
 * target = 3
 * Output: true
 * 
 * Example 2:
 * 
 * Input:
 * matrix = [
 * [1,   3,  5,  7],
 * [10, 11, 16, 20],
 * [23, 30, 34, 50]
 * ]
 * 
 * target = 13
 * Output: false
 */

class Solution {

    /** This is a O(n+m) solution */
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix.length == 0)
            return false;
        
        int row = 0;
        int col = matrix[0].length - 1;
        
        while(row < matrix.length && col >= 0 )
        {
            if (matrix[row][col] > target)
                col--;
            else if(matrix[row][col] < target)
                row++;
            else
                return true;
        }
        return false;
    }

    public boolean searchMatrixII(int[][] matrix, int target)
    {
        if(matrix.length == 0)
            return false;
        
        int m = matrix.length;
        int n = matrix[0].length;
        
        // a binary search anstracting the entire 2D matrix as an array with row = mid // n and column = mid % n
        int low  = 0;
        int high = m*n -1;
        int pivotElement;
        
        while(low <= high)
        {
            int mid = low + (high - low) / 2;
            pivotElement = matrix[mid / n][mid %n];
            
            if (target == pivotElement)
                return true;
            else {
                if(target < pivotElement)
                    high = mid -1;
                else
                    low = mid + 1;
            }
        }
        return false;
    }
}