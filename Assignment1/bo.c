//
// Created by benji on 9/8/23.
//

#include <stdio.h>
#include "assignment.h"

int login() {
    // default login status is failed
    int success = 'F';
    char passwd[80];
    gets(passwd);
    return success;
}

void welcome() {
    printf("Welcome, you are logged in!\n");
    exit(0);
}

void quit() {
    printf("The password is incorrect.\n");
    exit(1);
}

void main() {
    printf("Please enter password: ");
    if(login() == 'T')
        welcome();
    else
        quit();
}