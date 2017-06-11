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
