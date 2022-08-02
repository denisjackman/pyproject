# Notes on various things

## ELO rating
Ea is the probability of 'a' winning a match against 'b'.
The correct equations are:

Ea = 1 / (1 + 10 ^ ((Rb-Ra)/400) )
Eb = 1 / (1 + 10 ^ ((Ra-Rb)/400) )

Being two probabilities, Ea+Eb=1

Ra is the 'rating' of 'a'.
As Haseeb well explained, the rating changes after every match, according to this formula:

Ra(t+1) = Ra(t) + K * ( W - Ea )

where W=1 if 'a' wins / W=0 if 'a' loses.

The same for Rb.

t is time. At time+1, the new rating of A is the old rating of A plus a constant multiplied by the delta.

Ra(t+1) = new rating for A.
Ra(t) = previous rating for A.

K = constant  choose a lower number for more stable ratings, and a higher number for ratings that update more quickly.
(W - Ea) = the delta. The actual outcome W minus the expected outcome Ea.


Ea = 1 / (1 + 10 (Rb-Ra)/400 )
Eb = 1 / (1 + 10 (Ra-Rb)/400 )

## Reference
* [Wiki Definition](https://en.wikipedia.org/wiki/Elo_rating_system)
* [Geeks for geeks definition](https://www.geeksforgeeks.org/elo-rating-algorithm/)
