import numpy as np

def sigrej(data, rej_lim, boo_mask = None ):
    """
    Filters data values according to given range of standard deviations

    Parameters
    ----------
    data : array_like
        Array containing the data/values
    rej_lim : tuple of float
        Tuple with number of standard deviations to use for each iteration.
        The length of the tuple is the number of iterations performed.
    boo_mask : array_like of bool, optional
        Boolean mask that matches shape of the data, determining good(True) and bad(falso) data points
        accroding to rej_limit provided. If not provided, all data points are initially considered good.

    Returns
    -------
    boo_mask : ndarray of bool
        Updated Boolean mask that matches the shape of data, where True indicates a
        data point that passed all rejection iterations and False indicates
        a data point that was rejected or was initially identified as bad.

    Examples
    --------
    >>> data = np.array([1, 2, 3, 5, 7, 8, 9, 30, 60])
    >>> mask = sigrej(data, (2,1))
    >>> print(mask)
    iteration: 0, rej_lim = 2
    mean = 13.88888888888889
    std = 18.24794931823814

    iteration: 1, rej_lim = 1
    mean = 8.125
    std = 8.695365144719341

    [ True  True  True  True  True  True  True False False]
    """
    
    if boo_mask is None:
        boo_mask = np.ones(data.shape, dtype = bool)    #If no Boolean mask is provided one is created, keep/reject record

    for i in range(len(rej_lim)):                       
        good_data = data[boo_mask]                      #Contains only true(good) values from data, signified by boo_mask
        data_mean = np.mean(good_data)
        data_std = np.std(good_data)

        lower_lim = data_mean - (rej_lim[i] * data_std)
        upper_lim = data_mean + (rej_lim[i] * data_std)

        print(f"iteration: {i}, rej_lim = {rej_lim[i]}")
        print(f"mean = {data_mean}")
        print(f"std = {data_std}\n")
        

        boo_mask_update = (lower_lim <= data) & (data <= upper_lim)   #determines which values from original array fit within range (boolean)
        boo_mask = boo_mask_update & boo_mask                         #updated boolean mask containing orignal bad values and new ones(boolean)

    return boo_mask
    