#include<stdlib.h>
#include<stdio.h>
#include"definitions.h"
#include<string.h>

double converter(double a, double b) {
    return 0.0;
}

bool parser(char *json_str, size_t json_str_size)  {
    json_str[json_str_size] = '\0';
    printf("Hello world! %s - %d\n", json_str, strlen(json_str));
    return true;
}

