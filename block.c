#include <stdio.h>
int main(void)
{
    for(int a = 1; a < 100; a++)
    {
        for(int b = a; b < 100; b++)
        {
            for(int c = b; c < 100; c++)
            {
                if(a*a + b*b == c*c) // **2 does not work in C
                {
                    printf("%d %d %d\n", a, b, c);
                }
            }
        }
    }
}