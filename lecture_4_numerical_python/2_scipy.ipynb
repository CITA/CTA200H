{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# SciPy\n",
    "\n",
    "SciPy is a collection of software for scientific computing. It includes NumPy and matplotlib from the previous two lessons, for example.\n",
    "\n",
    "The SciPy library also includes functions to do numerical integration, interpolation, Fourier transforms, statistics, special mathematical functions, and more.\n",
    "\n",
    "### Integration\n",
    "\n",
    "\n",
    "* $\\int_0^5 dx (x^2 + 3)$\n",
    "\n",
    "* We will use Gaussian quadrature  https://en.wikipedia.org/wiki/Gaussian_quadrature \n",
    "\n",
    "* exact answer is $5^3 / 3 + 3\\times5 $"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "5.**3 / 3 + 3 * 5."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can use SciPy to numerically integrate the function $(x^2 + 3)$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy import integrate\n",
    "import numpy as np\n",
    "\n",
    "# define the function to integrate\n",
    "def myf(x):\n",
    "    return x**2 + 3\n",
    "\n",
    "# pass in function, integration limits, and quality of answer\n",
    "# returns answer and estimate of the error\n",
    "I, err = integrate.quad(myf, 0, 5, epsabs = 1.e-14)\n",
    "\n",
    "print (I, err)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "integrate.quad?\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Integration of a pre-sampled function\n",
    "\n",
    "In astrophysics this happens a lot -- someone hands you some pre-sampled points, and you have to calculate the area under the curve.\n",
    "\n",
    "Recall Simpson's rule -- https://en.wikipedia.org/wiki/Gaussian_quadrature\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "N = 20\n",
    "\n",
    "\n",
    "x = np.linspace(0, 2 * np.pi, N)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "y = np.cos(x)**2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%pylab inline\n",
    "\n",
    "plot(x, y, 'o')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "val = integrate.simps(y,x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"value is\", val, \"fractional error is\" , np.abs(val - np.pi) / np.pi)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Not bad -- 0.2% accuracy based on so few points.\n",
    "\n",
    "### Interpolation\n",
    "\n",
    "Say you have some data that is sampling your function and you want to interpolate the value of your function between your data points. \n",
    "\n",
    "* Example function (from which coarse data are drawn):  $f(x) = (e^{-x})  \\sin(2  \\pi  x)$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def myf(x):\n",
    "    return (exp(-x)) * sin(2 * numpy.pi * x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's sample our function only at 8 points, but we want to interpolate between those points to sample our function at 50 different points."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_coarse = linspace(0, 2, num = 8)\n",
    "x_fine = linspace(0, 2, num = 50)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let's try different interpolation techniques. First, we will use a basic interpolation method, and then we will interpolate using a spline (see http://mathworld.wolfram.com/CubicSpline.html for information about cubic splines)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy import interpolate\n",
    "\n",
    "myInterpFunc = interpolate.interp1d(x_coarse, myf(x_coarse))\n",
    "y_coarse = myInterpFunc(x_coarse)\n",
    "\n",
    "myInterpFuncSpline = interpolate.CubicSpline(x_coarse, myf(x_coarse))\n",
    "y_coarseSpline = myInterpFuncSpline(x_coarse)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Here's our coarse points and how they compare to the original function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "plot(x_coarse, y_coarse, 'o', label = 'original points')\n",
    "plot(x_fine, myf(x_fine), label = 'original function')\n",
    "legend()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And here are the results of our interpolations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "plot(x_coarse, y_coarse, 'o', label = 'original points')\n",
    "plot(x_fine, myInterpFunc(x_fine), '+', label = 'interpolated values')\n",
    "plot(x_fine, myInterpFuncSpline(x_fine), 'x', label = 'spline interpolated values')\n",
    "plot(x_fine, myf(x_fine), label = 'original function')\n",
    "legend()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice that, although the polynomial spline doesn't fit our data exactly, it does provide a much better fit to our function than the simple interpolation."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
