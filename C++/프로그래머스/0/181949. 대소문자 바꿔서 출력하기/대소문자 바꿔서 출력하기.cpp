#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main(void) {
    string str;
    cin >> str;
    
    for (char c : str)
    {
        if (isupper(c) == 0)
            cout << (char)toupper(c);
        else
            cout << (char)tolower(c);
    }
    return 0;
}