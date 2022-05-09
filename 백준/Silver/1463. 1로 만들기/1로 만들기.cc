#include <stdio.h>

long long int d[1000001];

long long int min(long int a, long int b){
	long long int min;
	if(a>b) return min = b;
	if(b>a) return min = a;
}

long long int dp(int n){
	if(n==0) return 0;
	if(n==1) return 0;
	if(n==2) return 1;
	if(n==3) return 1;
	if(d[n] != 0) return d[n];
	d[n] = dp(n-1) + 1;
	if(n%3==0) d[n] = min(d[n], dp(n/3) + 1);
	if(n%2==0) d[n] = min(d[n], dp(n/2) + 1);
	return d[n];
}

int main(){
	int n;
	scanf("%d", &n);
	printf("%lld", dp(n));
}