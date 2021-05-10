import argparse
import os
from datetime import datetime

print ("Hello Python World")

parser = argparse.ArgumentParser()
parser.add_argument("--sample_input_data", type=str)
parser.add_argument("--sample_input_string", type=str)
parser.add_argument("--sample_output_data", type=str)

args = parser.parse_args()

print("sample_input_string: %s" % args.sample_input_string)
print("sample_input_data mounted path: %s" % args.sample_input_data)
print("sample_output_data mounted path: %s" % args.sample_output_data)

print("mounted_path files: ")
arr = os.listdir(args.sample_input_data)
print(arr)

for filename in arr:
    print ("reading file: %s ..." % filename)
    with open(os.path.join(args.sample_input_data, filename), 'r') as handle:
        print (handle.read())

cur_time = datetime.now()

cur_time_str=cur_time.strftime("%b-%d-%Y-%H-%M-%S")
    
print("files in sample_output_data mounted path: %s before:" % args.sample_output_data)
arr = os.listdir(args.sample_output_data)
print(arr)

print("Writing file: %s" % os.path.join(args.sample_output_data,"file-" + cur_time_str + ".txt"))
with open(os.path.join(args.sample_output_data,"file-" + cur_time_str + ".txt"), "wt") as text_file:
    print(f"Logging date time: {cur_time_str}", file=text_file)

print("files in sample_output_data mounted path: %s after:" % args.sample_output_data)
arr = os.listdir(args.sample_output_data)
print(arr)
