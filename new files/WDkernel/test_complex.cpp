//#include <stdlib.h>
//#include <cmath>
//#include <complex>
//#include <iostream>
//using namespace std; 

#include "common.h"
#include "WDkernel.h"

/*
void random_init(Complex ** array, int n, int m)
{

  for (int i=0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      array[i][j] = polar(1.0,sqrt(1.0/6.0)*(double(rand())/ (RAND_MAX)));
    }
  }
  return;
}



double ** allocateTwoDimenArray(int row, int col)
{
    double ** ptr = (double **) malloc(sizeof(double *)*row);
    for(int i = 0; i < row; i++)
    {
        ptr[i] = (double *) malloc(sizeof(double)*col);
    }
    return ptr;
}

Complex ** allocate2DComplexArray(int n, int m)
{
    Complex ** ptr = (Complex **)malloc(sizeof(Complex *)*n);
    for (int i = 0; i <n; i++)
    {
        ptr[i] = (Complex *)malloc(sizeof(Complex)*m);
    }
    return ptr;
}

Complex *** allocate3DComplexArray(int n, int m, int dof)
 {
     Complex *** ptr = (Complex ***)malloc(sizeof(Complex **)*n);
     for (int i = 0; i <n; i++)
     {
         ptr[i] = (Complex **)malloc(sizeof(Complex *)*m);
     
        for (int j = 0; j < m; j ++) {
          ptr[i][j] = (Complex *)malloc(sizeof(Complex)*dof);
       }
     }
        return ptr;
 }


void freeTwoDimenArray(double ** ptr, int row, int col)
{
    for(int i = 0; i < row; i++)
    {
        free(ptr[i]);
    }
    free(ptr);
}

void free2DComplexArray(Complex ** ptr, int n, int m)
{
    for (int i = 0; i < n; i++)
    {
        free(ptr[i]);
    }
    free(ptr);
}

void free3DComplexArray(Complex *** ptr, int n, int m)
 {
     for (int i = 0; i < n; i++)
     {
       for (int j = 0; j < m; j++) 
       {

         free(ptr[i][j]);
       }
       free(ptr[i]);
    }
     free(ptr);
 }
*/

int main ()
{
  int n = 2;
  int m = 2;
  int dof = 4;

  float mass = 0.01;

  Complex *** gauge = allocate3DComplexArray(n, m, dof); 
  Complex *** psi = allocate3DComplexArray(n, m, dof);
  Complex *** chi = allocate3DComplexArray(n, m, dof);

  if (!gauge && !psi && !chi)
  {
		cout << "Memory Allocation Failed" << endl;
		exit(1);
	}

  for (int i=0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      for (int k = 0; k < dof; k++) {
      gauge[i][j][k] = Complex(1.0,0.1);
      psi[i][j][k] = Complex(1.0,0.1);
      cout << psi[i][j][k] << gauge[i][j][k] << endl;
      }
    }
  } 
  
  coarseDpsi(chi, psi, gauge, n, m, dof, mass); 


   for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      for (int k = 0; k < dof; k++) {
      cout << chi[i][j][k] << endl;
      }
    }
  } 


  free3DComplexArray(gauge, m, n);
  free3DComplexArray(psi, m, n);
  free3DComplexArray(chi, m, n);
  return 0;
  
}
