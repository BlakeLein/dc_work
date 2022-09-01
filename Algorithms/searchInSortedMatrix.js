const searchMatrix = (matrix, target) => {
  // For Loop for ROWS
  for (let r = 0; r < matrix.length; r++) {
    // r refers to each row, 'rows' is the
    const rows = matrix[r];
    for (let c = 0; c < rows.length; c++) {
      if (rows[c] === target) return [r, c];
    }
    return [-1, -1];
  }
};

const matrix = [
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004],
];

const target = 44;

searchMatrix(matrix, target);
