---
layout: splash
title: Probability 1 Permutation, Combination
permalink: /prob1/
---
# Probability 1 Permutation, Combination

Before we move to probability we need to define what is permutation and combination.

## Permutation
### Example:
 If we arrange three $$ a $$, $$ b $$ and $$ c $$, three letters. We could have possible result:

> permutation: $$abc, bac, cab, acb, bca, cba$$

Total number of arrangements is $$ 6 $$. Each arrangement is a ``permutation``. Thus, we know there are $$ 6 $$ possible permutations.

Without loss of generality, if we arrange $$ n $$ different objects, there will be

\$\$
  n (n-1) (n-2) ... 3 \cdot 2 \cdot 1 = n!
$$


different permutations.

## Permutation with Repetition(Optional)
### Example:
 If we arrange $$ 4 $$ letters, $$ a $$, $$ a $$, $$ b $$, $$ b $$. How many possible permutations could we get?

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

We can also consider, in each block, the only thing that makes difference is permutations of repeated objects. In the example above, each block have 2 repeated $$a$$ and $$b$$, so a pattern like $$a, a, b, b$$ will have 4($$2! \cdot 2!$$) permutations if . So without loss of generality, if we have $$n$$ objects with $$n_1$$ objects are type_1, $$$n_2$ objects are type_2, $$n_3$$ objects are type_3, so on so forth to type k, the number of permutations is

\$\$
  \frac{n!}{n_1! n_2! n_3! ... n_k!}
$$
