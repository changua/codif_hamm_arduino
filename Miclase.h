#ifndef Miclase_h
#define Miclase_h
#include <Arduino.h>

class Miclase
{

public:
    Miclase();
    void generador_funciones();
private:
  char option;
  String number;
  float volta;
  float valor_sensor;
  float voltaje;
};


#endif
