#include <iostream>
using namespace std;

int main(){
    int i,j,k;
    int a[100];

    for (i=0; i<8; i++){
        cin >> a[i];
    }

    for (i=0; i<8; i++){
        for (j=0; j<7-i; j++){
            if (a[j] > a[j+1]){
                k = a[j];
                a[j] = a[j+1];
                a[j+1] = k;
            }
        }
    }

    for (i=0; i<8; i++){
        cout << a[i] << ' ';
    }
}