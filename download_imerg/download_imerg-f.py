'''
Created on 2023-06-30
author: @msuarez

Ejemplo de ejecución:
python3 download_imerg-f.py 'subset_GPM_3IMERGHH_06_20230630_154342_.txt' '/home/msuarez/Documents/IMERG-Final/20200325'
'''

import pandas as pd
import numpy as np
import xarray as xr
import requests 
import argparse

parser = argparse.ArgumentParser(prog="Descargar datos IMERG-F, download_imerg-f.py")

parser.add_argument("txt_path"   , help="Path al txt, ejemplo: /home/msuarez/subset_GPM_3IMERGHH_06_20230627_010541_.txt")
parser.add_argument("output_path", help="Path al directorio de salida, ejemplo: /home/msuarez/Documents/")

args = parser.parse_args()

ds = pd.read_csv(args.txt_path, header = None, sep = ' ')[0]

# Do not forget to add .netrc file in root dir of colab. printing `result` should return status code 200
for file in range(len(ds)):
    URL = ds[file]
    print('Descargando ',URL)
    result = requests.get(URL)
    filename = args.output_path +'/'+ URL.split('?')[0].split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(result.content)

print('******************************')
print('******************************')
print('***** Proceso Finalizado *****')
print('******************************')
print('******************************')
