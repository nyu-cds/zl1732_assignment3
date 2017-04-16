from mpi4py import MPI
import numpy as np

#create COMM_WORLD object
comm = MPI.COMM_WORLD

#get_rank method
rank = comm.Get_rank()

#get size
size = comm.Get_size()

#internal value, need to be checked
rank_val = np.zeros(1)

#start the process, check input it should be 
#1,integer
#2,less than 100
if rank == 0:
    #initial step at rank 0
    while (True):
        input_val = input('input an integer less than 100:')
        # check integer
        try: 
            rank_val[0]=int(input_val)
        except ValueError as error:
            print(error)
            continue
        #check value
        if rank_val[0]<100:
            break
        else:
            print("input should be less than 100")

    #final step at rank 0, recieve value
    comm.Send(rank_val, dest=1)
    comm.Recv(rank_val, source=size-1)
    #receieve from the last rank
    print("result = %d"  % (int(rank_val[0])))

#middle step: send buffer number to rank+1
if rank>0 and rank<size-1:
    comm.Recv(rank_val, source=rank-1)
    rank_val = rank_val*rank
    comm.Send(rank_val, dest=rank+1)
    
#final step, send back to process 0
elif rank==size-1:
    comm.Recv(rank_val, source=rank-1)
    rank_val = rank_val*rank
    comm.Send(rank_val, dest=0)