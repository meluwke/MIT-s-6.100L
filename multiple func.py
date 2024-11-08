# -*- coding: utf-8 -*-
def multiple(*x):
    """
    Parameters
    ----------
    *x is tuple of integers

    Returns
    -------
    it multiples integers inside the tuple.

    """
    tot=1
    for i in x:
        tot*=i
    return tot
print(multiple(1,2,3,4))
