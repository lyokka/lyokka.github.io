---
layout: splash
title: Probability 2 The Binomial Theorem & The Multinomial Theorem
permalink: /prob2/
---
# Probability 2 The Binomial Theorem & The Multinomial Theorem

If you are not familiar with ``permutation`` and ``combination``, please read [this](/prob1/) first.

## The Binomial Theorem
### Theorem:
>$$
\begin{align*}
  (x+y)^n = \sum_{k=0}^{n} \left( \begin{array}{c} n \\ k \end{array} \right) x^k y^{n-k}
\end{align*}
$$

### Proof:
>$$
\begin{align*}
  (x+y)^n = \overbrace{
    (x+y) \cdot (x+y) \cdot(x+y) ... (x+y) \cdot (x+y)
   }^\text{n}
\end{align*}
$$

For example if we want to get the coefficient of $$x^4 y^{n-4}$$, we must select four $$(x+y)$$ to generate $$x^4$$, and the rest to generate $$y^{n-4}$$.

$$
\begin{align*}
\overbrace{
    (x+y) \cdot (x+y) \cdot (x+y) \cdot (x+y)}^\text{selected 4} \cdot
\overbrace{ (x+y) \cdot (x+y) ... (x+y)
   }^\text{rest n-4}
\end{align*}
$$

This is selecting $$4$$ objects from $$n$$, so the coefficient of $$x^4 y^{n-4}$$ is $$\left( \begin{array}{c} n \\ 4 \end{array} \right)$$.

Thus, for term $$x^k y^{n-k}$$, it's coefficient is $$\left( \begin{array}{c} n \\ k \end{array} \right)$$

>$$
\begin{align*}
  (x+y)^n &= \overbrace{
    (x+y) \cdot (x+y) \cdot(x+y) ... (x+y) \cdot (x+y)
   }^\text{n} \\
   \\
   &= C_0 x^n y^0 + C_1 x^{n-1} y + C_2 x^{n-2} y^2 + ... + C_{n-1} x y^{n-1} + C_n x^0 y^n \\
   \\
   &= \left( \begin{array}{c} n \\ n \end{array} \right) x^n y^0 +
    \left( \begin{array}{c} n \\ n-1 \end{array} \right) x^{n-1} y +
     \left( \begin{array}{c} n \\ n-2 \end{array} \right) x^{n-2} y^2 +
      ... +
       \left( \begin{array}{c} n \\ 1 \end{array} \right) x y^{n-1} +
        \left( \begin{array}{c} n \\ 0 \end{array} \right) x^0 y^n \\
        \\
  &= \sum_{k=0}^{n} \left( \begin{array}{c} n \\ k \end{array} \right) x^k y^{n-k}  
\end{align*}
$$

### Useful Compendium:
Since we've already proofed
>$$
\begin{align*}
  (x+y)^n = \sum_{k=0}^{n} \left( \begin{array}{c} n \\ k \end{array} \right) x^k y^{n-k}
\end{align*}
$$

If we set $$x = y = 1$$, we will get
>$$
\begin{align*}
  2^n = \sum_{k=0}^{n} \left( \begin{array}{c} n \\ k \end{array} \right)
\end{align*}
$$

### Example:
If we have a set of $$n$$ elements, how many subsets are there?
### Explanation:
If there are n elements in a set, there will be $$\left( \begin{array}{c} n \\ 1 \end{array} \right)$$ subset consist with 1 element, $$\left( \begin{array}{c} n \\ 2 \end{array} \right)$$ subset consist with 2 elements, so on so forth. Since empty set and the set itself are also the subset.

The total number of subsets of $$n$$ elements set is
>$$
\begin{align*}
  \left( \begin{array}{c} n \\ n \end{array} \right) +
  \left( \begin{array}{c} n \\ n-1 \end{array} \right) +
  \left( \begin{array}{c} n \\ n-2 \end{array} \right) +
   ... +
    \left( \begin{array}{c} n \\ 1 \end{array} \right) +
     \left( \begin{array}{c} n \\ 0 \end{array} \right)
      = \sum_{k=0}^{n} \left( \begin{array}{c} n \\ k \end{array} \right) = 2^n
