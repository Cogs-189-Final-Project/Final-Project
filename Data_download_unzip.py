import requests
import zipfile
print('Downloading started')
url = 'http://bbci.de/competition/download/competition_iv/BCICIV_1calib_1000Hz_mat.zip'

username = 'xihong@ucsd.edu'
password = 'his7kaiPha'
req = requests.get(url, auth=(username,password))
filename = url.split('/')[-1]
 
with open(filename,'wb') as output_file:
    output_file.write(req.content)
print('Downloading Completed')

# Change to your path
print('Unzipping')
path_to_zip_file = '/home/xihong/BCICIV_1calib_1000Hz_mat.zip'
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall('/home/xihong/data')
print('Unzipping Completed')