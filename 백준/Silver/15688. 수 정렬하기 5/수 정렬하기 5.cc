#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> v;

int main(void){
    ios::sync_with_stdio(false);
	cout.tie(NULL);
	cin.tie(NULL);
    
    int n;
    cin >> n;
    
    for (int i = 0; i<n; i++){
        int num;
        cin >> num;
        v.push_back(num);
    }
    
    sort(v.begin(), v.end());
    
    for (int i =0; i<n; i++){
        cout << v[i] << '\n';
    }
    
    return 0;
}