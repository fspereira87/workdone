#include <stdio.h>
#include <cs50.h>

int main(void)

{

long x = get_long ("x: "); // long para numeros grandes (explicação bits limitados)
long y = get_long ("y: ");

float z = (float) x / (float) y; //converter em decimal. Usamos (float)

printf("Result: %.20f\n", z); // %f para out put decimal

// floating points leva a um erro (floating point impercision) que pode ser corrigido ao substituir na linha 11 float por double que usa 64 bits em vez de 32
}

