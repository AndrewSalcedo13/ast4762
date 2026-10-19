import numpy as np


def skycormednorm(sub_obj_frame, norm_sky, region=None):
    """
    Subtracts a normalized sky frame from an object frame after
    restoring the sky frame to the appropriate brightness scale.

    Parameters
    ----------
    sub_obj_frame : array_like
        2D dark-subtracted object frame.

    norm_sky : array_like
        2D dark-subtracted, normalized sky frame.

    region : tuple, optional
        Coordinates of two opposite corners of the region used to
        calculate the normalization factor, specified as
        ((y1, x1), (y2, x2)). If None, the entire object frame is used.

    Returns
    -------
    sky_sub : ndarray
        2D array containing the object frame after sky subtraction.
    """
    if region is None:
        norm_factor = np.median(sub_obj_frame)
    else:
        (y1, x1), (y2, x2) = region
        norm_factor = np.median(sub_obj_frame[y1:y2, x1:x2])

    sky = norm_sky * norm_factor
    sky_sub = sub_obj_frame - sky

    return sky_sub


##################################################################

def normmedcomb(array3d, region = None):
    """
    Median-combines a 3D array of normalized images by first normalizing the images/data then finding the median value
    of each pixel across all exposures and combining into one 2-d array.

    Parameters
    ----------
    array3d : array_like
        3D array containing multiple images/exposures. The first
        dimension represents the different exposures, while the
        remaining two dimensions represent the image pixels.

    region : tuple, optional
        Tuple containing the coordinates of two opposite corners of
        the region used to calculate the normalization factor for
        each exposure. Specified as ((y1, x1), (y2, x2)). If None,
        the entire image is used to calculate the normalization factor.

    Returns
    -------
    norm_factors : list
        List containing the normalization factor calculated for each
        exposure using the median of the specified region or the
        entire image.

    master_flat : ndarray
        2D normalized, median-combined array containing the median
        value of each pixel across all normalized exposures.

    Examples
    --------
    >>> array3d = np.array([[[1, 2], [3, 4]],
    ...                     [[5, 6], [7, 8]],
    ...                     [[9, 10], [11, 12]]])
    >>> norm_factors, master_flat = normmedcomb(array3d)
    >>> print(norm_factors)
    [2.5, 6.5, 10.5]
    >>> print(master_flat)
    [[0.66666667 0.8       ]
     [0.92307692 1.        ]]
    """
    norm_factors = []        #empty array, to contain the normalization factors for each exposure
    norm_expos = []          #empty array, to containt all the normalized exposures(2d arrays)
    
    for i in range(array3d.shape[0]):      #loops through each exposure
        expo = array3d[i]                  #defines current exposure in loop
        if region is None:               
            norm_fact = np.median(expo)    #takes median of entire exposure(no selected region)
        else:
            (y1, x1), (y2, x2) = region
            norm_fact = np.median(expo[y1:y2, x1:x2])     #takes median of selected region of exposure
            
        norm_expo = expo / norm_fact       #normalizes exposure
        
        
        norm_factors.append(norm_fact)     #stores normalization factors for each exposure, corresponding to index
        norm_expos.append(norm_expo)       #stores normalized exposures, should be 3d array

    master_flat = np.median(norm_expos, axis=0)    #master flat, takes the median of all the now normalized exposures
    return norm_factors, master_flat
    

##################################################################

def window(time, center, width, height):
    '''
    The function defines a transit interval centered at `center` with
    the specified `width`. The normalized flux is set to `height` for
    observation times within the transit interval and to 1 outside it.

    Parameters
    ----------
    time : array_like
        Array containing the observation times in days.
    center : float
        Center of the transit window in days.
    width : float
        Total width of the transit window in days.
    height : float
        Normalized flux value within the transit window.

    Returns
    -------
    box_flux : ndarray
        Array of artificial normalized flux values, with values equal
        to `height` inside the transit window and 1 outside it.
    '''
    box_bool = ((center - width/2) < time) & (time < (center + width/2))     #boolean that defines transit window times
    box_flux = np.ones(len(time))                    #creates artificial normalized flux values for array
    box_flux[box_bool] = height                      #sets normalized flux values within defined transit window to the height to create box
    return box_flux

##################################################################

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

##################################################################