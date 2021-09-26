
import re
import os
import json
try: import requests
except ModuleNotFoundError: os.system("python -m pip install requests &> /dev/null")
try: import bs4
except ModuleNotFoundError: os.system("python -m pip install bs4 &> /dev/null")
import requests as req
from time import sleep as waktu
from bs4 import BeautifulSoup as parser
koneksi_error=(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout)
def kembali(kata,fuck=None):
	print(kata)
	waktu(2)
	fuck() if fuck is not None else exit()