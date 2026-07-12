//
// Created by user on 26. 7. 12..
//

#include "Map.h"
#include "helper.h"
#include <iostream>
using namespace std;

int GMap1D[MAP_SIZE * MAP_SIZE] =
{
    1, 1, 1, 1, 1,
    1, 0, 0, 0, 1,
    1, 0, 2, 0, 1,
    1, 0, 0, 0, 1,
    1, 1, 1, 1, 1,
};

int GMap2D[MAP_SIZE][MAP_SIZE] =
{
    { 1, 1, 1, 1, 1 },
    { 1, 0, 0, 0, 1 },
    { 1, 0, 2, 0, 1 },
    { 1, 0, 0, 0, 1 },
    { 1, 1, 1, 1, 1 },
};

void PrintMap1D()
{
    SetCursorPosition(0, 0);

    for (int i = 0; i < MAP_SIZE * MAP_SIZE; i++)
    {
        switch (GMap1D[i])
        {
        case 0:
            cout << "◇";
            break;
        case 1:
            cout << "◆";
            break;
        case 2:
            cout << "♞";
            break;
        }

        if ((i + 1) % MAP_SIZE == 0)
            cout << endl;
    }
}

void PrintMap2D()
{
    SetCursorPosition(0, 0);

    for (int j = 0; j < MAP_SIZE; j++)
    {
        for (int i = 0; i < MAP_SIZE; i++)
        {
            switch (GMap2D[i][j])
            {
            case 0:
                cout << "◇";
                break;
            case 1:
                cout << "◆";
                break;
            case 2:
                cout << "♞";
                break;
            }
        }
        cout << endl;
    }
}
