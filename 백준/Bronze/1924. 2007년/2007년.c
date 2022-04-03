#include <stdio.h>

int main(){
    int month[13] = {0, 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30};
    int mon, date;
    int yoil;
    scanf("%d %d", &mon, &date);
    for(int i = 1; i<=mon; i++){
    	month[0] += month[i];
    }
    yoil = (month[0]+date) % 7;
    if(yoil == 1){
        printf("MON");
    }
    else if(yoil == 2){
        printf("TUE");
    }
    else if(yoil == 3){
        printf("WED");
    }
    else if(yoil == 4){
        printf("THU");
    }
    else if(yoil == 5){
        printf("FRI");
    }
    else if(yoil == 6){
        printf("SAT");
    }
    else if(yoil == 0){
        printf("SUN");
    }
    return 0;
}