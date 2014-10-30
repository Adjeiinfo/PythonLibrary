"""
Created on Fri Oct 24 13:21:36 2014
This library is a set of functions to be used as a cheatsheet


@author: KKouassi2
"""

"""
function name: fileconcat
input argument:
    Directory 
    file extention 
    The output file name 
    Specify wether the files are binary or not, default not binary
output:
    One file that is the concatonated file of all files in 
    the directory saved in the same directory 
    Return 0 if success 
    Return 1 if error
    
"""
import os  
def fileconcat(mydir,myext,myoutfile="output",isBinary=False):
    #the options for the file operation 
    if isBinary == True:
        readOption = 'rb'
        writeOption = 'wb'
    else:
        readOption = 'r'
        writeOption = 'w'
    
    #prepare the output file path
    outputpath = mydir +"/"+myoutfile +myext   
    
    #got all files' name in the directory 
    allfiles = os.listdir(mydir)
    #print allfiles
    #filter the files to the file to the extension
    filenames = []
    for files in allfiles:
        if files.endswith(myext):
            filenames.append(files)
    #print filenames

    if len(filenames)==0:
       raise("No files found")
       return 1 
    
    #append and and save file
    with open(outputpath, writeOption) as outfile:   
        for fname in filenames:
            fpath = mydir+"/"+fname
            print fpath
            with open(fpath,readOption) as infile:
                for line in infile:
                    outfile.write(line)
    return 0
