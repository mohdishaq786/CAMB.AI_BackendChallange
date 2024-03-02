set -m
python3 main.py &

huey_consumer tasks.huey

fg %1