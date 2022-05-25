#include <bits/stdc++.h>

using namespace std;

int main() {
  string s;
  cin >> s;
  list<char> editor;
  
  for (auto a:s) {
    editor.push_back(a);
  }
  auto e = editor.end();

  int n;
  cin >> n;
  cin.ignore();
  
  string command;
  for(int i = 0; i<n; i++){
    getline(cin, command);
    
    switch(command[0]){
    case 'L':
      if (e != editor.begin())
        e--;
      break;
    case 'D':
      if (e != editor.end())
        e++;
      break;
    case 'B':
      if (e != editor.begin()){
        e--;
        e = editor.erase(e);
      }
      break;
    case 'P':
      e = editor.insert(e, command[2]);
      e++;
      break;
    }
  }
  for (e = editor.begin(); e != editor.end(); e++){
    cout << *e;
  }
}