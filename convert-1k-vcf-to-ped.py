import glob
import subprocess
import os

vcfs = glob.glob("*.vcf")

pops = "-population FIN -population GBR -population CHS -population CDX -population PUR -population IBS -population ACB -population GWD -population ESN -population MSL -population -CEU -population YRI"

for i in vcfs:
#	print i
	call = "echo \"perl vcf_to_ped_convert.pl -vcf " + i 
	call += " -sample integrated_call_samples_v3.20130502.ALL.panel -region "
	ia = i.split(".")[1].replace("chr","")
	call += ia + ":1-249240543 " + pops + "\"|qsub -V -S /bin/bash -cwd -j y -r y -q all.q -N vcf" + ia
	#subprocess.call(call,shell=True,cwd=os.getcwd())
	print call

