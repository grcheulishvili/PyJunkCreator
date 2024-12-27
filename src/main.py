import argparse
import sys
#import os
#import pathlib
import time

def no_args():
    message = """
    PyJC - Python Junk Creator

    Arguments not provided...
    Canceling operation.

    Try jc -h for help"""
    print(message)
    sys.exit(0)

parser = argparse.ArgumentParser(description = """
PyJC - Python Junk Creator.
Created for quickly generating junk files of large size.
""")
parser.add_argument('filename', nargs='*',type=str, help = "Filename. Default format is nothing")
parser.add_argument('--size', type=int, help = 'Size in bytes. Default value  is 1 byte' )
ns = parser.parse_args()

filename = str(ns.filename)
if len(sys.argv)==1:
   no_args()

size = 0
if ns.size == None:
    size = 1
else:
    size = int(ns.size)

#Writing in file
junk_file = open(filename, "w+")

run_time = time.perf_counter()
char = """ """ * 1024

for i in range(size):
    junk_file.write(char)
junk_file.close()

print("\nOperation completed.")
print("Time: ", time.perf_counter() - run_time,"sec\n")
