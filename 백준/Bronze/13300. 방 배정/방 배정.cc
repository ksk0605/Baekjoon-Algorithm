#include <iostream>
using namespace std;

int bRoom[7];
int gRoom[7];

int main() {
    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        int s, y;
        cin >> s >> y;
        if (s == 0) {
            gRoom[y]++;
        }
        else {
            bRoom[y]++;
        }
    }

    int gCnt = 0, bCnt = 0;
    for (int i = 1; i < 7; i++) {
        if (gRoom[i] != 0) {
            if (gRoom[i] % k == 0)
                gCnt += gRoom[i] / k;
            else
                gCnt += gRoom[i] / k + 1;
        }
        if (bRoom[i] != 0) {
            if (bRoom[i] % k == 0)
                bCnt += bRoom[i] / k;
            else
                bCnt += bRoom[i] / k + 1;
        }
    }
    cout << gCnt+bCnt;
}