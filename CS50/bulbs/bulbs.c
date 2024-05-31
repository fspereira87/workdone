#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit); //print the emoji

int main(void)
{
int i;
int j;

    // TODO
    string s = get_string("Message: ");
    int len = strlen (s);

    for (i=0; i<len; i++)
    {
        //getting ASCII value
        int ascii_value = (int) s[i];

        //Convert to binary

        for ( j = BITS_IN_BYTE -1; j >=0; j--)
        {
            int bit = (ascii_value>>j) & 1;

            print_bulb(bit);

            if (j%8==0)
            {
                printf("\n");
            }
        }
    }
printf("\n");

}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
