"""
         2208 function calls in 39.124 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100   39.102    0.391   39.102    0.391 nbody_iter.py:68(advance)
      100    0.012    0.000    0.012    0.000 {method 'send' of '_socket.socket' objects}
      200    0.002    0.000    0.018    0.000 iostream.py:309(write)
      100    0.002    0.000    0.020    0.000 {built-in method builtins.print}
      100    0.001    0.000    0.015    0.000 ioloop.py:932(add_callback)
      100    0.001    0.000    0.001    0.000 nbody_iter.py:99(report_energy)
      200    0.001    0.000    0.016    0.000 iostream.py:241(_schedule_flush)
        1    0.001    0.001   39.124   39.124 nbody_iter.py:136(nbody)
      100    0.001    0.000    0.001    0.000 stack_context.py:253(wrap)
      100    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
      200    0.000    0.000    0.001    0.000 iostream.py:228(_is_master_process)
      100    0.000    0.000    0.012    0.000 common.py:75(wake)
      200    0.000    0.000    0.000    0.000 {method 'write' of '_io.StringIO' objects}
      200    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
      200    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000   39.124   39.124 {built-in method builtins.exec}
      100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      100    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        1    0.000    0.000   39.124   39.124 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 nbody_iter.py:25(create)
        1    0.000    0.000    0.000    0.000 nbody_iter.py:118(offset_momentum)
        2    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
        
        
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    53                                           def advance(dict_local, Local_keys, pairs,dt,i):
    54                                               '''
    55                                                   advance the system one timestep
    56                                               '''
    57    100005       213826      2.1      0.5      for _ in range(i):
    58   1100000      2227571      2.0      5.3          for pair in pairs:
    59   1000000      2337722      2.3      5.6              ((x1, y1, z1), v1, m1) = dict_local[pair[0]]
    60   1000000      2291839      2.3      5.5              ((x2, y2, z2), v2, m2) = dict_local[pair[1]]
    61   1000000      2040544      2.0      4.9              dx = x1-x2
    62   1000000      1986708      2.0      4.8              dy = y1-y2
    63   1000000      1983802      2.0      4.8              dz = z1-z2
    64   1000000      3363218      3.4      8.1              mag = dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
    65                                                       ################
    66                                                       # add temp var #
    67                                                       ################
    68   1000000      2124555      2.1      5.1              temp1 = m1*mag
    69   1000000      2030174      2.0      4.9              temp2 = m2*mag
    70   1000000      2489374      2.5      6.0              v1[0] -= dx * temp2
    71   1000000      2520447      2.5      6.0              v1[1] -= dy * temp2
    72   1000000      2462499      2.5      5.9              v1[2] -= dz * temp2
    73   1000000      2535931      2.5      6.1              v2[0] += dx * temp1
    74   1000000      2495434      2.5      6.0              v2[1] += dy * temp1
    75   1000000      2407855      2.4      5.8              v2[2] += dz * temp1
    76                                           
    77    600000      1289095      2.1      3.1          for body in Local_keys:
    78    500000      1138239      2.3      2.7              (r, [vx, vy, vz], m) = dict_local[body]
    79    500000      1234132      2.5      3.0              r[0] += dt * vx
    80    500000      1243206      2.5      3.0              r[1] += dt * vy
    81    500000      1247988      2.5      3.0              r[2] += dt * vz
"""
# we can see that most of the time are spend in advance function

from itertools import combinations
from timeit import timeit
PI = 3.14159265358979323
SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

