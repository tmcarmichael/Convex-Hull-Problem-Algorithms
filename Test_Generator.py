"""

Generate Test Cases Python

Instructions: 

    o   Set record_num and dimension_num in main below
    o   Modify 'f_name' var to change output file 
    o   'TGen_Out.txt' is default output textfile

"""
import random

if __name__ == "__main__":
    # Set records and dimension number
    record_num = 50
    dimension_num = 3

    # Write header with #records, #dimensions
    header = str(record_num) + " " + str(dimension_num) + '\n'
    # data = [" ".join([str(random.randint(-10,10)) for _ in range(dimension_num)]) + '\n' for _ in range(record_num)]

    # Generate random data, format data
    data = [[random.randint(-10,10) for _ in range(dimension_num)] for _ in range(record_num)]
    data = [" ".join([str(r) for r in d])+'\n' for d in data]

    # Write to output file, can rename with f_name var below
    f_name = "TGen_Out.txt"
    file = open(f_name,"w")
    file.writelines(header)
    file.writelines(data)
    file.close()