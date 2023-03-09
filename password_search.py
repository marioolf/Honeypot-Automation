# -*- coding: utf-8 -*-
import argparse

parser = argparse.ArgumentParser(description='Search for lines containing "text=" in a log file and print everything up to the first "&". If the line also contains "password", print everything to the right of "password".')
parser.add_argument('-f', '--file', type=str, required=True, help='path to log file')
args = parser.parse_args()

print('usuario contraseña')

with open(args.file, 'r') as file:
    for line in file:
        if 'text=' in line:
            text = line[line.index('text=')+len('text='):line.index('&')].strip()
            if 'password' in line:
                password = line[line.index('password=')+len('password='):].strip()
                print(text + ' ' + password.rstrip("'"))
            else:
                print(text)

