from mpi4py import MPI

#create COMM_WORLD object
comm = MPI.COMM_WORLD

#get_rank method
rank = comm.Get_rank()

#even rank
if rank%2 == 0:
    print('Hello from process '+str(rank))

#odd rank
else:
    print('Goodbye from process '+str(rank))