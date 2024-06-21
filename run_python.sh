#!/bin/bash
#! chmod +x run_python.sh
#! ./python.sh

mkdir -p ../test_outputs

module load anaconda; conda activate 

cd /hpc/projects/group.czii/phil.smoot/test_project/scripts

date; test_start_time=`date +%s`

python3 shellout.py

date; _end_time=`date +%s`

echo execution time was `expr $test_end_time - $test_start_time` s.
 