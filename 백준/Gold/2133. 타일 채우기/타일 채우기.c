#include <stdio.h>

int d[1001];

int dp (int n){
	if(n==0) return 1;
	if(n==1) return 0;
	if(n==2) return 3;
	if(d[n] != 0) return d[n];
	int result = 3 * dp(n-2);
	for(int i = 4; i <= n; i++){
		if(i%2==0) result += 2 * dp(n-i);
	}
	return d[n] = result;
}

int main(){
	int n;
	scanf("%d", &n);
	printf("%d", dp(n));
	return 0;
}
