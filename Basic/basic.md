---
layout: splash
title: Basic
permalink: /basic/
---

## Exponential Function:

### Definition:
$$e^x = \sum_{n=0}^{\infty}\frac{x^n}{n!} = \frac{x^0}{0!} + \frac{x^1}{1!} + \frac{x^2}{2!} + ...$$

$$e^x = \lim_{n\to\infty} (1+\frac{x}{n})^n \rightarrow e^x = \lim_{n\to0} (1+xn)^{\frac{1}{n}} $$


## Derivative:
### Definition:
$$\frac{df(x)}{dx} = \lim_{\Delta x\to0} \frac{f(x+\Delta x) - f(x)}{\Delta x}$$

### Example: Derivative of Exponential Function

$$
\begin{align}
\frac{e^x}{dx} &= \lim_{\Delta x\to0} \frac{e^{(x+\Delta x)} - e^x}{\Delta x}\\
&= \lim_{\Delta x\to0} \frac{e^x (e^{\Delta x} -1)}{\Delta x}\\
&= e^x \lim_{\Delta x\to0} \frac{(e^{\Delta x} -1)}{\Delta x}\\
&= e^x \cdot \lim_{\Delta x\to0}(\frac{1}{\Delta x})(\underbrace{1+\Delta x + \frac{(\Delta x)^2}{2!} + \frac{(\Delta x)^3}{3!} + ...}_{e^{\Delta x}} - 1) \\
&= e^x \cdot \lim_{\Delta x\to0}(\frac{1}{\Delta x})(\Delta x + \frac{(\Delta x)^2}{2!} + \frac{(\Delta x)^3}{3!} + ...) \\
&= e^x \cdot \lim_{\Delta x\to0}(1 + \underbrace{\frac{(\Delta x)}{2!}}_{0} + \underbrace{\frac{(\Delta x)^2}{3!}}_{0} + ...)\\
&= e^x
\end{align}
$$
