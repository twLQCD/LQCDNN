#ifndef COMMON_H
#define COMMON_H

#include <stdlib.h>
#include <iostream>
#include <complex>
#include <cmath>
using namespace std;

typedef complex<double> Complex;
#define I Complex(0,1.0);

void random_init(Complex ** array, int n, int m)
{

  for (int i=0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      array[i][j] = polar(1.0,sqrt(1.0/6.0)*(double(rand())/ (RAND_MAX)));
    }
  }
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


#endif
