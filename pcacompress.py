from cv2 import cv2
import numpy as np
import glob
import os
import imageio
import matplotlib.pyplot as plt 
from PIL import Image

# IMPORTING IMAGE USING SCIPY AND TAKING R,G,B COMPONENTS
def comp_2d(image_2d): # FUNCTION FOR RECONSTRUCTING 2D MATRIX USING PCA
                cov_mat = image_2d - np.mean(image_2d , axis = 1)
                eig_val, eig_vec = np.linalg.eigh(np.cov(cov_mat)) # USING "eigh", SO THAT PROPRTIES OF HERMITIAN MATRIX CAN BE USED
                p = np.size(eig_vec, axis =1)
                idx = np.argsort(eig_val)
                idx = idx[::-1]
                eig_vec = eig_vec[:,idx]
                eig_val = eig_val[idx]
                numpc = 600 # THIS IS NUMBER OF PRINCIPAL COMPONENTS, YOU CAN CHANGE IT AND SEE RESULTS
                if numpc <p or numpc >0:
                        eig_vec = eig_vec[:, range(numpc)]
                score = np.dot(eig_vec.T, cov_mat)
                recon = np.dot(eig_vec, score) + np.mean(image_2d, axis = 1).T # SOME NORMALIZATION CAN BE USED TO MAKE IMAGE QUALITY BETTER
                recon_img_mat = np.uint8(np.absolute(recon)) # TO CONTROL COMPLEX EIGENVALUES
                return recon_img_mat
def compress2(a):
        a_np = np.array(a)
        a_r = a_np[:,:,0]
        a_g = a_np[:,:,1]
        a_b = a_np[:,:,2]
        a_r_recon, a_g_recon, a_b_recon = comp_2d(a_r), comp_2d(a_g), comp_2d(a_b) # RECONSTRUCTING R,G,B COMPONENTS SEPARATELY
        recon_color_img = np.dstack((a_r_recon, a_g_recon, a_b_recon)) # COMBINING R.G,B COMPONENTS TO PRODUCE COLOR IMAGE
        recon_color_img = Image.fromarray(recon_color_img)
        return recon_color_img

def compression1():
    dir_path = r'D:\python_idleprog\Practice\frames'
    nf = len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))])
    for i in range(1, nf+1):
        fpath  = "D:\\python_idleprog\\Practice\\frames\\"
        a= imageio.imread(fpath+str(i)+".jpg")
        b = compress2(a)
        imageio.imwrite(f"D:\\python_idleprog\\Practice\\final_op\\{i}.jpg",b,format=None)
        

# def deleteFrames():
#     files = glob.glob('D:\\python_idleprog\\Practice\\frames\\*.jpg')
#     for f in files:
#         os.remove(f)


