#!/bin/bash

# env var=owklr
# EXPECTED_RESULT=61 62 6e 73
# "skipped 2 bytes" and "var_15 = *(var_20 + 8)" which means skip 8 bytes INCLUDING 'owklr=' => 616161626e73

export owklr=$(echo "616161626e73" | xxd -p -r)
exec /challenges/rev/level3_teaching1
