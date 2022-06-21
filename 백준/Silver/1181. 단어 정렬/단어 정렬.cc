#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(string a, string b){
  if (a.length() == b.length())
    return a<b;
  return a.length()<b.length();
}

int main() {
  int n; 
  cin >> n; 
  vector<string> s;
  for (int i =0; i<n; i++) {
    string str;
    cin >> str;
    s.push_back(str);
  }
  sort(s.begin(), s.end(), compare);
  s.erase(unique(s.begin(), s.end()), s.end());
  
  for(string a:s){
    cout << a << '\n';
  }
}