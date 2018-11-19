'''
A python script that read all the executable files in the specified directory
and then execute these programs one by one in lexicographic order.
If there is an error, print the error and continue to execute the next file.
Time: 11-16-2018
Author: Tongyu Guo
'''

import os
import sys
import subprocess

'''
used to judge if a file is a executable file by "ll -x command"
'''
def judge_executable(dirname):
	judge_executable=os.access(dirname,os.X_OK)
	#judge_executable=os.system("ls -p -F "+dirname+" | grep -q '*' ")
	#&&("file"+file_path+" | grep -q \"executable\"")
	return judge_executable
'''
Used to traversing all the executable files in specified directory and sort these in lexicographic order
return a list contains all the executable file path
'''
def traversing_dir(dirname):

	result = []#All files

	for maindir, subdir, file_name_list in os.walk(dirname):

		#print("1:",maindir) #Current home directory
		#print("2:",subdir) #All directories under the current home directory
		#print("3:",file_name_list)  #All files in the current home directory

		for filename in file_name_list:
			file_path = os.path.join(maindir, filename)#Merge into one full path
			#file_type= os.path.splitext(apath)[0]  #Get the file suffix [0] to get something other than the file name
			if judge_executable(file_path)==True:
				result.append(file_path)

	return sorted(result) #return a list contains all the executable file path which sorted in lexicograhic orderr

'''
main module
'''
if __name__ == "__main__":
	dirname = sys.argv[1]
	#dirname=input()
	try:
		os.listdir(dirname)
	except IOError as e1:
		print("File error:"+str(e1))

	if not os.listdir(dirname):
		print("Exception:this is an empty directory")
		exit(1)

	sorted_result=traversing_dir(dirname)

	errorList=[]

	for i in range(len(sorted_result)):
		try:
			print("-----Executing: ",sorted_result[i],"-----")
			stdout=subprocess.call(sorted_result[i])
			print("\n-----Executing Successfully-----\n")
		except OSError as e:
			errorList.aapend(sorted_result[i])
			print("Execution failed when running",sorted_result[i]," Error:",e)
