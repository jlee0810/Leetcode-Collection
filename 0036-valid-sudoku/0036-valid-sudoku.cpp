class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<set<char>> row(9);
        vector<set<char>> col(9);
        vector<set<char>> ssquare(9);

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (isdigit(board[i][j])) {
                    int square_num = (i / 3) * 3 + (j / 3);

                    if (row[i].find(board[i][j]) != row[i].end()) {
                        return false;
                    }
                    if (col[j].find(board[i][j]) != col[j].end()) {
                        return false;
                    }
                    if (ssquare[square_num].find(board[i][j]) != ssquare[square_num].end()) {
                        return false;
                    }
                    row[i].insert(board[i][j]);
                    col[j].insert(board[i][j]);
                    ssquare[square_num].insert(board[i][j]);
                }
            }
        }
        return true;
    }
};