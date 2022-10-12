int maximumWealth(int** accounts, int accountsSize, int* accountsColSize){
    int total = 0;

    for (int i = 0; i < accountsSize; i++) {
        int row_sum = 0;
        for (int j = 0; j < *accountsColSize; j++) {
            row_sum += accounts[i][j];
        }
        if (total < row_sum) {
            total = row_sum;
        }
    }
    return total;
}