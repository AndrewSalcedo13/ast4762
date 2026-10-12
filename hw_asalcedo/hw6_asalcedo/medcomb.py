import numpy as np

def medcomb(array3d):
    """
    Median-combines a 3D array of images by finding the median value
    of each pixel across all exposures.

    Parameters
    ----------
    array3d : array_like
        3D array containing multiple images/exposures. The first
        dimension represents the different exposures, while the
        remaining two dimensions represent the image pixels.

    Returns
    -------
    comb_arr : ndarray
        2D median-combined array containing the median value of each
        pixel across all exposures.

    Examples
    --------
    >>> array3d = np.array([[[1, 2], [3, 4]],
    ...                     [[5, 6], [7, 8]],
    ...                     [[9, 10], [11, 12]]])
    >>> comb_arr = medcomb(array3d)
    >>> print(comb_arr)
    [[5. 6.]
     [7. 8.]]
    """
    comb_arr = np.median(array3d, axis = 0)
    return comb_arr
    