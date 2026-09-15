import numpy as np
import matplotlib.pyplot as plt



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


def squareplot(lrange, hrange, points, saveplot = False):
    """
    takes in low range, high range and number of points to plot over specified range as well as
    additional optional argument to save plot. From this information, function will plot results
    using given range against previous square function, optionally saving it according to input.

    Variables
    ---------------
    xarray: array, creates a array from arguments
    yarray: array, creates array using square function(with xarray as its argument to do so)
    
    Parameters
    ------------
    lrange: low range of points inputted, integer or float
    hrange: high range of points inputted, integer or float
    points: number of points desired in plot, integer

    Returns
    ---------
    no returns

    Other Parameters
    -----------------
    saveplot: additional optional argument used to name and save the plot created(automatically save as .pdf), string

    Raises
    -------
    lrange, hrange: will not take in strings, lists, or arrays
    saveplot: argument must be a string and cannot have an extension, extension already included(saved as .pdf)
    
    See Also
    -----------
    other functions used.
    Square: inputted arguments create array, 'arrayx', arrayx is used in the square function and its result is the array y, 'yarray',
    which it is then plotted.

    Notes
    ---------
    function creates array, so squareplot cannot take in array's.

    Example
    ----------------
    >>>squareplot(0, 10, 6, 'plot')
    >>>plot.pdf
    """
    #a) create x array of evenly spaced elements up to and including high range
    xarray = np.linspace(lrange, hrange, points)
    #b) call square function to create y array
    yarray = square(xarray)
    #c) plot
    plt.figure()
    plt.plot(xarray, yarray)
    plt.title('Square function')
    plt.xlabel('input')
    plt.ylabel('output')
    # save plot
    if saveplot is not False:
        plt.savefig(saveplot + ".pdf")
    plt.show()
    
    