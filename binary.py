from itertools import permutations
def zbits(n,k):
    '''
    1, Import the permutations tool from itertools
   
    2, check the correctness of n and k
      1) check both inputs are not string or other types
      2) check both inputs are integers
      3) check both inputs are positive
      4) ensure that n is greater than k
    
    3, use the permutations to create 0-1 strings and store
    them in a result, which is a set(),noted that permutations
    create some items that are the same, but set() won't add 
    the duplicate items.
    '''
    # ===============
    # check n and k
    # ===============
    try:
        int(n) and int(k)
    except:
        raise ValueError("one or both of the input are not number!")
        
    if int(n)!=n or int(k)!=k:
        raise ValueError("intput should be int! no float allowed!")
    
    if n<0 or k<0:
        raise ValueError("input should be positive!")
        
    if n<k:
        raise ValueError("n should be greater than k!")
        
    # ====================
    # create permutations
    # ====================
    result = set()
    database = "1"*(n-k)+"0"*k
    
    for item in permutations(database, n):
        result.add(''.join(item))
    
    return result

def main():
    assert zbits(4, 3) == {'0100', '0001', '0010', '1000'}
    assert zbits(4, 1) == {'0111', '1011', '1101', '1110'}
    assert zbits(5, 4) == {'00001', '00100', '01000', '10000', '00010'}
    
if __name__ == '__main__':
    main()