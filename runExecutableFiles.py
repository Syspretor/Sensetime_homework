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
used to judge if a file is a executable file by os.access(file,X_OK)
@:param (String) filepath: the full path of the file need judging it's executability
'''
def judge_executable(filepath):
	ifExecutable=os.access(filepath,os.X_OK)#judge the executability of the file, if it can be executed, it will return True
	return ifExecutable
'''
Used to traversing all the executable files in specified directory and sort these in lexicographic order
return a list contains all the executable file path in lexicographic order
@:param （String)dirname: the full path of target specified directory need traversing
'''
def traversing_dir(dirname):

	result = [] #All files

	for maindir, subdir, file_name_list in os.walk(dirname):#traversing the target dir

		#print("1:",maindir) #Current home directory
		#print("2:",subdir) #All directories under the current home directory
		#print("3:",file_name_list)  #All files in the current home directory

		for filename in file_name_list:
			file_path = os.path.join(maindir, filename)#Merge into one full path
			if judge_executable(file_path)==True:
				result.append(file_path)

	return sorted(result) #return a list contains all the executable file path which sorted in lexicograhic orderr

'''
main function, read the target specific dir from parameter
'''
if __name__ == "__main__":
	dirname = sys.argv[1]
	try:#handle the exception of unexisted dir
		os.listdir(dirname)
	except IOError as e1:
		print("File error:"+str(e1))

	if not os.listdir(dirname):#handle exception of the empty dir, exit and throw exception 1
		print("Exception:this is an empty directory")
		exit(1)

	sorted_result=traversing_dir(dirname)#generate list contains all the exxcuted files in target specified dir in lexicographic order

	errorList=[]#a list contains all the executed failed files

	for i in range(len(sorted_result)):
		try:#handle the exception of executing
			print("-----Executing: ",sorted_result[i],"-----")
			stdout=subprocess.call(sorted_result[i])
			print("\n-----Executing Successfully-----\n")
		except OSError as e:
			errorList.aapend(sorted_result[i])
			print("Execution failed when running",sorted_result[i]," Error:",e)
