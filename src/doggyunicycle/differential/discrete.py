## Code for hw00
#
# David Fowler 8/26/2026
#

def diff(TimeValue,SignalValue):
    """
    Calculate the discrete derivative of a timeseries data
    
    w
    
    formula = [x(t(k)) - x(t(k-1))] / [t(k)-t(k-1)]
    
    Args:
        t (array) Time array
        x (array) Signal value with respect to the time array
        k (int) Position of the term to find
        
    Returns:
        array: The discrete derivative of the signal values
        
    Raises:
        ValueError: Time and signal arrays must be same size
        ValueError: Time and signal arrays must have size > 1
    
    Examples:
        Nothing rn
    
    """
    
    
    if len(TimeValue) != len(SignalValue):
        raise ValueError("Time and Signal array must share size")

    if len(TimeValue) < 2:
        raise ValueError("Time and Signal array must have size > 1")



    DiscreteDerivative = []
    
    for i in range(1,len(TimeValue),1):
        
        DiscreteDerivative.append(round(((SignalValue[i])-(SignalValue[i-1]))/(TimeValue[i]-TimeValue[i-1]), 3))
        
    return(DiscreteDerivative)