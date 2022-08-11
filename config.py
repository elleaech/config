from subprocess import run
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('config_file', help='Configuration file')
args = parser.parse_args()

config_file = open(args.config_file)

for line in config_file.readlines():
    print(line)
