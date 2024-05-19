## Question 1
<details>
<summary><strong>Q:</strong> Suppose we have <code>N</code> items. We want to divide these <code>N</code> between three groups. Two groups should get the same amount of items. 
How can we divide the items so that the difference between the number of items dedicated to each group is minimal?</summary>
<be>
<strong>Idea:</strong> x + 2y = N 

=> diff = |y - x| = |(N - 3x)/2|

=> If `N` is even, `x` also should be even to have a natural `diff` value. And if `N` is odd, `x` also should be odd to have a natural `diff` value. 

= > Based on `N`, create the list of possible `x` values, calculate the `diff` values for each `x`, and then find the minimum of `diff` values. Then you can find the associated `x` and calculate the `y` value. 
</details>
