#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char word[100];
    int i, len;
    int pos [100];
    int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
    int score = 0;

    printf("Enter a word: ");
    scanf("%s", word);

    len = strlen(word);

    for (i = 0; i < len; i++) {
        if (word[i] >= 'a' && word[i] <= 'z') {
            pos[i] = word[i]-'a';

        }
        else if (word[i] >= 'A' && word[i] <= 'Z') {
            pos[i] = word[i]-'A';
        }
        else
        {
            pos[i]= -1; //Non-alphabetic characters
        }
    }

    for (i = 0; i<len;i++)
    {
        if (pos [i] != -1)
        score +=  (POINTS[pos[i]]); //calculate points
    }

        printf("Score: %d\n", score);
        return 0;

}