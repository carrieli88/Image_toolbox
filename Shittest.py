"""
By default: "shittest is the main function under windows; "dumbtest" is the
main function under Linux.
Last modification: 06/05/2017
"""

<<<<<<< HEAD:Demos/Shittest.py
import glob 
import os 
from Pipeline import pipeline_tstacks, pipeline_zstacks
=======
import glob
import os
from src import Cell_extract

def ext_TS(path, TS_flags = 'TS', nsample = 5, DB = True):
    '''
    extract cells from a T stack.
    '''
    TS_list = glob.glob(path + '*'+TS_flags + "*.npz")




>>>>>>> 21fbd4c122ecb9b0265eefdf7f6e9d580d4fbc6a:Shittest.py

def main():
    """
    OK this part already works. 
    """
    hroot = 'D:\Data/'
    abspath = os.path.abspath(hroot)
    aq_date = '/2016-10-25\\'
    fd = abspath + aq_date
    fd_list = glob.glob(fd+'*TS*') # list all the tiff files in the folder
    tpflags = 'ZP'
    fd_list.sort(key=os.path.getmtime)  
    for work_folder in fd_list:
        work_folder = work_folder+ '\\'
        print(work_folder)
     
        pz = pipeline_tstacks(work_folder, tpflags)
        pz.tstack_zseries(deblur = 30, align = True, ext_all = False)
        
def shit1():
    """
    Correct a stack of shift
    How to add argc, argv like what we do in c/c++ ?
    """
    hroot = 'D:\Data/'
    abspath = os.path.abspath(hroot)
    aq_date = '/2016-12-07\\'
    fd = abspath + aq_date  
    fd_list = glob.glob(fd+'B2*ZD*')
    for work_folder in fd_list:
        work_folder += '\\'
        pt = pipeline_zstacks(work_folder, tpflags='ZD')
        pt.zstack_tseries(deblur = 30, align = True)
    
    
    
def shit2():
    """
    Correct a stack of shift
    How to add argc, argv like what we do in c/c++ ?
    """
    hroot = 'D:\Data/'
    abspath = os.path.abspath(hroot)
    aq_date = '/2016-12-07\\'
    fd = abspath + aq_date  
    fd_list = glob.glob(fd+'B2_HB_TS*')
    for work_folder in fd_list:
        work_folder += '\\'
        pt = pipeline_tstacks(work_folder, zp_flags='ZP')
        pt.tstack_zseries(deblur = 30, align = True, ext_all=False)
        
        




if __name__ == '__main__':
    shit2()

