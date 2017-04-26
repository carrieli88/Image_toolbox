"""
Last update: 04/25/2016
Test affine transformation
"""


import os
from src.preprocessing.z_dense import z_dense_ref, z_dense_construct
import numpy as np
import matplotlib.pyplot as plt
from src.Cell_extract import Cell_extract
import src.preprocessing.tifffunc as tf
import src.preprocessing.Affine as Affine
from src.visualization.brain_navigation import slice_display

global_datapath = '/home/sillycat/Programming/Python/Image_toolbox/data_test/'


def dumb1():
    '''
    0. Load two slices, first one is the matched slice in the ZD stack, second one is the second slice in the ts stack.
    1. Load all the retrieved cells
    2. Apply the affine transformation inversely to the cells tracked from the T-slice
    3. Cross align the positions of the T-cells with those in the Z-stacks.
    '''
    # read the Z-slices and the t-slices
    TS_slice9 = 'TS_folder/rg_A1_FB_TS_ZP_9.tif'
    TS_slice14 = 'TS_folder/rg_A1_FB_TS_ZP_14.tif'
    ZD_stack = 'A1_FB_ZD.tif'
    zstep = 4
    Z_slices = tf.read_tiff(global_datapath+ZD_stack, np.array([9,14])*zstep)
    T_slice9 = tf.read_tiff(global_datapath+TS_slice9, 1)
    T_slice14 = tf.read_tiff(global_datapath + TS_slice14, 1)

    # load the cell extraction data 

    TS14 = np.load(global_datapath+'TS_14.npz')
    coord_14, f_14 = TS14['xy'], TS14['data'] # split the coordinates and data
    # do the similar thing for slice 9
    TS9= np.load(global_datapath+'TS_9.npz')
    coord_14, f_14 = TS9['xy'], TS9['data'] # split the coordinates and data
     


    ref_im = tf.read_tiff(global_datapath+'ref_crop.tif')
    rot30_im = tf.read_tiff(global_datapath+'rot30_crop.tif')
    rotpt_im = tf.read_tiff(global_datapath+'rot30_crop_pt.tif')
    compstack = np.array([ref_im,rot30_im, rotpt_im]).astype('float64')

    CE = Cell_extract(compstack)
    CE.stack_blobs(msg = True)
    #CE.save_data_list(global_datapath+'ref_rot')
    coord_list= CE.get_coordinates()
    print(coord_list.keys())
    coord_ref = coord_list['s_000'] # flip the original coordinates
    coord_rot = np.fliplr(coord_list['s_001'])
    coord_pts = coord_list['s_002']
    af_mat, af_vec = Affine.aff_read(global_datapath + 'sliceReg.txt')
    af_mat = af_mat[0]
    af_vec = af_vec[0]

    raf_mat, raf_vec = Affine.reverse_trans(af_mat, af_vec)
    afc_rot = np.fliplr(Affine.pixel_transform(coord_rot, raf_mat, raf_vec))
    fig_comp= slice_display([coord_ref,afc_rot ])
    print("Cells plotted!")
    fig_comp.savefig(global_datapath+'ref_display')
#     fig_rot.savefig(global_datapath+'rot_display')


if __name__ == '__main__':
    dumb1()# 
