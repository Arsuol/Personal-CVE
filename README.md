# Personal-CVE
The Personal-CVE tool downloads CVSS files from https://nvd.nist.gov/
and stores them for offline search, consultation, and reference.  

Downloading the full CVSS database limits lookup to online CVE databases and 
earns (a lot of) time in the long run.

## Setup
The tool has some requirements.  
First, you need to install python.  
Then you can upgrade to python3, install pip and python libraries by launching 
the setup script:  
```
python script.py
```
The is a basic one, it uses the 'apt-get' package manager. If your distribution is not 
using 'apt-get', you can edit the script and change the 'package-manager' 
variable.

## Usage
Launch the personalcve script to start using the tool:
```
python3 ./bin/personalcve.py
```
The tool will print out the help information.  

### APIs
The tool uses multiple APIs to access data from Twitter, YouTube, and Reddit.  
If you want to use these functionalities, you need to copy the relevant 
configuration file '/conf/file.json_example' to '/conf/file.json' and edit it 
accordingly.
