#!/bin/bash

export owklr=$(echo "6161736e6261" | xxd -p -r)
cd /challenges/rev
./level3_teaching1
