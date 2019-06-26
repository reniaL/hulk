# -*- coding: utf-8 -*-
import zipfile


def write():
    source_paths = ["/data/temp/upload/test1.txt", "/data/temp/upload/test2.txt"]
    zip_path = "/data/temp/pack/target/as.zip"
    with zipfile.ZipFile(zip_path, 'w') as zip:
        for path in source_paths:
            zip.write(path)
            print("read file: " + path)
    print("write to zip done.")


def read():
    path = "/data/temp/pack/target/as.zip"
    with zipfile.ZipFile(path, 'r') as zip_file:
        for info in zip_file.infolist():
            print('{}, {}'.format(info.filename, info.CRC))


if __name__ == '__main__':
    read()
    # write()