\end{align*}
$$

## The Multinomial Coefficients
### Example:
We want to divided a $$n$$ distinct objects in to $$r$$ groups, so that *group 1* has $$n_1$$ objects, *group 2* has $$n_2$$ objects, so on so forth, *group r* has $$n_r$$ objects. How many possible divisions are possible?


$$
\begin{align*}
  \overbrace{
    Obj_1, Obj_2, Obj_3 ... Obj_{n-1}, Obj_n
   }^{n} &\rightarrow \overbrace{
     Group_1
    }^{n_1} , \overbrace{
      Group_2
     }^{n_2}, ...
     \overbrace{
       Group_r
      }^{n_r} \\
  n = n_1 + n_2 + .. + n_r &= \sum_{k=1}^{k=r} n_k
\end{align*}
$$

### Explanation:

To solve this problem, we can select $$n_1$$ from $$n$$ as *group 1*, there are $$\left( \begin{array}{c} n \\ n_1 \end{array} \right)$$ possible ways; then we can select $$n_2$$ from rest $$n - n_1$$ as *group 2*, there are $$\left( \begin{array}{c} n - n_1 \\ n_2 \end{array} \right)$$ possible ways, then we use same strategy to select objects till *group r*. Finally, we got

> $$
\begin{align*}
  \overbrace{
    \left(
      \begin{array}{c}
        n \\ n_1 \end{array}
    \right)}^\text{group 1}
  &\cdot \overbrace{\left( \begin{array}{c} n - n_1 \\ n_2 \end{array} \right)}^\text{group 2}
  \cdot \overbrace{\left( \begin{array}{c} n - n_1 - n_2 \\ n_3 \end{array} \right)}^\text{group 3} ...
   \overbrace{\left( \begin{array}{c} n - n_1 - n_2 - ... - n_{r-1} \\ n_r \end{array} \right)}^\text{group r} \\
   = \frac{n!}{n_1!(n-n_1)!} &\cdot \frac{(n-n_1)!}{n_2!(n-n_1-n_2)!} \cdot \frac{(n-n_1-n_2)!}{n_3!(n-n_1-n_2-n_3)!} ... \frac{(n-n_1-... -n_{r-1})!}{n_r!  \;\;\;\; [(n-n_1-...-n_{r-1} - n_r)! ]\leftarrow {\color{red}{0!}}} \\
   = \frac{n!}{n_1! n_2! ... n_r!}
\end{align*}
$$

### Definition:
The possible ways to divided $$n$$ different objects into $$r$$ distinct groups, with $$n_k$$ objects in $$k^{th}$$ group, are

>$$
\begin{align*}
    \frac{n!}{n_1! n_2! ... n_r!} = \left( \begin{array}{c} n \\ n_1, n_2, ..., n_r \end{array} \right)
\end{align*}
$$

This is known as ``mutinomial coefficient``.

## The Multinomial Theorem
### Theorem
>$$
\begin{align*}
  (x_1+x_2+...+x_r)^n &= \sum \left( \begin{array}{c} n \\ n_1,n_2,...,n_r \end{array} \right) x_1^{n_1} x_2^{n_2} ... x_r^{n_r} \\
  \text{with } n &= n_1 + n_2 + ... + n_r
\end{align*}
$$

### Proof
We use similar strategy as implemented in proofing Binomial Theorem. For example, if we want to calculate the coefficient of term $$x_1^{n-2} x_2^{1} x_3^{1} x_4^0...x_r^{0}$$. We need to separate $$(x_1+x_2+x_3+...+x_r)^n$$ like this:

$$
\begin{align*}
(x_1+x_2+x_3+...+x_r)^n &= (\sum_{k=1}^{r} x_k)^n\\
\overbrace{
    \sum_{k=1}^{r} x_k \cdot \sum_{k=1}^{r} x_k ... \sum_{k=1}^{r} x_k}^{\text{Group to generate }x_1^{n-2}} &\cdot
