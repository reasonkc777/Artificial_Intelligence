#include <iostream>
#include <vector>
using namespace std;
vector<char> alternate_combine(vector<char> arr1, vector<int> arr2) {
    vector<char> combined;
    int len = max(arr1.size(), arr2.size());
    for (int i = 0; i < len; i++) {
        if (i < arr1.size()) {
            combined.push_back(arr1[i]);
        }
        if (i < arr2.size()) {
            combined.push_back(arr2[i]);
        }
    }
    return combined;
}

int main() {
    vector<char> arr1 = {'a', 'b', 'c'};
    vector<int> arr2 = {49, 50, 51};
    vector<char> combined = alternate_combine(arr1, arr2);
    cout<<"[";
    for (int i = 0; i < combined.size(); i++) {
        cout << combined[i] << " ";
    }
    cout << "]" << endl;
    return 0;
    cout << endl;
    return 0;
}
