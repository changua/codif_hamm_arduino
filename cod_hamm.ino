#include "cod_hamm.h"
cod_hamm hamming;
String c[]="";:
int i=0;
void setup(){
	Serial.begin(9600);
}

void loop(){
	if (Serial.available())
	
		c+=Serial.read();
	}
	else
	{
		for(i=0;i<strlen(c);i++)
			Serial.write(c[i]);
	}	
}
