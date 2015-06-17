#!/usr/bin/env python
# encoding: utf-8

import glob
import os
import subprocess

'''
Remove bad 23andMe SNPs 
PLINK format
'''

for i in open("merge_list.txt"):
	i = i.strip()
	call = "./plink --bfile " + i + " --exclude 23andme_merged/merge-pass1-merge.missnp --make-bed --out " + i + "-filtered"
	subprocess.call(call,shell=True)

