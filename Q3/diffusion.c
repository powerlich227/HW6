// C function to simulate the reflection from a surface that has mixed diffuse and specular reflection coefficients.
//    spec_prob is the probility of reflections that are specular
//    theta_in  is the angle to the normal of the surface in radians of the incident photon
//    phi_in    is the azimuth angle of the incident photon
//    theta_out is the angle to the normal of the surface of the reflectd photon
//    phi_out   is the azimuth angle of the reflected photon relative to phi_in
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "diffusion.h"

#define PI 3.1415926

// To return theta&phi together, using pointer
void diffusion(double spec_prob, double theta_in, double phi_in, double *theta_out, double *phi_out)
{
	double r1,r2,r3;
	// Check for specular reflection
	r1 = (double)random()/(double)RAND_MAX;
	if (r1 <= spec_prob)
	{
		*theta_out = theta_in;
		*phi_out = phi_in + PI;
		if (*phi_out >= 2.*PI) 
			*phi_out = *phi_out - 2.*PI;
		return;
	}
	// Not specular, then diffusion
	r2 = (double)random()/(double)RAND_MAX;
	*theta_out = acos(1.-2.*r2)/2.;
	r3 = (double)random()/(double)RAND_MAX;
  	*phi_out = 2.*PI*r3;
  	return;
}
