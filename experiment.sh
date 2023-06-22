#!/bin/bash -e

REPEATS=10

rm -f results.txt
for i in `seq 1 $REPEATS`; do
GOAL=`python main.py 100 10`
echo "$GOAL" >> results.txt
done
done
done

pause
Start-Sleep 10
