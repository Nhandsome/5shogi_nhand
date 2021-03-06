import argparse
import os
import sys
import re
import statistics
import matplotlib.pyplot as plt

def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)

def filter_csa_files(dir):
    ptn_rate = re.compile(r"^'(black|white)_rate:.*:(.*)$")

    kifu_count = 0
    rates = []
    for filepath in find_all_files(dir):
        rate = {}
        move_len = 0
        toryo = False
        try:
            for line in open(filepath, 'r', encoding='utf-8'):
                line = line.strip()
                m = ptn_rate.match(line)
                if m:
                    rate[m.group(1)] = float(m.group(2))
                if line[:1] == '+' or line[:1] == '-':
                    move_len += 1
                if line == '%TORYO':
                    toryo = True
            if not toryo or move_len <= 10:
                print('REMOVE')
                os.remove(filepath)
            else:
                kifu_count += 1
                rates.extend([_ for _ in rate.values()])
        except:
            os.remove(filepath)
            print('REMOVE')

    print('kifu count :', kifu_count)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='./data/csa_files')
    args = parser.parse_args()

    ptn_rate = re.compile(r"^'(black|white)_rate:.*:(.*)$")

    kifu_count = 0
    rates = []
    for filepath in find_all_files(args.dir):
        rate = {}
        move_len = 0
        toryo = False
        try:
            for line in open(filepath, 'r', encoding='utf-8'):
                line = line.strip()
                m = ptn_rate.match(line)
                if m:
                    rate[m.group(1)] = float(m.group(2))
                if line[:1] == '+' or line[:1] == '-':
                    move_len += 1
                if line == '%TORYO':
                    toryo = True
            if not toryo or move_len <= 10:
                print('REMOVE')
                os.remove(filepath)
            else:
                kifu_count += 1
                rates.extend([_ for _ in rate.values()])
        except:
            os.remove(filepath)
            print('REMOVE')

    print('kifu count :', kifu_count)