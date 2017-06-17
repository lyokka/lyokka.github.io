---
layout: splash
title: Probability 3 Sample Space and Events
permalink: /prob3/
---
## Statistical Experiment

Before we define what is probability, let's think what is statistical experiment

### Example:
A coin is flipped.

### Explanation:
- First, before we flipping a coin, we know there are 2 outcomes, $$\{H, T\}$$, where $$H$$ is head, and $$T$$ is tail.
- Second, we know the result is either $$H$$ or $$T$$, but we don't know it exactly.
- Third, a coin can be flipped as many times as desired.

### Definition:
A ``statistical experiment`` is an experiment in which:
- <span style="color:red">all outcomes</span> of  the experiment are <span style="color:red">known</span> in advance,
- any <span style="color:red">performance</span> of the experiment results in an outcome that is <span style="color:red">not known</span> in advance, and
- the experiment can be <span style="color:red">repeated</span> under identical conditions.

## Sample Space

### Example:
When we flip two coins, what's the possible outcomes?

### Explanation:
We can have following possible outcomes:

$$
\{(H, H), (H, T), (T, H), (T, T)\}
$$

### Definition:
The set of all possible outcomes of a statistical experiment is ``sample space``, usually denotes as $$S$$. In the example above the sample space is $$\{(H, H), (H, T), (T, H), (T, T)\}$$.

## Event
### Example:
When we flip two coins, what's the possible outcomes of two coins shows different faces?

### Explanation:
The outcomes with different faces:

$$
\{(H, T), (T, H)\}
$$

Obviously, this is a subset of sample space.

### Definition:
Any subset $$E$$ of sample space $$S$$ is an ``event``.

## Event Space:
### Example:
When we flip two coins, we are interested in two coins showing different faces, what's the event space of this experiment?

### Explanation:
Mathematically, we modeled such an event space using $$\sigma-algebra$$ of sample space $$\Omega$$. Term $$\sigma-algebra$$ comes from ``measure theory``, we don't dig deep into it. Roughly speaking, $$\sigma-algebra$$ only tells us:

  - $$\varnothing \in F$$ (empty set is in event space $$F$$.)
  - If $$ A \in F $$, then its $$ A^c \in F $$ (If an event in event space, then its complement also in event space.)
  - If $$ A_1, A_2, A_3, ... \in F $$, then $$ \bigcup_{i=1}^{\infty}A_i \in F $$. (If many events in event space, then their union also in event space.)

Back to experiment of flip two coins, obviously, there are many event spaces, e.g:
  - $$F = \{\varnothing, \Omega\}$$, where $$\Omega$$ is $$\{(H, H), (H, T), (T, H), (T, T)\}$$, since
    - $$\varnothing \in F$$
    - $$\Omega \in F$$ and $$\Omega^c=\varnothing$$
    - $$\Omega \bigcup \varnothing = \Omega$$
  - $$F = \{\varnothing, \Omega, E_\text{dif}, E_\text{same}\}$$, where event $$E_\text{dif}$$ is $$\{(H, T), (T, H)\}$$, and event $$E_\text{same}$$ is $$\{(H, H), (T, T)\}$$, we can tell it is valid:
    - $$\varnothing \in F$$
    - - $$\varnothing \in F$$, $$\varnothing^c = \Omega \in F$$
      - $$E_\text{dif} \in F$$, $$E_\text{dif}^c = E_\text{same} \in F$$
    - - $$E_\text{dif} \bigcup E_\text{same} = \Omega $$
      - $$\Omega \bigcup \varnothing = \Omega$$

Therefore, $$\{\varnothing, \Omega, E_\text{dif}, E_\text{same}\}$$ is the event space of flipping two coins, when we are interested in event showing two different faces.

### Definition:
If we are interested some events, we can form an ``event space`` by adding their components, their union, and empty set.

## Probability (Probability Measure)

