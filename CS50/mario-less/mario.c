#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Get Size of the piramid
    int n;
    do
    {
        n = get_int ("Choose the Height between 1 and 8: ");
    }

    //Print the piramid
    while (n < 1 || n > 8);

       for (int i = 1; i <= n; i++)

       {
        
        for (int j = 1; j <= n - i; j++)
        {
            printf(" ");
        }

        for (int j = 1; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }

}