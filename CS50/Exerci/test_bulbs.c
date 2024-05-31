#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    int i;
    string s = get_string("Message: ");
    int len = strlen (s);

    for (i=0; i<len; i++)
    {
        s[i]= (int) s[i];
    }

    printf ("ASCII: %d\n", s);
    return 0;

}