

# import numpy as np


# def cost(y, x):
#     return (np.linalg.norm(np.absolute(y) - np.absolute(x)))/(np.linalg.norm(x))


# def posterior(y, x, meth, alpha, gamma=1):
#     if alpha < 0 or alpha > 1:
#         return
#     m, n = y.shape
#     likelihood = np.sum(np.square(np.absolute(y-x)))
#     up = np.absolute(x-np.roll(x, [1, 0], [0, 1]))
#     down = np.absolute(x-np.roll(x, [m-1, 0], [0, 1]))
#     left = np.absolute(x-np.roll(x, [0, 1], [0, 1]))
#     right = np.absolute(x-np.roll(x, [0, n-1], [0, 1]))
#     if meth == "quadratic":
#         prior = np.sum(np.square(up) + np.square(down) +
#                        np.square(left) + np.square(right))
#     elif meth == "huber":
#         prior_up = np.multiply(np.less_equal(up, gamma), up**2/2) + \
#             np.multiply(np.greater(up, gamma), (gamma*up - gamma**2/2))
#         prior_down = np.multiply(np.less_equal(down, gamma), down**2/2) + \
#             np.multiply(np.greater(down, gamma), (gamma*down - gamma**2/2))
#         prior_left = np.multiply(np.less_equal(left, gamma), left**2/2) + \
#             np.multiply(np.greater(left, gamma), (gamma*left - gamma**2/2))
#         prior_right = np.multiply(np.less_equal(right, gamma), right**2/2) + \
#             np.multiply(np.greater(right, gamma), (gamma*right - gamma**2/2))
#         prior = np.sum(prior_up + prior_down + prior_left + prior_right)
#     elif meth == "log":
#         prior_up = gamma*up - gamma**2*np.log(1+up/gamma)
#         prior_down = gamma*down - gamma**2*np.log(1+down/gamma)
#         prior_left = gamma*left - gamma**2*np.log(1+left/gamma)
#         prior_right = gamma*right - gamma**2*np.log(1+right/gamma)
#         prior = np.sum(prior_up + prior_down + prior_left + prior_right)

#     return (1-alpha)*likelihood + alpha*prior

# # based on dynamic step size


# def gradiant(y, x, meth, alpha, gamma=1):
#     if alpha < 0 or alpha > 1:
#         return
#     m, n = y.shape
#     likelihood = 2*(y-x)
#     up = x-np.roll(x, [1, 0], [0, 1])
#     down = x-np.roll(x, [m-1, 0], [0, 1])
#     left = x-np.roll(x, [0, 1], [0, 1])
#     right = x-np.roll(x, [0, n-1], [0, 1])

#     if meth == "quadratic":
#         prior = 2*(up+down+left+right)
#     elif meth == "huber":
#         prior_up = np.multiply(np.less_equal(np.absolute(up), gamma), up) + \
#             np.multiply(np.greater(np.absolute(up), gamma),
#                         (gamma*up/np.abs(up)))
#         prior_down = np.multiply(np.less_equal(np.absolute(down), gamma), down) + np.multiply(
#             np.greater(np.absolute(down), gamma), (gamma*down/np.abs(down)))
#         prior_left = np.multiply(np.less_equal(np.absolute(left), gamma), left) + np.multiply(
#             np.greater(np.absolute(left), gamma), (gamma*left/np.abs(left)))
#         prior_right = np.multiply(np.less_equal(np.absolute(right), gamma), right) + np.multiply(
#             np.greater(np.absolute(right), gamma), (gamma*right/np.abs(right)))
#         prior = prior_up + prior_down + prior_left + prior_right
#     elif meth == "log":
#         prior_up = np.multiply(
#             gamma*up, np.reciprocal(gamma + np.absolute(up)))
#         prior_down = np.multiply(
#             gamma*down, np.reciprocal(gamma + np.absolute(down)))
#         prior_left = np.multiply(
#             gamma*left, np.reciprocal(gamma + np.absolute(left)))
#         prior_right = np.multiply(
#             gamma*right, np.reciprocal(gamma + np.absolute(right)))
#         prior = prior_up + prior_down + prior_left + prior_right