def create():
    '''
    Add a function that create the BODIES dictionary
    '''
    BODIES = {
        'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS),

        'jupiter': ([4.84143144246472090e+00,
                     -1.16032004402742839e+00,
                     -1.03622044471123109e-01],
                    [1.66007664274403694e-03 * DAYS_PER_YEAR,
                     7.69901118419740425e-03 * DAYS_PER_YEAR,
                     -6.90460016972063023e-05 * DAYS_PER_YEAR],
                    9.54791938424326609e-04 * SOLAR_MASS),

        'saturn': ([8.34336671824457987e+00,
                    4.12479856412430479e+00,
                    -4.03523417114321381e-01],
                   [-2.76742510726862411e-03 * DAYS_PER_YEAR,
                    4.99852801234917238e-03 * DAYS_PER_YEAR,
                    2.30417297573763929e-05 * DAYS_PER_YEAR],
                   2.85885980666130812e-04 * SOLAR_MASS),

        'uranus': ([1.28943695621391310e+01,
                    -1.51111514016986312e+01,
                    -2.23307578892655734e-01],
                   [2.96460137564761618e-03 * DAYS_PER_YEAR,
                    2.37847173959480950e-03 * DAYS_PER_YEAR,
                    -2.96589568540237556e-05 * DAYS_PER_YEAR],
                   4.36624404335156298e-05 * SOLAR_MASS),

        'neptune': ([1.53796971148509165e+01,
                     -2.59193146099879641e+01,
                     1.79258772950371181e-01],
                    [2.68067772490389322e-03 * DAYS_PER_YEAR,
                     1.62824170038242295e-03 * DAYS_PER_YEAR,
                     -9.51592254519715870e-05 * DAYS_PER_YEAR],
                    5.15138902046611451e-05 * SOLAR_MASS)}


    return BODIES


def advance(dict_local, Local_keys, pairs,dt,i):
    '''
        advance the system one timestep
    '''
    for _ in range(i):
        for pair in pairs:
            ((x1, y1, z1), v1, m1) = dict_local[pair[0]]
            ((x2, y2, z2), v2, m2) = dict_local[pair[1]]
            dx = x1-x2
            dy = y1-y2
            dz = z1-z2
            mag = dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
            ################
            # add temp var #
            ################
            temp1 = m1*mag
            temp2 = m2*mag
            v1[0] -= dx * temp2
            v1[1] -= dy * temp2
            v1[2] -= dz * temp2
            v2[0] += dx * temp1
            v2[1] += dy * temp1
            v2[2] += dz * temp1

        for body in Local_keys:
            (r, [vx, vy, vz], m) = dict_local[body]
            r[0] += dt * vx
            r[1] += dt * vy
            r[2] += dt * vz


def report_energy(dict_local, Local_keys,pairs,e=0.0):
    '''
        compute the energy and return it so that it can be printed
    '''
    for pair in pairs:
        ((x1, y1, z1), v1, m1) = dict_local[pair[0]]
        ((x2, y2, z2), v2, m2) = dict_local[pair[1]]
        dx = x1-x2
        dy = y1-y2
        dz = z1-z2
        e -= (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5)
        
    for body in Local_keys:
        (r, [vx, vy, vz], m) = dict_local[body]
        e += m * (vx * vx + vy * vy + vz * vz) / 2.
        
    return e

# add an input that take local_keys
def offset_momentum(dict_local, Local_keys, ref, px=0.0, py=0.0, pz=0.0):
    '''
        ref is the body in the center of the system
        offset values from this reference
    '''
   
    for body in Local_keys:
        (r, [vx, vy, vz], m) = dict_local[body]
        px -= vx * m
        py -= vy * m
        pz -= vz * m
        
    (r, v, m) = ref
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m


def nbody(loops, reference, iterations):
    '''
        nbody simulation
        loops - number of loops to run
        reference - body at center of system
        iterations - number of timesteps to advance
    '''
    
    dict_local = create()
    Local_keys = dict_local.keys()
    pairs = list(combinations(dict_local.keys(), 2))
    
    # Set up global state
    offset_momentum(dict_local, Local_keys,dict_local[reference])
    
    for _ in range(loops):
        advance(dict_local, Local_keys,pairs, 0.01,i=iterations)
        print(report_energy(dict_local, Local_keys,pairs))

if __name__ == '__main__':
    print(timeit(lambda:nbody(100, 'sun', 20000), number=1))

