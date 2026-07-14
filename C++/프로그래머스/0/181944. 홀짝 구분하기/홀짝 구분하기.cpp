#include <iostream>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    
    // true : output + 1, false : output + 0
    // cout << n << (n % 2 == 0) ? " is even" : " is odd";
    
    cout << n << ((n % 2 == 0) ? " is even" : " is odd");
    return 0;
}