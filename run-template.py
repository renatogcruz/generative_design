from src import job

jobDescription = {
	"jobName": "untitled",
	"inputsDef": [
		# { "name": "input1", "type": "continuous", "range": [0,10]},
		# { "name": "input2", "type": "categorical", "num": 5},
		# { "name": "input3", "type": "series", "length": 25, "depth": 3, "mutationRate": 0.5},
		# { "name": "input4", "type": "sequence", "length": 10, "mutationRate": 0.3}
		],
	"outputsDef": [
		# { "name": "objective1", "type": "objective", "goal": "min"},
		# { "name": "objective2", "type": "objective", "goal": "max"},
		# { "name": "constraint1", "type": "constraint", "goal": "less than 1.0" }
		# { "name": "constraint2", "type": "constraint", "goal": "greater than 0" }
		# { "name": "constraint3", "type": "constraint", "goal": "equals 0.005" }
		],
	"algo": "GA",
	"algoOptions": {
		"numGenerations": 10,
		"numPopulation": 10,
		"mutationRate": 0.05,
		"saveElites": 2,
		"DOE": "random",
		# "DOE": ["_job name_", -1],
		},
	"jobOptions": {
		"screenshots": True
		}
	}

job.createInputFile(jobDescription)
# job.run(jobDescription)