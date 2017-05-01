#include "Miclase.h"

Miclase::Miclase()
{

    Serial.begin(9600);
   // canal1='A0';
   // canal2='A1';
}

void Miclase::generador_funciones()
{
  option = Serial.read();
  if (option == 'a')

  {
  valor_sensor = analogRead(A0);
  float voltaje = valor_sensor * (5.0 / 1023.0);
  Serial.println(voltaje);
  //delay(400);
  }

  else if (option == 'b')

  {
  valor_sensor = analogRead(A1);
  float voltaje = valor_sensor * (5.0 / 1023.0);
  Serial.println(voltaje);
 // delay(400);
  }

  else
  {
    number = Serial.readStringUntil('z');
    volta=number.toFloat();
    volta= volta * (225.0/5.0);
    analogWrite(8,volta);
    Serial.println(volta);
  }


  delay(400);

}
