import sys
import os

file1 = sys.argv[1]
gdc_manifest_file = open(file1, "r")
gdc_data = gdc_manifest_file.readlines()
os.system("mkdir gdc_downloads")
log = open("logfile.txt", "w")
for data in gdc_data[1:]:
	data_ls = data.split("\t")
	gdc_id = data_ls[0]
	os.system("wget https://api.gdc.cancer.gov/data/"+gdc_id+" -O gdc_downloads/"+data_ls[1])
	log = open("logfile.txt", "a")
	log.write(gdc_id+"\n")
log.close()
gdc_manifest_file()

# python gdc_download.py <gdc_manifest.txt>
