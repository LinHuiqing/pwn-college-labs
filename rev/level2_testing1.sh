#!/bin/bash

# no. of vars ("argc > 215") = 215
# no. of dummy vars = 215-1 = 214
# EXPECTED_RESULT=6a6973
# hex to string => sij (215th arg)

cd /challenges/rev
run_cmd="./level2_testing1"
for i in {1..214}
do
    run_cmd+=" $i"
done
run_cmd+=" sij"
echo "run: $run_cmd"
output=$(eval "$run_cmd")
echo "$output"
