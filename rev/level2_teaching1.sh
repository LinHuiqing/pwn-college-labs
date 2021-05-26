#!/bin/bash

# no. of vars ("argc > 793") = 793
# no. of dummy vars = 793-1 = 792
# EXPECTED_RESULT=697978
# hex to string => xyi (793rd arg)

cd /challenges/rev
run_cmd="./level2_teaching1"
for i in {1..792}
do
    run_cmd+=" $i"
done
run_cmd+=" xyi"
echo "run: $run_cmd"
output=$(eval "$run_cmd")
echo "$output"
