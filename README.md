## Question 1: The best possible items distribution. 
<details>
<summary><strong>Q:</strong> Suppose we have <code>N</code> items. We want to divide these <code>N</code> between three groups. Two groups should get the same amount of items. 
How can we divide the items so that the difference between the number of items dedicated to each group is minimal?</summary>
<be>
<strong>Idea:</strong> x + 2y = N 

=> diff = |y - x| = |(N - 3x)/2|

=> If `N` is even, `x` also should be even to have a natural `diff` value. And if `N` is odd, `x` also should be odd to have a natural `diff` value. 

= > Based on `N`, create the list of possible `x` values, calculate the `diff` values for each `x`, and then find the minimum of `diff` values. Then you can find the associated `x` and calculate the `y` value. 
</details>


## Question 2: Compound Interest Rate 
<details>
<summary><strong>Q:</strong> Suppose we have <code>P0</code> dollars. We also have a saving account in a bank that proposes <code>r%</code> annual interest compounded every <code>1/n</code> period in a year (for example, every month becomes <code>1/12</code>). At the end of each period, we add <code>P</code> dollars to the account. After <code>t</code> years, how much money will we have? </summary>
<be>
<strong>Idea:</strong> 
  We can find the formula to find the final value by writing the value of our money step by step. We should consider that, at the end of each period, an interest of <code>r/n</code> is applied to our money. So: 
  
  ```
0 --> P0
1 --> P0 + (r/n)P0 + P = (1+r/n)P0 + P
2 --> (1+r/n)P0 + P + (r/n)[(1+r/n)P0 + P] + P = (1+r/n)^2.P0 + [(1+r/n) + 1]P
3 --> (1+r/n)^2.P0 + [(1+r/n) + 1]P + (r/n)[(1+r/n)^2.P0 + [(1+r/n) + 1]P] + P = (1+r/n)^3.P0 + [(1+r/n)^2 + (1+r/n) + 1]P
.
.
.
nt --> ... = (1+r/n)^(nt).P0 + [(1+r/n)^(nt) + (1+r/n)^(nt - 1) + ... + (1+r/n)^2 + (1+r/n) + 1]P
  ```

So, we should write a code that calculates the final coefficients of <code>P0</code> and <code>P</code> to calculate the final value!
</details>

## Question 3: Mean Dwell Time 
<details>
<summary><strong>Q:</strong> Suppose we have a sequence of different states (shown by numbers). Calculate the mean time that the system stays in each specific state. </summary>
<be>

</details>
