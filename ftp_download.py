import sys
import os

file1 = sys.argv[1]
ftp_file = open(file1, "r")
ftps = ftp_file.readlines()
os.system("mkdir ftp_downloads")
log = open("logfile.txt", "w")
for ftp in ftps:
	os.system("wget -P ftp_downloads/ " + ftp)
	log = open("logfile.txt", "a")
	log.write(ftp)
log.close()
ftp_file.close()

# python ftp_download.py <ftpfilepaths>
