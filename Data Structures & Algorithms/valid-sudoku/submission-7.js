class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        let col = new Array(9).fill().map(()=> new Array(9).fill(0));
        let block = new Array(9).fill().map(()=> new Array(9).fill(0))
        for (let i=0; i<9; i++) {
            let row = new Array(9).fill(0);
            for (let j=0; j<9; j++) {
                if ( board[i][j] === ".") continue
                let num = Number(board[i][j]) - 1
                let blockIdx = Math.floor(i/3)*3 + Math.floor(j/3)
                if (block[blockIdx][num] === 1 || col[j][num] === 1 || row[num] === 1) return false
                row[num]++
                col[j][num]++
                block[blockIdx][num]++
            }
        }
        return true
    }
}
