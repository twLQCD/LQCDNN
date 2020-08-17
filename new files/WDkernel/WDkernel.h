#ifndef WDKERNEL_H
#define WDKERNEL_H

//#include <stdlib.h>
//#include <cmath>
//#include <complex>
//#include <iostream>
//using namespace std;

#include "common.h"

void Dpsi(Complex *** psi2, Complex *** psi1,
           Complex *** gauge, int nt, int nx, float m){
      
      double m0 = m;
      double  r = 1.0;
      double constant = (2*r + m0);
      int xp1, xm1, yp1, ym1;
 
    //Sum over 0,1 directions.
      for(int x=0; x< nx; x++) { 
        xp1 = (x+1) % nx;
        xm1 = (x - 1 + nx) % nx;
        for(int y=0; y < nt; y++) {
          yp1 = (y+1) % nt;
          ym1 = (y - 1 + nt) % nt;
   
          //upper
          psi2[x][y][0] = constant * psi1[x][y][0] -
  
      0.5*(     gauge[x][y][0]    * (r*psi1[xp1][y][0] - psi1[xp1][y][1]) +
           conj(gauge[xm1][y][0]) * (r*psi1[xm1][y][0] + psi1[xm1][y][1]) +
   
           gauge[x][y][1]    * (r*psi1[x][yp1][0] + Complex(0,1.0)*psi1[x][yp1][1]) +
           conj(gauge[x][ym1][1]) * (r*psi1[x][ym1][0] - Complex(0,1.0)*psi1[x][ym1][1]));
 
          //lower
            psi2[x][y][1] = constant * psi1[x][y][1] -
 
      0.5*(     gauge[x][y][0]    * (-psi1[xp1][y][0] + r*psi1[xp1][y][1]) -
           conj(gauge[xm1][y][0]) * (-psi1[xm1][y][0] - r*psi1[xm1][y][1]) +
   
           gauge[x][y][1]    * (-Complex(0,1.0)*psi1[x][yp1][0] + r*psi1[x][yp1][1]) -
           conj(gauge[x][ym1][1]) * (-Complex(0,1.0)*psi1[x][ym1][0] - r*psi1[x][ym1][1]));
 
 
      }
   }
}

void coarseDpsi(Complex *** psi2, Complex *** psi1,
           Complex *** gauge, int nt, int nx, int dof, float m){

      double m0 = m;
      double  r = 1.0;
      double constant = (2*r + m0);
      int xp1, xm1, yp1, ym1, dp1, dm1;

    //Sum over 0,1 directions.
      for(int x=0; x< nx; x++) {
        xp1 = (x+1) % nx;
        xm1 = (x - 1 + nx) % nx;
        for(int y=0; y < nt; y++) {
          yp1 = (y+1) % nt;
          ym1 = (y - 1 + nt) % nt;
          for (int k=0; k < (dof-1); k += 2) {
            dp1 = (k + 1) % dof;
            dm1 = (k - 1 + dof) % dof;

          //upper
          psi2[x][y][k] = constant * psi1[x][y][k] -

      0.5*(     gauge[x][y][k]    * (r*psi1[xp1][y][k] - psi1[xp1][y][dp1]) +
           conj(gauge[xm1][y][k]) * (r*psi1[xm1][y][k] + psi1[xm1][y][dp1]) +

           gauge[x][y][dp1]    * (r*psi1[x][yp1][k] - psi1[x][yp1][dp1]) +
           conj(gauge[x][ym1][dp1]) * (r*psi1[x][ym1][k] + psi1[x][ym1][dp1]));

          //lower
            psi2[x][y][dp1] = constant * psi1[x][y][dp1] -

      0.5*(     gauge[x][y][k]    * (-psi1[xp1][y][k] + r*psi1[xp1][y][dp1]) -
           conj(gauge[xm1][y][k]) * (-psi1[xm1][y][k] - r*psi1[xm1][y][dp1]) +

           gauge[x][y][dp1]    * (psi1[x][yp1][k] + r*psi1[x][yp1][dp1]) -
           conj(gauge[x][ym1][dp1]) * (psi1[x][ym1][k] - r*psi1[x][ym1][dp1]));


       }
    }
  }
}



#endif