#     return (1-alpha)*likelihood + alpha*prior


# def routine(imgNoisy, alpha, gamma, step, thresh, meth):
#     old_model = np.copy(imgNoisy)
#     old_posterior = posterior(imgNoisy, old_model, meth, alpha)
#     posterior_val = []
#     posterior_val.append(posterior)
#     if meth == "huber" or meth == "log":
#         for i in range(30):
#             gradiant_img = gradiant(imgNoisy, old_model, meth, alpha, gamma)
#             new_model = old_model - step*gradiant_img
#             new_posterior = posterior(imgNoisy, new_model, meth, alpha, gamma)

#             if new_posterior < old_posterior:
#                 step = 1.1*step
#                 old_model = new_model
#                 old_posterior = new_posterior

#             else:
#                 step = 0.5*step
#             posterior_val.append(old_posterior)

#     else:
#         while step > thresh:
#             gradiant_img = gradiant(imgNoisy, old_model, meth, alpha)
#             new_model = old_model - step*gradiant_img
#             new_posterior = posterior(imgNoisy, new_model, meth, alpha)

#             if new_posterior < old_posterior:
#                 step = 1.1*step
#                 old_model = new_model
#                 old_posterior = new_posterior

#             else:
#                 step = 0.5*step
#             posterior_val.append(old_posterior)

#     return posterior_val, new_model


# def optimization_quadratic_prior(imageNoisy):
#     threshold = 1e-7
#     alpha_opt_list = []
#     alpha_opt_list.append(0)        
#     alpha = alpha_opt_list[0]
#     step = 1

#     cost_quad=[]
#     while alpha <= 0.2:  
#         post, denoised_model_quad = routine(imageNoisy, alpha, 1, step, threshold, "quadratic")
#         cost_quad.append(cost(denoised_model_quad, imageNoisy))
#         alpha+=0.005
#         alpha_opt_list.append(alpha)
        
#     alpha_opt_list = alpha_opt_list[:-1] 
#     print("alpha_opt_list: %s" %(alpha_opt_list))
    
#     alpha_opt = 0.125    
#     post, denoised_model_quad = routine(imageNoisy, 0.125, 1, step, threshold, "quadratic")
#     post = post[1:]
#     post_alpha1, denoised_model_quad_alpha1 = routine(imageNoisy, 1.2*alpha_opt, 1, step, threshold, "quadratic")
#     post_alpha2, denoised_model_quad_alpha2 = routine(imageNoisy, 0.8*alpha_opt, 1, step, threshold, "quadratic")

#     cost_noisy = cost(imageNoisy, denoised_model_quad)
#     cost_quad_denoised = cost(denoised_model_quad, denoised_model_quad)
#     cost_quad_alpha1 = cost(denoised_model_quad_alpha1, denoised_model_quad)
#     cost_quad_alpha2 = cost(denoised_model_quad_alpha2, denoised_model_quad)

#     print('RMSE for noisy image : %s' %(cost_noisy))
#     print('RMSE for denoised image using alpha=%s and gamma=%s for quad prior : %s' %(alpha_opt, 1,cost_quad_denoised))
#     print('RMSE for denoised image using alpha=%s and gamma=%s for quad prior : %s' %(1.2*alpha_opt, 1,cost_quad_alpha1))
#     print('RMSE for denoised image using alpha=%s and gamma=%s for quad prior : %s' %(0.8*alpha_opt, 1,cost_quad_alpha2))
# from preparation import img2tensor, imread, single_image_inference
import math
import torch
from basicsr.models import create_model
from basicsr.utils.options import parse
from modules.code.NAFNet_ImageDenoising import img2tensor, imread, single_image_inference

def process_image(imageArray):
    opt_path = 'options/test/SIDD/NAFNet-width64.yml'
    opt = parse(opt_path, is_train=False)
    opt['dist'] = False
    NAFNet = create_model(opt)
    # ==========
    img_input = imread(imageArray)
    print("img_input:", img_input)
    inp = img2tensor(img_input)
    print("inp:", inp)
    output_image = single_image_inference(NAFNet, inp)
    print("output_image:", output_image)
    return output_image