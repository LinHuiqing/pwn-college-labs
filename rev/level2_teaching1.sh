#!/bin/bash

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
