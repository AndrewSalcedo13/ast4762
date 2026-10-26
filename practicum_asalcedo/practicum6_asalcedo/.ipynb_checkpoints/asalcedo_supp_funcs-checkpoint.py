import numpy as np
import os
from astropy.io import fits

def filefind(datadir, fext, fname, load_data = False):
    """
    Finds files in a specified directory whose names contain a given
    substring and returns a list of matching filenames. This was made with .fits files in mind(especially the load data) argument

    Parameters
    ----------
    datadir : str
        Directory containing the files to be searched.

    fext : str
        File extension to be removed from the matching filenames,
        such as '.fits'.

    fname : str
        Substring used to identify relevant files. Any filename
        containing this substring will be included in the list.
    load_data : bool, optional
        If True, load the matching FITS files into a 3D data cube.
        Defaults to False.

    Returns
    -------
    files : list
        List of matching filenames with the specified extension
        removed. The filenames do not include the directory path.
    data_cube : ndarray, optional
        3D array containing the image data from each matching FITS
        file. Returned only when load_data is True.

    Examples
    --------
    >>> files = filefind('hw6_data/', '.fits', 'stars_13s_', load_data = True)
    >>> print(files[0])
    ['stars_13s_1', 'stars_13s_2', 'stars_13s_3']
    """
    #Loops through previously determined directory and appends all relevant files to array according to file name given
    files = []
    for i in os.listdir(datadir):
        if fname in i:
            files.append(i.replace(fext, ""))
    
    #Printing informative statements on files being searched for
    print(f"\nData Directory: {datadir}")
    print(f"Extension: {fext}")
    print(f"File name: {fname}")
    print(f"Last element in {fname} file: {files[-1]}")
    
    #Defines the rows and columns of the fits files
    ny, nx = fits.getdata(os.path.join(datadir + files[0] + fext)).shape
    nfiles = len(files)
    
    #Informative statements on the first file and the number of files
    print(f"Number of rows in the first {fname} file image: {ny}")
    print(f"Number of elements/colummns in row 1 of the first {fname }file: {nx}")
    print(f"Number of {fname} files: {nfiles}")

    #Optional fourth argument: Returning the files as a datacube
    if load_data:
        data_cube = np.zeros((nfiles, ny, nx), dtype=np.float64)
        for i in range(nfiles):
            data_cube[i] = fits.getdata(os.path.join(datadir + files[i] + fext))
            filehead = fits.getheader(os.path.join(datadir + files[i] + fext))
        return files, data_cube
    else:
        return files
    

##################################################################

def disk(radius, center, shape):
    """
    Creates a 2D Boolean mask in the shape of a disk by determining
    which pixel centers fall within a specified radius of the disk center.

    Parameters
    ----------
    radius : float
        Radius of the disk in pixels.

    center : array_like, tuple
        Coordinates of the disk center, specified as (y, x). The
        coordinates may be fractional.

    shape : array_like, tuple
        Dimensions of the 2D mask, specified as (ny, nx), where ny
        is the number of rows and nx is the number of columns.

    Returns
    -------
    dmask : ndarray
        2D Boolean array with the specified shape. Pixels whose centers
        are within or on the specified radius of the disk center are
        True, and all other pixels are False.

    Examples
    --------
    >>> dmask = disk(6.2, (12.3, 14.5), (25, 30))
    >>> print(dmask.shape)
    (25, 30)
    >>> print(dmask.dtype)
    bool
    """
    y_c, x_c = center
    y, x = np.indices(shape)             #creates an array the same shape as the given input to help calculate individual pixel distances
    dist = ((y-y_c)**2+(x-x_c)**2)**0.5  #Calculates the distance of individual pixel from center
    dmask = (dist <= radius)             #Creates boolean array/mask to define the disk shaped mask
    return dmask

##################################################################

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