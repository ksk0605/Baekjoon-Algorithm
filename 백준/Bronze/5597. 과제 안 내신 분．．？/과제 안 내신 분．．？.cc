#include <iostream>

using namespace std; 

int main() {
  int student[31] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30};
  for (int i = 1; i<=28; i++){
    int n;
    cin >> n;
    student[n] = 0;
  }
  for (int i = 1; i<=30; i++){
    if (student[i] != 0) 
      cout << i << '\n';
  }
}