#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "diffusion.h"

#define PI 3.1415926
#define rand_num 1000000
#define degree_step_theta 5
#define degree_step_phi 20
#define spec_prob 0.1

FILE *ostream1;
FILE *ostream2;

int main()
{
	int i,j,k;
	int itheta=0, iphi=0;
	double theta_in,phi_in,theta_out,phi_out;
	int theta_bin=90/degree_step_theta, phi_bin=360/degree_step_phi;
	double step_thetaout=PI*5./180.,step_phiout=PI*20./180.;
	int thetaout[17]={0},phiout[17]={0};//variable sized object may not be initialized
	double theta_out0[theta_bin],theta_out30[theta_bin],theta_out60[theta_bin],phi_out45[phi_bin];

	for(i=0; i<=rand_num; i++)
	{
		theta_in = PI*0.;
		phi_in = 0;
		diffusion(spec_prob,theta_in,phi_in,&theta_out,&phi_out);
		itheta=(int)(theta_out/step_thetaout);
		if(itheta<=theta_bin)
			theta_out0[itheta]++;

		theta_in = PI*30./180.;
		diffusion(spec_prob,theta_in,phi_in,&theta_out,&phi_out);
		itheta=(int)(theta_out/step_thetaout);
		if(itheta<=theta_bin)
			theta_out30[itheta]++;

		theta_in = PI*60./180.;
		diffusion(spec_prob,theta_in,phi_in,&theta_out,&phi_out);
		itheta=(int)(theta_out/step_thetaout);
		if(itheta<=theta_bin)
			theta_out60[itheta]++;

		theta_in = PI*45./180.;
		phi_in = PI;
		diffusion(spec_prob,theta_in,phi_in,&theta_out,&phi_out);
		iphi=(int)(phi_out/step_phiout);
		if(iphi<=phi_bin)
			phi_out45[iphi]++;
	}

	ostream1 = fopen("hmwk5c_problem1a.dat","w");
	for(j=0; j<theta_bin; j++)
	{
		thetaout[j+1]=thetaout[j]+5;
		fprintf(ostream1,"%d %f %f %f\n",thetaout[j],theta_out0[j]/rand_num,theta_out30[j]/rand_num,theta_out60[j]/rand_num);
	}

	ostream2 = fopen("hmwk5c_problem1b.dat","w");
	for(k=0; k<phi_bin; k++)
	{	
		phiout[k+1]=phiout[k]+20;
		fprintf(ostream2,"%d %f\n",phiout[k],phi_out45[k]/rand_num);
	}
	fclose(ostream1);
	fclose(ostream2);
	return 0;
}
