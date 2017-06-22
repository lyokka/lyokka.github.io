---
layout: splash
title: Series
permalink: /series/
---

## Series

## $$ \sum_{k=1}^{n}k$$:
>$$ \sum_{k=1}^{n}k = 1 + 2 + 3 + ... + n - 1 + n $$
### proof:
>$$
\begin{align}
 \sum_{k=1}^{n}k = S &= 1 + 2 + 3 + ... + n - 1 + n \\
 S &= n + n-1 + n-2 + ... + 2 + 1 \\
 2S &= \underbrace{(n+1) + (n-1+2) + (n-2+3) + ... + (2+n-1) + (1+n)}_{\text{n}}\\
 2S &= (n+1)n\\
  S &= \frac{n(n+1)}{2}
\end{align}
$$

## $$ \sum_{k=1}^{n}k^2$$：
>$$ \sum_{k=1}^{n}k^2 = 1^2 + 2^2 + 3^2 + ... + (n - 1)^2 + n^2 $$
### proof:
>$$
\begin{align}
 \sum_{k=1}^{n}((k+1)^3-k^3) &= \sum_{k=1}^{n}(k^3 +3k^2+3k+1-k^3)\\
    &=  \sum_{k=1}^{n}(3k^2+3k+1)\\
    &= 3\sum_{k=1}^{n}k^2 + 3\sum_{k=1}^{n}k + \sum_{k=1}^{n}1 \\
    &= 3\sum_{k=1}^{n}k^2 + 3\frac{n(n+1)}{2} + n\\
 \sum_{k=1}^{n}((k+1)^3-k^3) &= (n+1)^3 - n^3 + n^3 - (n-1)^3 + ... + 2^3 - 1^3\\
  &= (n+1)^3 - 1\\
(n+1)^3 - 1 &= 3\sum_{k=1}^{n}k^2 + 3\frac{n(n+1)}{2} + n\\
\sum_{k=1}^{n}k^2 &= \frac{n(n+1)(2n+1)}{6}
\end{align}
$$

## $$\sum_{k=1}^{n} r^k$$:
>$$ \sum_{k=0}^{n}r^k = r^0 + r^1 + r^2 + ... + r^(n - 1) + r^n $$
### proof:
> for $$r \ne 1$$
$$\begin{align}
\sum_{k=0}^{n}r^k = S &= r^0 + r^1 + r^2 + ... + r^(n - 1) + r^n\\
r S &= r^1 + r^2 + ... + r^(n - 1) + r^n + r^{(n+1)}\\
(1-r)S &= 1 - r^{(n+1)} \\
S &= \frac{1 - r^{(n+1)}}{1-r}
\end{align}
$$

> for $$r = 1$$
$$\begin{align}
\sum_{k=0}^{n}r^k = S &= \underbrace{1^0 + 1^1 + 1^2 + ... + 1^{(n - 1)} + 1^n}_{\text{n+1}}\\
S &= n+1
\end{align}
$$
