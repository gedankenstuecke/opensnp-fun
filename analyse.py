#!/usr/bin/env python
# encoding: utf-8

import glob
import os
import subprocess

'''
Convert 23andMe files to 
PLINK format
'''

def twenty3_and_me_files():
	"""Return the opensnp files that are 23 and me format"""
	all_twenty3_and_me_files= glob.glob('../opensnp_datadump.current/*.23andme.txt')
	fifteen_mb = 15 * 1000 * 1000
	non_junk_files = [path for path in all_twenty3_and_me_files if os.path.getsize(path) > fifteen_mb]
	return non_junk_files


def run_plink_format(usable_files):
	"""Reformat the 23andMe files into plink binary stuff"""
	try:
		os.mkdir("00-23andme_plink")
	except:
		print "can't create output-folder"
		exit
	for f in usable_files:
		# gid is the genotype-ID
		gid = f.split("/")[-1].split("_")[1].replace("file","")
		# converts the genotyping file to plink format, using the gid as sample name
		call = "./plink --23file "+ f + " F" + gid + "ID" + gid + "I 1"
		call += " --out 00-23andme_plink/genotypeid_" + gid
		print "convert gid " + gid
		subprocess.call(call,shell=True)

def merge_plink():
	"""Merge the Files, will crash at first and then needs to do some weird corrections"""
	try:
		os.mkdir("01-23andme_merged")
	except:
		print "damn, can't create output-again"
		exit
	allbeds = glob.glob("00-23andme_plink/*.bed")
	start_bed = allbeds[0]
	list_bed = allbeds[1:]
	listhandle = open("merge_list.txt","w")
	for i in list_bed:
		listhandle.write(i+"\n")



usable_files = twenty3_and_me_files()
run_plink_format(usable_files)