\overbrace{ \sum_{k=1}^{r} x_k
   }^{\text{Group to generate } x_2^1} \cdot
   \overbrace{ \sum_{k=1}^{r} x_k
      }^{\text{Group to generate } x_3^1}
\end{align*}
$$

We have totally $$\left( \begin{array}{c} n \\ n -2 ,1,1,0,...,0 \end{array} \right)$$ ways to generate term $$x_1^{n-2} x_2^{1} x_3^{1} x_4^0...x_r^{0}$$, so its coefficient is $$\left( \begin{array}{c} n \\ n -2 ,1,1,0,...,0 \end{array} \right)$$.

Therefore,

>$$
\begin{align*}
(x_1+x_2+x_3+...+x_r)^n &= (\sum_{k=1}^{r} x_k)^n\\
&= (\sum_{k=1}^{r} x_k) \cdot (\sum_{k=1}^{r} x_k) ... (\sum_{k=1}^{r} x_k)\\
&= C_0 x_1^{n} x_2^{0}...x_r^{0} + C_1 x_1^{n-1} x_2^{1}...x_r^{0} + ... + \overbrace{C_m x_1^{0} x_2^{0}...x_r^{n}}^{\text{just use } C_m \text{to denote the coefficient of this term}} \\
&= \left( \begin{array}{c} n \\ n,0,...,0 \end{array} \right) x_1^{n} x_2^{0}...x_r^{0} + \left( \begin{array}{c} n \\ n-1,1,...,0 \end{array} \right) x_1^{n-1} x_2^{1}...x_r^{0} + ... + \left( \begin{array}{c} n \\ 0,0,...,n \end{array} \right) x_1^{0} x_2^{0}...x_r^{n}
\end{align*}
$$

### Example
How many terms are there in $$(x_1+x_2...+x_r)^n$$ after expansion?

### Explanation

After expansion

$$
(x_1+x_2+...x_r)^n = C_0 x_1^{n} x_2^{0}...x_r^{0} + C_1 x_1^{n-1} x_2^{1}...x_r^{0} + ... + C_m x_1^{0} x_2^{0}...x_r^{n}
$$

The general form of each term is

$$
C x_1^{n_1} x_2^{n_2} x_3^{n_3} ... x_r^{n_r} \text{ with } n = n_1+n_2 +...+n_r \text{ and } n_k \text{ is non-negative integer for } k \in [0,r]
$$

So our goal is to calculate the number of all non-negative integer solutions of $$n=n_1+n_2+...+n_r$$

, since each solution corresponding to a unique term. To be more clear,

$$n_1 = 2, n_2 = 3, n_3 = n-8, n_4 = 3, ..., n_r = 0$$,

is a sample solution of $$\sum_{k=1}^{r} n_k = n$$, which corresponding to term $$C x_1^{2} x_2^{3} x_3^{n-8} x_4^{3} x_5^{0} ... x_r^{0}$$.

### Subproblem
In order to calculate the number of all non-negative integer solutions, let's calculate the number of all positive solutions first. Then the problem become $$n = a_1 + a_2 + ... + a_r$$ where $$a_k $$ is a positive integer.

Let's consider a positive number $$n$$ is
$$
n = \overbrace{1 + 1 + 1 + 1 + ... + 1 + 1}^{n}
$$

and a sample positive integer solution is

$$
n = \overbrace{1 + 1 }^{a_1 = 2} + \overbrace{1 + 1+ 1}^{a_2 = 3} + \overbrace{1 + 1}^{a_3=2}+\overbrace{1+1+1+...+1}^{a_4=n-r-3} + \underbrace{\overbrace{1}^{a_5=1}+\overbrace{1}^{a_6=1}+...+\overbrace{1}^{a_r=1}}_{(r - 4)\text{ 1s}}
$$

We can verify it is a valid solution:

$$
a_1+a_2+a_3+a_4+...+a_r = 2 + 3 + 2 + n-r-3 + (r-4) \cdot 1 = n \\
$$

In order to generate $$r$$ positive integers which are valid solutions, we can generate a positive integer solution by inserting $$r-1$$ dividing bars into $$1$$s. Like the sample solution above:

