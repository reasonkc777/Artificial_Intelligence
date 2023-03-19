#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int arr1[] = {1, 4, 2};
    int arr2[] = {5, 2, 6, 2, 3};
    int n1 = sizeof(arr1)/sizeof(arr1[0]);
    int n2 = sizeof(arr2)/sizeof(arr2[0]);
    int merged[n1+n2];
    for (int i = 0; i < n1; i++) {
        merged[i] = arr1[i];
    }
    for (int i = 0; i < n2; i++) {
        merged[n1+i] = arr2[i];
    }
    sort(merged, merged + n1 + n2);
    for (int i = 0; i < n1 + n2; i++) {
        cout << merged[i] << " ";
    }
    cout << endl;
    return 0;
}
