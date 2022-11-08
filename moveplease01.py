#!/usr/bin/env python3

#import libraries
import shutil
import os

def main():
    #to start from this working directory
    os.chdir('/home/student/mycode/')
    # to move the file to particular destination
    shutil.move('raynor.obj', 'ceph_storage/')
   #prompt for new name of the file
   
    
    xname = input('What is the new name for kerrigan.obj? ') # collect string input from the user
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)  # moving kerrigan.obj into
                                                                       # ceph_storage/ with new name
main()
