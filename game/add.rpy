label time_forward_h(delay):
    
    $ TimeCounter += delay
    if delay > 24:
        $ renpy.display_notify("Error!To much time hop in hours!")
        
    if TimeCounter > 24:
        $ TimeCounter -= 24
        $ DayCounter += 1
    return