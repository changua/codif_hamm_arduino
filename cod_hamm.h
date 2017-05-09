//Inicio de la clase: uso clases para no hacer declaraciones globales de las variables.
#ifndef cod_hamm_h
#define cod_hamm_h
#include <stdio.h>
#include <iostream>
#include <time.h>
#include <string.h>
#include <math.h>
class cod_hamm  //clase cod_hamm.
{
    public:
        //funciones para codificación:
        void carc_bin(char c); //objeto de la clase, convierte de caracter a binario.
        void par();//objeto de la clase, halla la paridad del caracter.
        void men();//objeto de la clase, agrega las paridades y el byte de sincrinizacion
        //funciones para la decodificación:
        void sinc();//objeto de la clase, elimina el byte de sincronizacion.
        void errorr();//objeto de la clase, busca errores y los corrige si llega a existir.
        void deco();//objeto de la clase, obtiene los bits del mensaje.
        char bin_carc();//objeto de la clase, convierte de binario a caracter.
        //Variables a usar.  
        int b[7],m[12];
        int cod[20];        
        int p[4];
};
#endif
