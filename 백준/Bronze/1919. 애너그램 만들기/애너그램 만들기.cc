#include <bits/stdc++.h>

using namespace std;

int arr[2][30], res;
string a,b;
int main() {
  cin >> a >> b; 

  for (auto i: a){
    arr[0][i - 'a']++;
  }
  for (auto i: b) { 
    arr[1][i - 'a']++;  
  }

  for (int i = 0; i<26; i++){
    res += abs(arr[0][i] - arr[1][i]);  
  }
  cout << res;
}