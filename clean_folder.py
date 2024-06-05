import shutil
import os

def clean_record_path(path):
    shutil.rmtree(path)
    os.mkdir(path)