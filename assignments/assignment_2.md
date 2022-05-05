# Assignment 2
## Due by 11:59PM Saturday May 7

This assignment will have you practice some basic Python syntax such as functions, for loops and flow control. Write all of your code in a jupyter notebook and save it as `assignment_2/assignment.ipynb` in your git repo. Make sure you push to Github before the due date.

### Part 1

Write a python function for the function $f(x) = x^3 - x^2 - 1$. Also, write a function for it's derivative (you will have to work out $df/dx$ yourself), you can call these functions `f` and `df`.

### Part 2

Write a function `newton(f, df, x0, epsilon=1e-6, max_iter=30)` which performs a [Newton Iteration](https://en.wikipedia.org/wiki/Newton%27s_method) of the function `f` with derivative `df`.

Newton iteration finds the root ($x_n$ such that $f(x_n) = 0$).

To do this, implement the recursive expression $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$ using a loop.

The iteration should stop either when `max_iter` is exceeded or when $f(x_n)$ < `epsilon`.

If the method succeeds, (ie $f(x_n$) < `epsilon`), then your function should print `"Found root in <N> iterations"` and should return the value of $x_n$. Otherwise, it should print `"Iteration failed"` and return `None`.

Make sure that your function is documented with [Numpy style documentation](https://numpydoc.readthedocs.io/en/latest/format.html).

### Part 3

Try out your function with the function you defined in part 1. You can experiment with setting $x_0$ differently (show at least two examples of $x_0$ in the notebook). Leave `epsilon` and `max_iter` as the default values specified in part 2.

Try reducing `epsilon` to 1e-8. Does it still work? If so, how many more iterations does it take to converge.

### How to submit

Commit the jupyter notebook to your git repo. Push the changes to Github. You do not need to send me the link again if you sent it for A1.