Probability could be interpreted in different ways, and there are different ways to define it. However, in any definition, probability of event $$A$$ is just a number in $$[0, 1]$$.

### Classical Definition:
probability of event $$A$$ is

$$
P(A) = \frac{N_A}{N}
$$

where $$N$$ is the number of total possible outcomes and $$N_A$$ is the number of outcomes that are favorable to the event $$A$$. We also assume all outcomes are <span style="color:red">equally likely</span>.

### Example:
What's the probability that head shows when flipping a coin?

### Explanation:
- number of total possible outcomes is 2(Head or Tail).
- number of outcomes that is head is 1
- by *Classical Definition*, $$P(Head) = \frac{1}{2}$$

### Problem of Classical Definition:
- We need assume all outcomes are equally likely, for example if the coin is a not fair coin, $$P(Head) \neq \frac{1}{2}$$.
- If the number of possible outcomes(sample space) is infinite, we must use length, area or some other measure of infinity to calculate $$P(A) = \frac{N_A}{N}$$. However, if we use different measure of infinity, the probability maybe totally different.

### Bertrand Paradox(Optional)
*Bertrand Paradox* could show the probability maybe totally different when sample space is infinite, and we define the probability through classical definition.

### Relative Frequency Definition:
probability of event $$A$$ is

$$
P(A) = \lim_{n\to\infty} \frac{n_A}{n}
$$

where $$n$$ is the number of trails(number of experiments), and $$n_A$$ is the number of occurrences.

### Example:
What's the probability that head shows when flipping a coin?

### Explanation:
Let's do experiment, flipping coins 10000 times, then counting the number of times that head shows.

![relative_frequency.jpg](/assets/images/prob/prob3/relative_frequency_interp.jpg)

We could find $$P(A)=\lim_{n\to\infty} \frac{n_A}{n}\approx\frac{1}{2}$$.

### Problem of Relative Frequency Definition:
This definition seems very intuitive, as long as we do enough experiment we could get a probability of the event that we interested in. However,
- we don't know if $$P(A)=\lim_{n\to\infty} \frac{n_A}{n}$$ will converge to some number, because we can never proof it.
- more practically, we can never do infinite times experiments, so we can never get the limit.

### Axiomatic Definition:
This definition is made of 3 part:
- $$P(A) \ge 0$$ for all $$A \in F$$, where $$A$$ is an event in event space $$F$$.
- $$P(\Omega)=1$$, where $$\Omega$$ is the sample space.
- If $$A_1, A_2, ... \in F$$, are pairwise disjoint(e.g. $$A_i \bigcap A_j = \varnothing$$ for all $$i \ne j$$), then $$P(\bigcup_{i=1}^{\infty}A_i) = P(A_1) + P(A_2) + ... = \sum_{i=1}^{\infty} P(A_i)$$

**This is the definition which can basically satisfied and explained everything,  however the axiomatic definition of probability will still cause a lot arguments nowadays, but that's how we define probability in most cases.**

### Connection between These Definitions
No matter how we define probability of event $$A$$, we don't know if event $$A$$ will happen. While, if we assume all outcomes are equally likely, we can use ``Clasical Definition`` to determine $$P(A)$$; then we can use $$P(A)$$ to deduce some other probability $$P(B)$$ of event $$B$$  by ``Axiomatic Definition``; finally we can also show the link between theory and experiment by ``Relative Frequency Definition``.

## Probability Space
At last, we introduce what is ``probability space``. Right now, we know we can measure a probability of event $$A$$ as $$P(A)$$, but we know $$A$$ must in event space $$F$$, and $$F$$ must be modeled by $$\sigma-algebra$$ of sample space $$\Omega$$.

### Definition:
We define $$(\Omega, F, P)$$ is a probability space, where $$\Omega$$ is sample space, $$F$$ is event space, $$P$$ is probability measure, which is function that convert event $$A$$ to a real number from 0 to 1.
