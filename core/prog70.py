# Reusing module(1).
import prog69
prog69.add(10,20)
prog69.sub(10,20)

# Reusing module(2).
import prog69 as ar
ar.add(10,20)
ar.sub(10,20)

# Reusing module(3).
from prog69 import*
add(10,20)
sub(10,20)
