#!/usr/bin/python3

import os
import sys
import regex

# Get current file name
sys.stderr.write(f'Current input file: {os.environ["mapreduce_map_input_file"]}\n')

# input comes from STDIN (standard input)
for line in sys.stdin:
    # Update some counter from worker
    # reporter:counter:<group>,<counter>,<amount>
    sys.stderr.write('reporter:counter:Custom Counter,My Super INT Counter,1\n')

    # remove leading and trailing whitespace
    line = line.strip().lower()
    line = regex.sub(r'[\P{L}]', ' ', line)
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        if word != ' ':
            print('%s\t%s' % (word, 1))
