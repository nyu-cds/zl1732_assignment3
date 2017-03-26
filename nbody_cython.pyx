
"""
    N-body simulation.
    In this version, combined all the improvement together.
    before: 46s
    after: 10s
"""

from timeit import timeit
import itertools as it
cdef float PI = 3.14159265358979323
cdef float SOLAR_MASS = 4 * PI * PI
cdef float DAYS_PER_YEAR = 365.24

cdef dict BODIES = {
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





# add inputs to avoid create local variable many times.
cpdef void advance(dict_local, Local_keys,dt,i):
    '''
        advance the system one timestep
    '''
    # move pairs out of the loop
    pairs = list(it.combinations(Local_keys, 2))
    
    # def float
    cdef float x1, x2, y1, y2, z1, z2, m1, m2, dx, dy, dz, mag, temp1, temp2, vx, vy, vz, m
    cdef list v1, v2, r
    
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


cpdef float report_energy(dict_local, Local_keys,e=0.0):
    '''
        compute the energy and return it so that it can be printed
    '''
    # Add the pairs in main function as a local variable instead of add them in each function
    pairs = it.combinations(dict_local.keys(), 2)
    
    # def float
    cdef float dx, dy, dz
    
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
cpdef void offset_momentum(dict_local, Local_keys, ref, px=0.0, py=0.0, pz=0.0):
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


cpdef void nbody(loops, reference, iterations):
    '''
        nbody simulation
        loops - number of loops to run
        reference - body at center of system
        iterations - number of timesteps to advance
    '''
    
    dict_local = BODIES
    Local_keys = dict_local.keys()
    
    # Set up global state
    offset_momentum(dict_local, Local_keys,dict_local[reference])

    for _ in range(loops):
        report_energy(dict_local, Local_keys)
        advance(dict_local, Local_keys,0.01,i=iterations)
        print(report_energy(dict_local, Local_keys))

if __name__ == '__main__':
    print(timeit(lambda:nbody(100, 'sun', 20000),number=1))