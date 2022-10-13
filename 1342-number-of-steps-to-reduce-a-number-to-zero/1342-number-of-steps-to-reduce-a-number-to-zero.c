/*
14
7 6 ---1, 2
3 2 ---3, 4
1 0 ---5, 6
*/
int numberOfSteps(int num){
    int count = 0;
    
    while (num != 0) {        
        if (num % 2 == 0) {
            num /= 2;
            count++;
        }
        else {
            num -= 1;
            count++;
        }
    }
    
    return count;
}