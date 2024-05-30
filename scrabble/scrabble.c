#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);


int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 > score2)
    printf ("Player 1 wins!");

    else if (score1 < score2)
    printf("Player 2 wins!\n");

    else
    printf("Is a tie");

    return 0;
}


int compute_score(string word)
{

int len = strlen (word);
int pos [100];
int score =0;

    // Convert Lower case in uper case
    for (int i =0; i<len; i++)
    {
        if (word [i] >= 'a' && word [i] <= 'z')
        word[i]= toupper (word [i]);
    }

    //Calculate score for each word
    for (int i =0; i<len; i++)
    {
        if (word [i] >= 'A' && word [i] <= 'Z')
        pos[i]=word[i]-'A';

        else
        pos[i]=-1;
    }

    for (int i =0; i<len; i++)
    {
        if (pos[i] != -1)
        score += POINTS[pos[i]];
    }

    return score;
}





