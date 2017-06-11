---
layout: splash
title: Probability 1 Permutation, Combination
permalink: /prob1/
---
# Probability 1 Permutation, Combination

Before we move to probability we need to define what is permutation and combination.

## Permutation
### Example:
How many possible ways to arrange three letters $$ a, b, c $$?

### Explanation:
We could select a letter from 3 letters, then select another letter from the rest 2 letters. Possible result we could have:

$$abc, bac, cab, acb, bca, cba$$

Total number of arrangements is $$6$$. Each arrangement is a ``permutation``. Thus, we know there are $$ 6 $$ possible permutations.

### Definition:
Without loss of generality, if we arrange $$ n $$ different objects, there will be

>$$
  n (n-1) (n-2) ... 3 \cdot 2 \cdot 1 = n!
$$

different permutations.

## Permutation with Repetition(Optional)
### Example:
 If we arrange $$ 4 $$ letters, $$ a $$, $$ a $$, $$ b $$, $$ b $$. How many possible permutations could we get?

### Explanation:
To make it clear, we could label $$ 4 $$ letters as $$ a_1 $$, $$ a_2 $$, $$ b_1 $$, $$ b_2 $$. Then we can list all possible permutations:

  <center>
    <table style="width:50%;" border = "1">
      <th colspan="6" style="text-align:center;">permutations</th>
      <tr>
        <td>$$a_1 a_2 b_1 b_2$$</td>
        <td>$$a_1 a_2 b_2 b_1$$</td>
        <td>$$a_1 b_1 a_2 b_2$$</td>
        <td>$$a_1 b_1 b_2 a_2$$</td>
        <td>$$a_1 b_2 a_2 b_1$$</td>
        <td>$$a_1 b_2 b_1 a_2$$</td>
      </tr>
      <tr>
        <td>$$a_2 a_1 b_1 b_2$$</td>
        <td>$$a_2 a_1 b_2 b_1$$</td>
        <td>$$a_2 b_1 a_1 b_2$$</td>
        <td>$$a_2 b_1 b_2 a_1$$</td>
        <td>$$a_2 b_2 a_1 b_1$$</td>
        <td>$$a_2 b_2 b_1 a_1$$</td>
      </tr>
      <tr>
        <td>$$b_1 b_2 a_1 a_2$$</td>
        <td>$$b_1 b_2 a_2 a_1$$</td>
        <td>$$b_1 a_1 b_2 a_2$$</td>
        <td>$$b_1 a_2 b_2 a_1$$</td>
        <td>$$b_1 a_1 a_2 b_2$$</td>
        <td>$$b_1 a_2 a_1 b_2$$</td>
      </tr>
      <tr>
        <td>$$b_2 b_1 a_1 a_2$$</td>
        <td>$$b_2 b_1 a_2 a_1$$</td>
        <td>$$b_2 a_1 b_1 a_2$$</td>
        <td>$$b_2 a_2 b_1 a_1$$</td>
        <td>$$b_2 a_1 a_2 b_1$$</td>
        <td>$$b_2 a_2 a_1 b_1$$</td>
      </tr>
    </table>
  </center>

We cound find the pattern in all possible permutations:

<center>
  <table style="width:50%;" border = "1">
    <th colspan="6" style="text-align:center;">permutations</th>
    <tr>
      <td style="color:#FF77A8">$$a_1 a_2 b_1 b_2$$</td>
      <td style="color:#FF77A8">$$a_1 a_2 b_2 b_1$$</td>
      <td style="color:#83769c">$$a_1 b_1 a_2 b_2$$</td>
      <td style="color:#83769c">$$a_1 b_1 b_2 a_2$$</td>
      <td style="color:#29adff">$$a_1 b_2 a_2 b_1$$</td>
      <td style="color:#29adff">$$a_1 b_2 b_1 a_2$$</td>
    </tr>
    <tr>
      <td style="color:#FF77A8">$$a_2 a_1 b_1 b_2$$</td>
      <td style="color:#FF77A8">$$a_2 a_1 b_2 b_1$$</td>
      <td style="color:#83769c">$$a_2 b_1 a_1 b_2$$</td>
      <td style="color:#83769c">$$a_2 b_1 b_2 a_1$$</td>
      <td style="color:#29adff">$$a_2 b_2 a_1 b_1$$</td>
      <td style="color:#29adff">$$a_2 b_2 b_1 a_1$$</td>
    </tr>
    <tr>
      <td style="color:#ffa300">$$b_1 b_2 a_1 a_2$$</td>
      <td style="color:#ffa300">$$b_1 b_2 a_2 a_1$$</td>
      <td style="color:#ff004d">$$b_1 a_1 b_2 a_2$$</td>
      <td style="color:#ff004d">$$b_1 a_2 b_2 a_1$$</td>
      <td style="color:blue">$$b_1 a_1 a_2 b_2$$</td>
      <td style="color:blue">$$b_1 a_2 a_1 b_2$$</td>
    </tr>
    <tr>
      <td style="color:#ffa300">$$b_2 b_1 a_1 a_2$$</td>
      <td style="color:#ffa300">$$b_2 b_1 a_2 a_1$$</td>
      <td style="color:#ff004d">$$b_2 a_1 b_1 a_2$$</td>
      <td style="color:#ff004d">$$b_2 a_2 b_1 a_1$$</td>
      <td style="color:blue">$$b_2 a_1 a_2 b_1$$</td>
      <td style="color:blue">$$b_2 a_2 a_1 b_1$$</td>
    </tr>
  </table>
