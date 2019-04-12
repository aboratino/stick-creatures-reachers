# stick-creatures-reachers

Simulates an evolving population of segmented lifeforms.
They learn to reach a moving target using a genetic algorithm.  
Uses pygame for graphics

Example video on Youtube: https://www.youtube.com/watch?v=u0o51vhbfmU

Each stick creature consists of a chain of segments that are able to
rotate from their base.

Breeding occurs after each screen update.  The winner is chosen from 
the population based on whichever creature in the population's endpoint
is closest to the target.

Breeding consists of averaging out the rotation and rotation rates of each
segment and then applying a chance of mutation to those values to achieve
evolution.

Anthony Boratino 2013-1019
