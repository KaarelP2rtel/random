#!/usr/bin/env python3
from multiprocessing import Pool
import argparse
import subprocess
import os.path
def convert(filename):
    path=os.path.abspath(filename)
    target=f"{os.path.splitext(path)[0]}.mobi"

    print(f"Converting {path}")
    subprocess.run(["ebook-convert", 
                    path,
                    target, 
                    "--filter-css",
                    "font-family,color,margin-left,margin-right,padding-left,padding-right" ,
                    "--mobi-file-type",
                    "both"],
                    stderr=open(os.devnull, 'wb'), stdout=open(os.devnull, 'wb'))
    print(f"Finished {target}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process epub files into mobi files')

    parser.add_argument('-t', '--threads',
                        metavar='N',
                        action='store',
                        default=1,
                        type=int,
                        help='how many threads to use (default: 1)')
    parser.add_argument('files',
                        nargs='*',
                        metavar='FILE',
                        help='files to convert')

    args = parser.parse_args()

    with Pool(args.threads) as p:
        p.map(convert, args.files)
