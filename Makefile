
run.task_1_v1:
	@python task_1/task_1_v1.py -m=4 -n=5

run.task_1_v2:
	@python task_1/task_1_v2.py -m=4 -n=5

run.task_2:
	@python task_2/task_2.py -c=./task_2/circle.txt -p=./task_2/points.txt

run.task_3:
	@python task_3/task_3.py -v=./task_3/values.json -t=./task_3/tests.json -r=./task_3/report.json

run.all: run.task_1_v1 run.task_1_v2 run.task_2 run.task_3 run.task_4

run.task_4:
	@python task_4/task_4.py -n 1 2 3

tests:
	@pytest .