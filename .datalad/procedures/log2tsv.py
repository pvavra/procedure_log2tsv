# -*- coding: utf-8 -*-
"""
Created on Thu Aug  13 17:22:07 2020

@author: Judith Bomba 
"""
import os
import sys
import pandas as pd

inputs = sys.argv[:]
#print('inputs are: ',inputs)
input1 = sys.argv[1] #my_source 
input2 = sys.argv[2] #my_destination
print('will gather .log files from source:', input1, 'will convert to .tsv files stored in:', input2)

root = os.path.dirname(os.path.abspath('sourcedata'))


def merge_two_dicts(x, y):
    '''
    Given two dictionaries of the same depth, 
        merge them into a new dict as a shallow copy.
        https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-in-python-taking-union-o

    Parameters
    ----------
    x : dict
        first dictionary.
    y : dict
        second dictionary.

    Returns
    -------
    finaldict : TYPE
        combined dictionary.

    '''    
    finaldict = x.copy()
    finaldict.update(y)
    return finaldict

def logInfo_to_tsv(filenm, destination):
    '''
    Parameters
    ----------
    filenm : os path
        points to the appropriate file (..Info.log).
    filesource : os path
        DESCRIPTION.
    destination : os path
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    file = open(filenm, 'r')
    logfile = file.read().splitlines()
    
    ##############################################################################
    dict_var_set_1 = {}
    var_set_1 = ([(logfile[i].split())[0] for i in range(7)])
    var_inhalt_1 = ([(logfile[i].split())[2] for i in range(7)])
    
    for i in range(len(var_set_1)):
        k = var_set_1[i]
        val = var_inhalt_1[i]
        dict_var_set_1[k] = val
    #print(dict_var_set_1) #dictionary mit den ersten sechs Metavariablen
    
    vlastT = ((logfile[8261].split())[2])
    vfirstT = ((logfile[8260].split())[2])
    
    dict_var_set_1[(logfile[8261].split())[0]] = vlastT
    dict_var_set_1[(logfile[8260].split())[0]] = vfirstT
    ##############################################################################
    dict_var_set_2 = {}
    var_set_2 = logfile[8].split()
    
    for i in range(len(var_set_2)):
        k = var_set_2[i]
        for j in range(10,8260):
            val = (logfile[j].split())
            val1 = val[i]
            if j == 10:
                dict_var_set_2[k] = [val1]
            else:
                dict_var_set_2[k].append(val1)
    
    ##############################################################################
    finaldict = merge_two_dicts(dict_var_set_1,dict_var_set_2)
    #print(finaldict.keys())
    
    
    filename = "{}.tsv".format(filenm[-73:-4])
    df = pd.DataFrame.from_dict(finaldict)
    #print(df)
    df.to_csv('{}/{}'.format(destination,filename), sep = '\t', index=False)

def logPULS_to_tsv(filenm, destination):
    '''
    Parameters
    ----------
    file : os path 
        points to the appropriate file (..PULS.log).

    Returns
    -------
    None.

    '''
    file = open(filenm, 'r') #filenm
    logfile = file.read().splitlines()
    
    dict_var_set_1 = {}
    var_set_1 = ([(logfile[i].split())[0] for i in range(5)])
    var_inhalt_1 = ([(logfile[i].split())[2] for i in range(5)])
    
    for i in range(len(var_set_1)):
        k = var_set_1[i]
        val = var_inhalt_1[i]
        dict_var_set_1[k] = val
    dict_var_set_2 = {}
    var_set_2 = logfile[6].split()
    
    for i in range(len(var_set_2)):
        k = var_set_2[i]
        if i != (len(var_set_2)-1):
            for j in range(8,13418):
                val = (logfile[j].split())
                val1 = val[i]
                if j == 8:
                    dict_var_set_2[k] = [val1]
                else:
                    dict_var_set_2[k].append(val1)
        else:
            for j in range(8,13418):
                if len(logfile[j].split()) == 4:
                    val = (logfile[j].split())
                    val1 = val[i]
                    if j == 8:
                        dict_var_set_2[k] = [val1]
                    else:
                        dict_var_set_2[k].append(val1)
                else:
                    val = "NA"
                    if j == 8:
                        dict_var_set_2[k] = [val]
                    else:
                        dict_var_set_2[k].append(val)
    finaldict = merge_two_dicts(dict_var_set_1,dict_var_set_2)
    #print(finaldict.keys())
    
    
    filename = "{}.tsv".format(filenm[-73:-4])
    df = pd.DataFrame.from_dict(finaldict)
    #print(df)
    df.to_csv('{}/{}'.format(destination,filename), sep = '\t', index=False)
 
def logRESP_to_tsv(filenm, destination):
    '''
    Parameters
    ----------
    file : os path 
        points to the appropriate file (..RESP.log).

    Returns
    -------
    None.

    '''
    file = open(filenm, 'r') #filenm
    logfile = file.read().splitlines()
    dict_var_set_1 = {}
    var_set_1 = ([(logfile[i].split())[0] for i in range(5)])
    var_inhalt_1 = ([(logfile[i].split())[2] for i in range(5)])
    
    for i in range(len(var_set_1)):
        k = var_set_1[i]
        val = var_inhalt_1[i]
        dict_var_set_1[k] = val
    dict_var_set_2 = {}
    var_set_2 = logfile[6].split()
    
    for i in range(len(var_set_2)):
        k = var_set_2[i]
        if i != (len(var_set_2)-1):
            for j in range(8,13418):
                val = (logfile[j].split())
                val1 = val[i]
                if j == 8:
                    dict_var_set_2[k] = [val1]
                else:
                    dict_var_set_2[k].append(val1)
        else:
            for j in range(8,13418):
                if len(logfile[j].split()) == 4:
                    val = (logfile[j].split())
                    val1 = val[i]
                    if j == 8:
                        dict_var_set_2[k] = [val1]
                    else:
                        dict_var_set_2[k].append(val1)
                else:
                    val = "NA"
                    if j == 8:
                        dict_var_set_2[k] = [val]
                    else:
                        dict_var_set_2[k].append(val)
    finaldict = merge_two_dicts(dict_var_set_1,dict_var_set_2)
    #print(finaldict.keys())
    
    
    filename = "{}.tsv".format(filenm[-73:-4])
    df = pd.DataFrame.from_dict(finaldict)
    #print(df)
    df.to_csv('{}/{}'.format(destination,filename), sep = '\t', index=False)



filesource = os.path.join(root, input1)
#print(filesource)
destination = os.path.join(root, input2)

#print('#these are my files in root:\n',os.listdir(root))
#print('#these are my files in {}:\n'.format(input1),os.listdir('{}/my_source'.format(root))) #my_s
print('#these are my files in {} before converting:\n'.format(input2),os.listdir(destination)) #my_d
#print(root)

for file in os.listdir(filesource):
    if file.endswith('Info.log'):
        filename = (os.path.join(filesource,file))
        #print(filename)
        print(filename[-73:-4], "attempted to be processed")
        logInfo_to_tsv(filename, destination)
        
for file in os.listdir(filesource):
    if file.endswith('RESP.log'):
        filename = (os.path.join(filesource,file))
        #print(filename)
        print(filename[-73:-4], "attempted to be processed")
        logRESP_to_tsv(filename, destination)

for file in os.listdir(filesource):
    if file.endswith('PULS.log'):
        filename = (os.path.join(filesource,file))
        #print(filename)
        print(filename[-73:-4], "attempted to be processed")
        logPULS_to_tsv(filename, destination)

print('#these are the files in {} after converting:\n'.format(input2),os.listdir(destination))