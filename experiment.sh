#!/bin/bash -e

REPEATS=20
P_TEMP="0.7 0.9"
P_COOL="0.5 0.9"

rm -f results/results4.txt
for i in `seq 1 $REPEATS`; do
for temp in $P_TEMP; do
for cool in $P_COOL; do
rhc=`python random_hill_climbing.py 100`
hc=`python hill_climbing.py 100`
ts=`python tabu_search.py 100 5`
tsb=`python tabu_search_backtrack.py 100 5`
sa=`python simulated_annealing.py 100 5 $temp $cool`

echo "random_hill_climbing $rhc" >> results/results4.txt
echo "hill_climbing $hc" >> results/results4.txt
echo "tabu_search $ts" >> results/results4.txt
echo "tabu_search_backtrack $tsb" >> results/results4.txt
echo "simulated_annealing $sa" >> results/results4.txt
done
done
done
done
