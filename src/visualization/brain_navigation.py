'''
Created on 04/25/2017 by Dan.
Last update: 04/26/2017
Function: navigate a stack of images and display cells across the stack.
'''
import sys
import numpy as np
import matplotlib.pyplot as plt

global_ccode = 'bgrcmyk'


def slice_display(slice_blobs, ref_image = None):
    '''
    slice_blobs: a 2-D array specifying the cell coordinates
    ref_image: a 2-D array specifying the reference image.
    Adding multi-slice plotting:
    '''
    if ref_image is None:
        figd = plt.figure(figsize= (6.,4.) )
        ax = figd.add_subplot(111)
    else:
        ny, nx = ref_image.shape
        figd = plt.figure(figsize = (6., 6.*ny/nx))
        ax = figd.add_subplot(111)
        ax.imshow(ref_imagei, cmap = 'Greys_r')
        ax.set_xlim([0,nx])
        ax.set_ylim([0,ny])
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

    if isinstance(slice_blobs, list):
        ii = 0
        NS = len(slice_blobs)
        for fr in slice_blobs:
            ax.scatter(fr[:,1], fr[:,0], c = global_ccode[ii], s = 11*(NS-ii))
            ii+=1
    else:
        ax.scatter(slice_blobs[:,1], slice_blobs[:,0], c='g', s = 6)
    figd.tight_layout()
    return figd


def slices_compare(im_slice1, im_slice2):
    '''
    imshow two slices side by side.
    '''
    y1, x1 = im_slice1.shape
    y2, x2 = im_slice2.shape

    figc = plt.figure(figsize = ((x1+x2)/(y1+y2)*6., 6.))
    ax1 = figc.add_subplot(121)
    ax2 = figc.add_subplot(122)
    ax1.imshow(im_slice1, cmap = 'Greys_r')
    ax1.set_xlim([0, x1])
    ax1.set_ylim([0, y1])
    ax1.get_xaxis().set_visible(False)
    ax1.get_yaxis().set_visible(False)

    ax2.imshow(im_slice2, cmap = 'Greys_r')
    ax2.set_xlim([0, x2])
    ax2.set_ylim([0, y2])
    ax2.get_xaxis().set_visible(False)

    figc.tight_layout()
    return figc
    ax2.get_yaxis().set_visible(False)
