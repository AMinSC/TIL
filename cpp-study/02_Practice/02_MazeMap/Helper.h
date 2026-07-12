//
// Created by user on 26. 7. 12..
//

#ifndef CPP_STUDY_HELPER_H
#define CPP_STUDY_HELPER_H

enum MoveDir
{
    MD_NONE,
    MD_LEFT,
    MD_RIGHT,
    MD_UP,
    MD_DOWN,
};

void HandleKeyInput();
void SetCursorPosition(int x, int y);
void SetCursorOnOff(bool visible);

extern MoveDir GMoveDir;

#endif //CPP_STUDY_HELPER_H