$$
\overbrace{1, 1}^{a_1 = 2}, | \overbrace{1,1,1}^{a_2 = 3},|\overbrace{1, 1}^{a_3=2},|\overbrace{1,1,1...,1}^{a_4=n-r-3},| \underbrace{\overbrace{1}^{a_5=1},|\overbrace{1}^{a_6=1},|...,|\overbrace{1}^{a_r=1}}_{(r - 4)\text{ 1s}}
$$

There are $$n-1$$ positions in those $$1$$s, so we can select $$r-1$$ positions to insert bars. Each selection is a solution for $$\sum_{k=1}^{r} a_k = n$$. Therefore, there are $$\left( \begin{array}{c} n-1 \\ r-1 \end{array} \right)$$ possible positive integer solutions.

### Back to The Number of Terms in $$(x_1+x_2...+x_r)^n$$

We proof that the number of **positive integer solutions** of $$a_1 + a_2 + a_3 + ... + a_r = n$$ is $$\left( \begin{array}{c} n-1 \\ r-1 \end{array} \right)$$. Since it is positive integer we can rewrite the equation, by substituting $$a_k = b_k + 1$$ where $$b_k$$ is non-negative integer. Then we will have

$$
\begin{align*}
n &= a_1 + a_2 + a_3 + ... + a_r \\
  &= b_1 + 1 + b_2 + 1 + b_3 + 1 + ... + b_r + 1 \\
  &= b_1 + b_2 + ... + b_r + r
\end{align*}
$$

Finally, we got $$a_1 + a_2 + a_3 + ... + a_r = n - r$$, which means total number of non-negative integer solutions of this equation is $$\left( \begin{array}{c} n-1 \\ r-1 \end{array} \right)$$.

If we do it again to calculate number of non-negative integer solutions of $$\sum_{k=1}^{r} n_k = n$$, where $$n_k$$ is a non-negative integer. Then substitute $$n_k + 1 = c_k$$, where $$c_k$$ is a positive integer.

$$
\begin{align*}
  n_1 + n_2 + ... + n_r &= n \\
  n_1 + 1 + n_2 + 1 + ... + n_r + 1 &= n + r \\
  c_1 + c_2 + ... + c_r &= n + r
\end{align*}
$$

So the number of positive integer solutions of $$\sum_{k=1}^r c_k = n + r$$ is $$\left( \begin{array}{c} n + r -1 \\ r-1 \end{array} \right)$$, which is also the number of non-negative integer solutions of $$\sum_{k=1}^{r} n_k = n$$. We know is exactly the number of terms in the expansion of $$(x_1 + x_2 + ... + x_n)^n$$

### Summary on The Number of Terms in $$(x_1+x_2...+x_r)^n$$

In case you are overwhelmed with equations, I briefly summarize what I did for the proof:

- The number of terms in the expansion of $$(x_1+x_2...+x_r)^n$$ and the number of **non-negative integer** solutions in $$n=n_1+n_2+...+n_r$$ are same
- The number of **positive integer** solutions of $$n=a_1+a_2+...+a_r$$ is $$\left( \begin{array}{c} n-1 \\ r-1 \end{array} \right)$$, where $$a_k$$ is positive integer.
- The number of **non-negative integer** solutions of $$n - r=b_1+b_2+...+b_r$$ is $$\left( \begin{array}{c} n-1 \\ r-1 \end{array} \right)$$ where $$b_k$$ is non-negative interger, and $$a_k = b_k + 1$$
- The number of **positive integer** solutions of $$n+r=c_1+c_2+...+c_r$$ is $$\left( \begin{array}{c} n + r -1 \\ r-1 \end{array} \right)$$, where $$c_k$$ is positive integer.
- The number of **non-negative integer** solutions of $$n=n_1+n_2+...+n_r$$ is $$\left( \begin{array}{c} n+r-1 \\ r-1 \end{array} \right)$$, where $$n_k$$ is non-negative integer.
- So the number of terms in the expansion of $$(x_1+x_2...+x_r)^n$$ is $$\left( \begin{array}{c} n+r-1 \\ r-1 \end{array} \right)$$.
