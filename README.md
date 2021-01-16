# Tully-FSSH-1990
Fortran Code for Tully's Molecular Dynamics with Electronic Transition 1990 paper
Md-Tully.f90 contains the code for Tully's seminal 1990 paper. 
To run the code simply use the following commands:
#gfortran Md-Tully.f90
#./a.out
Another parallelized version is also there. 
This can be run on a cluster if you have access to one.
The sub.sh file will be used to submit the job on the cluster which will then allocate nodes to the child code.
the command to do so is:
#qsub sub.sh
prior to submitting the code on the cluster make sure to compile the tully.f90 code using
#gfortran tully.f90
and run the python code parallelize.py as
#python3 parallelize.py
Both the codes will reproduce results for Tully's 1990 paper.
