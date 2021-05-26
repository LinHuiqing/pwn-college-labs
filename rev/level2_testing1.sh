#!/bin/bash

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
