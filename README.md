## Question 1 (Q1)
**Q:** Suppose we have `N` items. We want to divide these `N` between three groups. Two groups should get the same amount of items. 
How can we divide the items so that the difference between the number of items dedicated to each group is minimal?

**Idea:** x + 2y = N 

=> diff = |y - x| = |(N - 3x)/2|

=> If `N` is even, `x` also should be even to have a natural `diff` value. And if `N` is odd, `x` also should be odd to have a natural `diff` value. 

= > Based on `N`, create the list of possible `x` values, calculate the `diff` value, and then find the minimum of `diff` values. Then you can calculate the `y` value too. 
