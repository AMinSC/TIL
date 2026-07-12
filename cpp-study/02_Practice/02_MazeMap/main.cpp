//
// Created by user on 26. 7. 12..
//

#include "main.h"
#include <iostream>
using namespace std;
#include "Helper.h"
#include "Map.h"
#include "player.h"



int main()
{
    SetCursorOnOff(false);

    while (true)
    {
        // 입력
        HandleKeyInput();

        // 로직
        HandleMove();

        // 출력
        PrintMap2D();

    }
}
