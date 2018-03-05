# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 15:00:51 2018

@author: Sean
"""
import string
def get_file_name(filename):
    """
    get all line name which is included in filename，
    by "DIR *.*  /B >LIST.TXT" command
    """
  
    file_fp = open(filename, 'r')
    list_name = file_fp.readlines()
    return list_name
    
def write_data(list_name, fileout):
    """
    read data from file
    """
    
    file_wt = open(fileout, 'w')
    for i in range(0,len(list_name)):
        filestr = list_name[i].replace("\n","")
        file_rd = open(filestr, 'r')
        list_dat = file_rd.readlines()
        
        for j in range(0,len(list_dat)):
            linestr = filestr.replace(".txt","") + '\t' + list_dat[j]
            file_wt.writelines(linestr)
            
allname = get_file_name('LIST.TXT')
write_data(allname, 'add_line_name.txt')
            
        

