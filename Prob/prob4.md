---
layout: splash
title: Probability 4 Conditional Probability
permalink: /prob4/
---

## Conditional Probability

### Definition:

Given a probability space $$(\Omega,F,P)$$, where $$\Omega$$ is sample space, $$F$$ is event space, $$P$$ is probability measure(probability function). If some event $$S$$ from event space $$F$$, then $$P(S) > 0$$, we define probability of event $$E$$ happens given $$S$$ is

$$
P(E|S) = \frac{P(ES)}{P(S)}
$$

### Explanation:
Since $$S$$ has already happened, the sample space reduce to $$S$$. No matter what event $$E$$ is, it must belong to $$E\cap S$$, for simplicity $$ES$$. Then the probability space becomes $$(S, F_s, P(\cdot | S))$$, where $$S$$ is the reduced sample space, $$F_s$$ is new event space, and $$P(\cdot | S)$$ is the conditional probability measure.

## Prior and Posterior:
### Definition:
If $$A,B$$ are two events in event spaces.
$$P(AB) = P(B|A)P(A) = P(B|A)P(A)$$, we call $$P(A)$$ ``prior``, and $$P(B|A)$$ ``posterior``.

### Proof:
$$
\begin{align}
P(A|B) = \frac{P(AB)}{P(B)} &\Longrightarrow P(A|B)P(B) = P(AB)\\
&\Longrightarrow P(AB) = P(B|A)P(A) \\
&\Longrightarrow P(B|A)P(A) = P(A|B)P(B)
\end{align}
$$

### Explanation:
If we only know $$P(A)$$ without anything else, that's the earliest thing we know, however, if we know $$P(A|B)$$, which means $$P(A)$$ has already been updated with $$B$$.

### Multiplication Rule:

$$ P(E_1E_2E_3E_4...E_n) = P(E_1)P(E_2|E_1)P(E_3|E_1E_2)...P(E_n|E_{1}E_{2}...E_{n-2}E_{n-1})$$

## Law of Total Probability
### Definition:
If $$(\Omega, F, P)$$ is a probability space, if $$A_i \in F$$, and $$A_i \cap A_j = \varnothing$$ for any $$i \ne j$$ and $$\Omega = \cup_iA_i$$. For any $$S \in F$$.

$$P(S) = P(A_1) P(S|A_1) + P(A_2) P(S|A_2) + ... + P(A_n) P(S|A_n)$$

### Proof:
$$\begin{align}
P(S) &= P(A_1S) + P(A_2S) + ... + P(A_nS)\\
&= P(A_1) P(S|A_1) + P(A_2) P(S|A_2) + ... + P(A_n) P(S|A_n)
\end{align}
$$

## Bayes' Rule
### Definition:

If $$(\Omega, F, P)$$ is a probability space, if $$A_i \in F$$, and $$A_i \cap A_j = \varnothing$$ for any $$i \ne j$$ and $$\Omega = \cup_iA_i$$. For any $$S \in F$$.

$$P(A_i|S) = \frac{P(S|A_i)P(A_i)}{\sum_{j} P(S|A_j)P(A_j)}$$

### Proof:
$$
\begin{align}
P(A_i|S) &= \frac{P(A_i S)}{P(S)} \\
&= \frac{P(S|A_i)P(A_i)}{P(S)} \\
&= \frac{P(S|A_i)P(A_i)}{P(A_1S) + P(A_2S) + ... + P(A_nS)} \\
&= \frac{P(S|A_i)P(A_i)}{\sum_{j} P(A_jS)} \\
&= \frac{P(S|A_i)P(A_i)}{\sum_{j} P(S|A_j)P(A_j)}
\end{align}
$$

## Independence
### Definition:
Given probability space $$(\Omega, F, P)$$, if $$A,B \in F$$, if $$P(AB) = P(A)P(B)$$, then $$A,B$$ are independent.

Similar, we can define conditional independence given event $$C$$ as $$P(AB|C) = P(A|C)P(B|C)$$

- **Conditional Independence does not imply Independence**
- **Independence does not imply Conditional Independence**