</center>

All possible permutations could be separated into such blocks. In those blocks, they have same pattern, such as $$a a b b$$. Here we labeled repeated objects, if we omit the label, we will get permutations with repetition, which is $$6$$ in this case.

We can also consider, in each block, the only thing that makes difference is permutations of repeated objects. In the example above, each block have 2 repeated $$a$$ and $$b$$, so a pattern like $$a, a, b, b$$ will have 4 permutations($$2!$$ for $$a$$, $$2!$$ for $$b$$).

### Definition:
So without loss of generality, if we have $$n$$ objects with $$n_1$$ objects are *type 1* (like $$a_1, a_2, a_3$$ are type $$a$$), $$n_2$$ objects are *type 2*, $$n_3$$ objects are *type 3*, so on so forth to type $$k$$, the number of permutations is

> \$\$
    \frac{n!}{n_1! n_2! n_3! ... n_k!}
  $$

## Combinations
### Example:
Suppose we have $$5$$ objects, $$a, b, c, d, e$$. We want to divided to two groups or select 2 from them. How many possible ways for selection?


### Explanation:
We could select $$1$$ from $$5$$, then we could select another $$1$$ from the rest $$4$$. This strategy will give us 20 possible groups with order(since we select objects in order):

<center>
  <table style="width:50%;" border = "1">
    <th colspan="10" style="text-align:center;">ordered selection result</th>
      <tr>
        <td>$$ab$$</td>
        <td>$$ac$$</td>
        <td>$$ad$$</td>
        <td>$$ae$$</td>
        <td>$$bc$$</td>
        <td>$$bd$$</td>
        <td>$$be$$</td>
        <td>$$cd$$</td>
        <td>$$ce$$</td>
        <td>$$de$$</td>
     </tr>
     <tr>
        <td>$$ba$$</td>
        <td>$$ca$$</td>
        <td>$$da$$</td>
        <td>$$ea$$</td>
        <td>$$cb$$</td>
        <td>$$db$$</td>
        <td>$$eb$$</td>
        <td>$$dc$$</td>
        <td>$$ec$$</td>
        <td>$$ed$$</td>
     </tr>
  </table>
</center>

From the table above, we can clear see there are repetitions because of the permutation. In this example, we want to select 2 objects from 5. When we select 1 group such as $$a, b$$, there are $$2!$$ ways to get this result. One is select $$a$$ first, the other is select $$b$$ first.

Typically, we can consider each group we selected is a ``combination``. We can selected $\frac{5 \cdot 4}{ 2 \cdot 1} = 10$ different combinations in this example.

### Definition:
Without loss of generality, if we want to select a group of $$r$$ different objects from $$n$$. Total number of combinations we have is

$$
\begin{align*}
  \frac{n (n-1) ... (n - r + 2)(n -r + 1)}{r !}
\end{align*}
$$

Rewrite the equation above,

$$
\begin{align*}
  \frac{n (n-1) ... (n -r + 1)}{r !} &= \frac{n(n-1)...(n-r+1) \;\;\;\; \cdot \;\;\;\; (n-r)(n-r-1)...2 \cdot 1}{r!  \;\;\;\; \cdot \;\;\;\; (n-r)(n-r-1)...2\cdot 1} \\
  &=\frac{n!}{(n-r)! \cdot r!} \\
  &= \left( \begin{array}{c} n \\ r \end{array} \right)
\end{align*}
$$
