# Sensetime Interview Test
A python script that read all the executable files in the specified directory, and then execute these programs one by one in lexicographic order. If there is an error, print the error and continue to execute the next file.

## Task Requirement
1. read all executable files in the specified directory
2. execute these files in alphabet order
3. if the executable file has the output, then print them to the terminal
4. if there is an error, print the error and continue to execute the next file

## Usage
### Requirement:
1. enviroment: Linux
2. lanuage: python3

### Run
1. open terminal
2. run the following command
##### test
```
python runExecutableFiles.py [specified directory path]
```
## Update log
1. Have a judgement of if the target directory exists.
2. Have a handle of OS exception, with execute errror
3. Generate a error list contains exectued failed files' path
4. Support parameter to specify target dir
5. Handle exception:
  ```
  a. empty dir
  b. target dir doesn't exist
  c. missing dir
  ```
 6. Use ```os.access(file,X_OK)``` in stead of linux command, judge the executability of a file directly.
 
