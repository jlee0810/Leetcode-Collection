class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<set<int>> rows(9);
        vector<set<int>> cols(9);
        vector<set<int>> squares(9);

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    if (rows[i].find(board[i][j]) != rows[i].end()) {
                        return false;
                    }
                    if (cols[j].find(board[i][j]) != cols[j].end()) {
                        return false;
                    }
                    if (squares[(i / 3) * 3 + (j / 3)].find(board[i][j]) !=
                        squares[(i / 3) * 3 + (j / 3)].end()) {
                        return false;
                    }

                    rows[i].insert(board[i][j]);
                    cols[j].insert(board[i][j]);
                    squares[(i / 3) * 3 + (j / 3)].insert(board[i][j]);
                }
            }
        }

        return true;
    }
};