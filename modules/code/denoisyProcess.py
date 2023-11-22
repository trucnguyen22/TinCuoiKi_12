

import numpy as np


def cost(y, x):
    return (np.linalg.norm(np.absolute(y) - np.absolute(x)))/(np.linalg.norm(x))


def posterior(y, x, meth, alpha, gamma=1):
    if alpha < 0 or alpha > 1:
        return
    m, n = y.shape
    likelihood = np.sum(np.square(np.absolute(y-x)))
    up = np.absolute(x-np.roll(x, [1, 0], [0, 1]))
    down = np.absolute(x-np.roll(x, [m-1, 0], [0, 1]))
    left = np.absolute(x-np.roll(x, [0, 1], [0, 1]))
    right = np.absolute(x-np.roll(x, [0, n-1], [0, 1]))
    if meth == "quadratic":
        prior = np.sum(np.square(up) + np.square(down) +
                       np.square(left) + np.square(right))
    elif meth == "huber":
        prior_up = np.multiply(np.less_equal(up, gamma), up**2/2) + \
            np.multiply(np.greater(up, gamma), (gamma*up - gamma**2/2))
        prior_down = np.multiply(np.less_equal(down, gamma), down**2/2) + \
            np.multiply(np.greater(down, gamma), (gamma*down - gamma**2/2))
        prior_left = np.multiply(np.less_equal(left, gamma), left**2/2) + \
            np.multiply(np.greater(left, gamma), (gamma*left - gamma**2/2))
        prior_right = np.multiply(np.less_equal(right, gamma), right**2/2) + \
            np.multiply(np.greater(right, gamma), (gamma*right - gamma**2/2))
        prior = np.sum(prior_up + prior_down + prior_left + prior_right)
    elif meth == "log":
        prior_up = gamma*up - gamma**2*np.log(1+up/gamma)
        prior_down = gamma*down - gamma**2*np.log(1+down/gamma)
        prior_left = gamma*left - gamma**2*np.log(1+left/gamma)
        prior_right = gamma*right - gamma**2*np.log(1+right/gamma)
        prior = np.sum(prior_up + prior_down + prior_left + prior_right)

    return (1-alpha)*likelihood + alpha*prior

# based on dynamic step size


def gradiant(y, x, meth, alpha, gamma=1):
    if alpha < 0 or alpha > 1:
        return
    m, n = y.shape
    likelihood = 2*(y-x)
    up = x-np.roll(x, [1, 0], [0, 1])
    down = x-np.roll(x, [m-1, 0], [0, 1])
    left = x-np.roll(x, [0, 1], [0, 1])
    right = x-np.roll(x, [0, n-1], [0, 1])

    if meth == "quadratic":
        prior = 2*(up+down+left+right)
    elif meth == "huber":
        prior_up = np.multiply(np.less_equal(np.absolute(up), gamma), up) + \
            np.multiply(np.greater(np.absolute(up), gamma),
                        (gamma*up/np.abs(up)))
        prior_down = np.multiply(np.less_equal(np.absolute(down), gamma), down) + np.multiply(
            np.greater(np.absolute(down), gamma), (gamma*down/np.abs(down)))
        prior_left = np.multiply(np.less_equal(np.absolute(left), gamma), left) + np.multiply(
            np.greater(np.absolute(left), gamma), (gamma*left/np.abs(left)))
        prior_right = np.multiply(np.less_equal(np.absolute(right), gamma), right) + np.multiply(
            np.greater(np.absolute(right), gamma), (gamma*right/np.abs(right)))
        prior = prior_up + prior_down + prior_left + prior_right
    elif meth == "log":
        prior_up = np.multiply(
            gamma*up, np.reciprocal(gamma + np.absolute(up)))
        prior_down = np.multiply(
            gamma*down, np.reciprocal(gamma + np.absolute(down)))
        prior_left = np.multiply(
            gamma*left, np.reciprocal(gamma + np.absolute(left)))
        prior_right = np.multiply(
            gamma*right, np.reciprocal(gamma + np.absolute(right)))
        prior = prior_up + prior_down + prior_left + prior_right

    return (1-alpha)*likelihood + alpha*prior


def routine(imgNoisy, alpha, gamma, step, thresh, meth):
    old_model = np.copy(imgNoisy)
    old_posterior = posterior(imgNoisy, old_model, meth, alpha)
    posterior_val = []
    posterior_val.append(posterior)
    if meth == "huber" or meth == "log":
        for i in range(30):
            gradiant_img = gradiant(imgNoisy, old_model, meth, alpha, gamma)
            new_model = old_model - step*gradiant_img
            new_posterior = posterior(imgNoisy, new_model, meth, alpha, gamma)

            if new_posterior < old_posterior:
                step = 1.1*step
                old_model = new_model
                old_posterior = new_posterior

            else:
                step = 0.5*step
            posterior_val.append(old_posterior)

    else:
        while step > thresh:
            gradiant_img = gradiant(imgNoisy, old_model, meth, alpha)
            new_model = old_model - step*gradiant_img
            new_posterior = posterior(imgNoisy, new_model, meth, alpha)

            if new_posterior < old_posterior:
                step = 1.1*step
                old_model = new_model
                old_posterior = new_posterior

            else:
                step = 0.5*step
            posterior_val.append(old_posterior)

    return posterior_val, new_model
