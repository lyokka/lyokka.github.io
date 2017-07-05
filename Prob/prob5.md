---
layout: splash
title: Probability 5 Random Variable
permalink: /prob5/
---

## Random Variable

### Definition:
Given a probability space $$(\Omega, F, P)$$, a ``random variable`` $$X$$ is a function from the sample space $$X$$ to the real numbers.

### Example:
Let's flip a coin. The sample space is $$\{Head, Tail\}$$. We define a random variable $$X$$, where

$$
\begin{align*}
  X(head) = 5\\
  X(tail) = -5
\end{align*}
$$

In this case, $$X$$ is a valid random variable.

### Explanation:
- **Random Variable is <span style="color:red">not a number</span>, random variable is a <span style="color:red">function</span> of outcomes in probability space**

- Random Variable could be ``discrete``, if it takes values on a finite or countably infinite subset of R such as the integers.
- It can also be ``continuous``, if it takes values over real numbers.

## Probability Mass Function:
Since random variable convert elements in sample space to real numbers. We can also convert these real numbers to probability. Therefore, probability mass function is a  function that output probability.

### Definition:
Given a probability space $$(\Omega, F, P)$$ and a ``random variable`` $$X$$. Then we map $$\Omega$$ to $$Z$$(set of integers: $$... -2,-1,0,1,2,3 ... $$). The ``probability mass function``(*pmf*) of $$X$$ is defined as:

$$p(x) = P(\{\omega|X(\omega)=x\})$$

### Example:
If we want to investigate the suit of a randomly selected card. Sample space is $$\Omega = \{\clubsuit, \diamondsuit, \heartsuit, \spadesuit\}$$; $$\omega$$ could be any suit in sample space. But we have a random variable maps $$X(\clubsuit) = 0, X(\diamondsuit) = 1, X(\heartsuit) = 2, X(\spadesuit) = 3$$, then we define probability mass function $$p(0) = P({\omega|X(\omega)=0}) = \frac{1}{4}$$, we know only $$X(\clubsuit)=0$$.

## Important Discrete Distribution

Usually saying a distributed of a discrete random variable, we refers to its *pmf*

### Bernoulli Random Variable

### Example
Tossing a biased coin 1 time, the probability of outcome is head is $$p$$.

``Bernoulli Distribution``:

$$
p_X(x) = \left\{
\begin{array}{ll}
      1- p & x = 0 \\
      p & x = 1 \\
      0 & else
\end{array}
\right. \\
\text{or to be more condense}\\
p_X(x) = p^x(1-p)^{(1-x)}, \text{  for  } x \in \{0, 1\}
$$

Here $$X(head) = 1$$, $$X(tail) = 0$$.

### Explanation:
probability of head show is $$p$$, which is the only parameter that will influence the shape of distribution.
![Bernoulli](/assets/images/prob/prob5/bernoulli_rv.png)

### Validity:
It is obvious to proof the validity of Bernoulli distribution:
$$p_X(0) + p_X(1) = p + 1- p = 1$$

### Geometric Random Variable

### Example
Tossing a biased coin till we obtain heads, what's the probability that we tossed $$k$$ times? We assume flips are independent, for example, even though I flipped coins 10 times, all of them are tails, but when I flip the coin again, I still have probability $$p$$ to get a head.

``Geometric Distribution``:
$$p_X(x) = (1-p)^{k-1}p$$ where $$k = 1, 2, 3, 4, ...$$
Here, random variable $$X(\text{flip one time}) = 0, X(\text{flip two times}) = 1, X(\text{flip three times}) = 2, ...$$
### Explanation:
Let's calculate the probability that we get a head after tossing 10 times.
$$
\begin{align}
P(\text{flip 10 times}) &= P(\text{1st flip is tail, 2nd flip is tail, 3rd flip is tail, ... , 10th flip is head})\\
&= P(\text{1st flip is tail})P(\text{2nd flip is tail})P(\text{3rd flip is tail}), ... ,P(\text{10th flip is head})\\
&= \underbrace{(1-p)(1-p)...(1-p)}_\text{9 tails} \underbrace{p}_\text{1 head} \\
&= (1-p)^{(10-1)} p
\end{align}$$

- paramter $$p$$ is the only parameter that influence the shape of distribution.
![Geometric](/assets/images/prob/prob5/geometric_rv.png)

### Validity:
$$
\begin{align}
\sum_{i=1}^{\infty} p_X(i) &= (1-p)^0 p + (1-p)^1 p + (1-p)^2 p + ... + (1-p)^n p + ... \\
 &= \lim_{n\to\infty}\sum_{k=0}^{n}(1-p)^k p \\
 &= \lim_{n\to\infty} p((1-p)^0 + (1-p)^1 + (1-p)^2 + ... + (1-p)^n ) \\
 &= \lim_{n\to\infty} p((1-p)^0 + (1-p)^1 + (1-p)^2 + ... + (1-p)^n ) \\
 &= \lim_{n\to\infty} p \frac{1-(1-p)^{n+1}}{1-(1-p)} \\
 &= \lim_{n\to\infty} p \frac{1-(1-p)^{n+1}}{p} \leftarrow \lim_{n\to\infty} (1-p)^{n+1}=0 \\
 &= 1
\end{align}
$$

### Binomial Random Variable

### Example
Tossing a biased coin $$n$$ times, what's the probability to get $$k$$ times head? We still assume flips are independent.

``Binomial Distribution``:
$$p_X(x) = \left( \begin{array}{c} n \\ k \end{array} \right) (1-p)^{n-k}p^k$$ where $$k = 1, 2, 3, 4, ...$$
Here, random variable $$X(\text{no head from n times flipping}) = 0,\\ X(\text{one head from n times flipping}) = 1,\\ X(\text{two heads from n times flipping}) = 2, ...$$

### Explanation:
Let's calculate the probability that we get 2 heads after tossing 3 times. All possible results are $$\{(T,H,H), (H,T,H), (H,H,T)\}$$. The probability of each possible result is $$(1-p)^2 p$$, totally there are $$\left( \begin{array}{c} 3 \\ 2 \end{array} \right)$$ combinations.
$$
\begin{align}
P(\text{2 heads after tossing 3 times}) &= \left( \begin{array}{c} 3 \\ 2 \end{array} \right) (1-p)^2 p
\end{align}$$

Not like ``Geometric Distribution``, ``Binomial Distribution`` have finite length, and it's shape depends on $$p, n$$.
