//
// Created by user on 26. 6. 23..
//
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int n = 3;

    for (int i = -n; i <= n; i++)
    {
        for (int j = -n; j <= n; j++)
        {
            if (n - abs(i) == abs(j))
                cout << "*";
            else
                cout << " ";
        }
        cout << endl;
    }
}
