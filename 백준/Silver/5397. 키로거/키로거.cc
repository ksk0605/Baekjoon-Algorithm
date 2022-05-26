#include <iostream>
#include <list>

using namespace std;

int main() {
  int n;
  cin >> n;

  cin.ignore();
  
  
  for (int i =0; i<n; i++){
    string l;
    getline(cin, l);

    list<char> code = {};
    auto iter = code.begin();

    for(auto c:l){
      switch(c){
        case '<':
          if (iter != code.begin())
            iter--;
          break;
        case '>':
          if (iter != code.end())
            iter++;
          break;
        case '-':
          if (iter != code.begin()){
            iter = code.erase(--iter);
          }
        break;
        default:
          code.insert(iter, c);
      }
    }
    for(auto c = code.begin(); c != code.end(); c++){
      cout << *c;
    }
    cout << '\n';
  }
}