#include <stdio.h>
#include <cs50.h>

int main (void)
{
    string answer = get_string ("What is your name? ");
    printf ("Hi %s\n", answer);

}

//command clang (substitue for make, mv and more)
// clang -0 hello hello.c - (make and change name)
//clang hello.c - creates default file a.out to every program (use ls to check)
//clang doesn't assume cs50.h, must write in the command. clang o- hello hello.c - lcs50