# =============================================================================
# Create your own implementation of a built-in function range, named in_range(), 
# which takes three parameters: `start`, `end`, and optional step. Tips: See the 
# documentation for `range` function
# =============================================================================

def in_range(finish, start=0, step=1):
    if start != 0:
        finish, start = start, finish
    
    if (start > finish and step > 0) or (start < finish and step < 0):
        return None
    elif start == finish:
        return start
    
    while start < finish:
        yield start
        start += step
            

for i in in_range(0, 6, 3):
    print(i)
    
    