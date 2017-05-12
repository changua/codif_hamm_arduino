#include "cod_hamm.h"
/*funciones de la clase*/
void cod_hamm::carc_bin(char c)
{
    int x=c;
	for (int i=0;i<7;i++)
	{	
		b[7-i]=x%2;
		x=x/2;
	}
}
void cod_hamm::par()
{
	int aux=b[0]+b[1]+b[3]+b[4]+b[6];
	p[0]=aux%2;
	aux=b[0]+b[2]+b[3]+b[5]+b[6];
	p[1]=aux%2;
	aux=b[1]+b[2]+b[3]+b[7];
	p[2]=aux%2;
	aux=b[4]+b[5]+b[6]+b[7];
	p[3]=aux%2;
}
void cod_hamm::men()
{
	int sin[]={0,0,0,0,0,0,0,1};
	cod[8]=p[0];
	cod[9]=p[1];
	cod[11]=p[2];
	cod[15]=p[3];
	for (int i=0;i<8;i++)//tiene un problema, modifica el vector de paridades.
	{
		cod[i]=sin[i];
	}
	for (int i=10,j=1,k=0;i<20;i++)//llena el mensaje codificado y con el byte de paridad.
	{
		if (i!=11 && i!=15)
		{	
			cod[i]=b[k];
			k++;
		}
	}
}
void cod_hamm::sinc()
{
	for (int i=0;i<12;i++)//elimina el byte de sinc.
	{
		m[i]=cod[i+8];
	}
}
void cod_hamm::errorr()
{	
	int aux=m[0]+m[2]+m[4]+m[6]+m[8]+m[10];
	int e[3];
	e[0]=aux%2;
	aux=m[1]+m[2]+m[5]+m[6]+m[9]+m[10];
	e[1]=aux%2;
	aux=m[3]+m[4]+m[5]+m[6]+m[11];
	e[2]=aux%2;
	aux=m[7]+m[8]+m[9]+m[10]+m[11];
	e[3]=aux%2;
	int pe=e[0]+e[1]*2+e[2]*4+e[3]*8;//calculo del error.
	if (pe!=0)
	{
		if (m[pe-1]==1)
			m[pe-1]=0;
		else
			m[pe-1]=1;
	}
}
void cod_hamm::deco()//decodifica el mensaje partiendo del vector m
{
	for (int i=2,j=0;i<12;i++)
	{
		if (i!=3 && i!=7)//estas posciones son paridades.
		{
			b[j]=m[i];
			j++;
		}
	}
}
char cod_hamm::bin_carc()
{
	int x=0;
	for (int i=0,j=7;i<8;i++,j--)//calcula el valor en ascii del vector b
		{
			x=b[i]*(pow(2,j))+x;
		}
	//char c=x;//convierte el ascii en caracter no estoy seguro si es necesario.
	return (x);
}
/*finaliza el código*/
