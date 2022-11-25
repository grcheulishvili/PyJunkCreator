import argparse
import sys
#import os
#import pathlib
import time

def no_args():
    message = """
    PyJC - Python Junk Creator

    Argumentebis gareshe...
    Operacia gauqmda.

    scadet jc -h daxmarebistvis"""
    print(message)
    sys.exit(0)

parser = argparse.ArgumentParser(description = """
PyJC - Python Junk Creator.
Sheqmnilia gamousadegari failebis generirebistvis.
""")
parser.add_argument('filename', nargs='*',type=str, help = "failis saxeli. nagulisxmevi formati aris sicariele")
parser.add_argument('--size', type=int, help = 'zoma baitebshi. carieli argumentis shemtxvevashi zoma = 1 byte' )
ns = parser.parse_args()

filename = str(ns.filename)
if len(sys.argv)==1:
   no_args()

size = 0
if ns.size == None:
    size = 1
else:
    size = int(ns.size)

#failshi chawera
junk_file = open(filename, "w+")

run_time = time.perf_counter()
char = """ """ * 1024

for i in range(size):
    junk_file.write(char)
junk_file.close()

print("\nOperacia dasrulebulia.")
print("dro: ", time.perf_counter() - run_time,"wami\n")
