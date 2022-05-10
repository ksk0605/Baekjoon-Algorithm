#include <iostream>
#include <string>

using namespace std;

int main(){
  string s;
  cin >> s;
  for (int i = 97; i<123; i++){
    int num = 0;
    for (int j = 0; j<s.size(); j++){
      if (s[j] == i)
        num++;
    }
    cout << num << ' ';
  }
}