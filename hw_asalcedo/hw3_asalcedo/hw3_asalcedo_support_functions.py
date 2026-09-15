import os
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import astropy.io.fits as fits


def square(array):
    """
    summary:
    takes in as input a scalar or array of any dimension or numerical type and
    returns its square

    Variables
    array : scalar or array
            function parameter
    array0 : scalaer or array
            function output
        
    Returns
    -------
    array0 : scalar or array

    Other Parameters
    ----------------
    no other paraneters

    Raises
    ------
    strings, lists:
        function does not intake strings or lists, will raise type error
    
    Examples
    --------
    >>> array1 = np.random.randint(1, 5, size=(1, 2, 3))
    >>> square(array1)
    >>> array([[[16,  4,  1],
                [ 1, 16, 16]]])
    >>> array2 = 5
    >>> square(array2)
    >>> 25
    """
    try:
        array0 = (array)**2                       #squares input/argument of function
    except TypeError:
        raise TypeError("Input not accepted")     #raises error if function is unable to square input/argument
    return array0


def squareplot(lrange, hrange, points, saveplot = false):
    """
    takes in low range, high range and number of points to plot over specified range as well as
    additional optional argument to save plot. From this information, function will plot results
    using given range against previous square function, optionally saving it according to input.

    Parameters
    ------------
    lrange: 
    hrange: 
    points: 
    saveplot: 

    Returns
    ---------
    what will function return: dtype, \n explanation

    Other Parameters
    -----------------
    confusing idk what this is supposed to mean, I think its none but idk

    Raises
    -------
    what wont work in this function
    saveplot argument cannot have extension, extension already included
    See Also
    -----------
    other function(square): relationship explanation
    """
    #a) create x array of evenly spaced elements up to and including high range
    xarray = np.linspace(lrange, hrange, points)
    #b) call square function to create y array
    yarray = square(xarray)
    #c) plot
    plt.figure()
    plt.plot(x, y)
    plt.title('Square function')
    plt.xlabel('x array')
    plt.ylabel('y array')
    # save plot
    if saveplot not false:
        plt.savefig(saveplot + ".pdf")
    plt.show()
    
    
    