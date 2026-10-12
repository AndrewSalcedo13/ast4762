import numpy as np

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