/*
 * file: currency_converter.c
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cdecl.h"

extern float converter_float(float, float);

int main(int argc, char *argv[])
{
    if(argc != 3){
        printf("Número de parámetros no válido.\n");
        exit(1);
    }
    float source_currency = atof(argv[1]);    // Criptomoneda en USD
    float convertion_factor = atof(argv[2]);  // Factor de conversión a EUR o ARS
    float dest_currency = converter_float( source_currency, convertion_factor);

    printf("%f\n",dest_currency);
  
    return 0;
}