## Mars Rover

### Ques 1.1


Speed on sandy terrain = S(S) = 3 km/h,
Speed on smooth terrain = S(SM) = 5 km/h,
Speed on rocky terrain = S(R) = 2 km/h,

- Route 1

Distance = 2 km
Probability of sandy terrain = 0.2
Probability of smooth terrain = 0.3
Probability of rocky terrain = 0.5

- Route 2

Distance = 1.8 km
Probability of sandy terrain = 0.4
Probability of smooth terrain = 0.2
Probability of rocky terrain = 0.4

- Route 3

Distance = 3.1 km
Probability of sandy terrain = 0.5
Probability of smooth terrain = 0.4
Probability of rocky terrain = 0.1


- route 1 = 0.2 * 2/3 + 0.3 * 2/5 + 0.5 * 2/2 = 0.133 + 0.12 + 0.5 = 0.753 hours
- route 2 = 0.4 * 1.8/3 + 0.2 * 1.8/5 + 0.4 * 1.8/2 = 0.24 + 0.072 + 0.36 = 0.672 hours
- route 3 = 0.5 * 3.1/3 + 0.4 * 3.1/5 + 0.1 * 3.1/2 = 0.516 + 0.248 + 0.155 = 0.919 hours

Route 2 is the most optimal path.

### Ques 1.2

#### Next case: Crator and Bridge

#### The new probabilities for each route

- Route 1  = 0.3 \* 3/4 = 0.225 hours
- Route 2  = 0.6 \* 1 = 0.6 hours

#### The new expected time for each route

- route 1 = 0.753 + 0.225 = 0.978 hours
- route 2 = 0.672 + 0.6 = 1.272 hours
- route 3 = 0.919 hours

#### Ans 1.2 -  According to the new expected time, the best route is route 3. lowest expected time is  0.919 hours.

### Ques 1.3

#### Now suppose that we can use a satellite to find out whether the terrain in route 3 is smooth. Is this helpful? What is the value of this information? Expressed differently, how long are we willing to wait for this information from the satellite?

The estimated time for route 3 will be 3.1/5 = 0.62 hours if the terrain is smooth. This is shorter than what route 1 and route 2 were supposed to take. Therefore, it would be beneficial if we could utilize a satellite to determine whether route 3's topography is smooth. This data has a value of 0.919 - 0.62 = 0.299 hours. We are willing to wait 0.299 hours for this information from the satellite.

### Ques 1.4

#### Now put this problem into ChatGPT. Is it able to solve it correctly? If not, where does it make mistakes?

ChatGPT is inaccurate:

- The various route lengths are not taken into account. It solely takes the terrains' probabilities into account. Thus, it believes that route 2 is the optimal one.
- When asked how long we are willing to wait for information from the satellite, it is unable to provide an accurate response. We indicate that we are prepared to wait for a whole day. However, the right response is 0.299 hours.
