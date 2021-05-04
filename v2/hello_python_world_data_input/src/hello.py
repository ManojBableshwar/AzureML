import argparse
import os
from datetime import datetime

print ("Hello Python World")

parser = argparse.ArgumentParser()
parser.add_argument("--sample_input_data", type=str)
parser.add_argument("--sample_input_string", type=str)

args = parser.parse_args()

print("sample_input_string: %s" % args.sample_input_string)
print("sample_input_data mounted path: %s" % args.sample_input_data)

print("mounted_path files: ")
arr = os.listdir(args.arg)
print(arr)

for filename in arr:
    print ("reading file: %s ..." % filename)
    with open(os.path.join(args.arg, filename), 'r') as handle:
        print (handle.read())

