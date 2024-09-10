def simple_intrest(p, n, r):
    """
    This function takes Principal, Numbers of years and Rate of Intrest as inpput
    Output Simple Intrest with amount
    """
    I = (p*n*r)/100
    A = p + I
    return I, A

if __name__=="__main__":
    I1, A1 = simple_intrest(p=57000, n=5, r=7.5)
    print(f"Simple Intrest : {I1:.2f}")
    print(f"Amount : {A1:.2f}")
    


