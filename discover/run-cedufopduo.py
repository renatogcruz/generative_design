from src import job

jobDescription = {
	"jobName": "untitled",
	"inputsDef": [
		 { "name": "input00", "type": "continuous", "range": [10,20]},
		 { "name": "input01", "type": "continuous", "range": [5.0,10.0]},
		 { "name": "input02", "type": "continuous", "range": [5.0,10.0]},
		 { "name": "input03", "type": "continuous", "range": [1.0,4.0]},
		 { "name": "input04", "type": "continuous", "range": [1.0,4.0]},
		 { "name": "input05", "type": "continuous", "range": [0.0,1.0]},
		 { "name": "input06", "type": "continuous", "range": [0.0,1.0]},
		 { "name": "input07", "type": "continuous", "range": [2.0,5.0]},
		 { "name": "input08", "type": "continuous", "range": [2.0,5.0]},
		 { "name": "input09", "type": "continuous", "range": [2.0,7.0]},
		 { "name": "input10", "type": "continuous", "range": [2.0,7.0]},
		 { "name": "input11", "type": "continuous", "range": [10,20]},
		 { "name": "input12", "type": "continuous", "range": [10,20]},
		 { "name": "input13", "type": "continuous", "range": [0.0,1.5]},
		 { "name": "input14", "type": "continuous", "range": [0.0,1.5]},
		 { "name": "input15", "type": "continuous", "range": [1.0,5.0]},
		 { "name": "input16", "type": "continuous", "range": [4.0,10.0]},
		 { "name": "input17", "type": "continuous", "range": [0,30]},
		 { "name": "input18", "type": "continuous", "range": [0,30]},
		 { "name": "input19", "type": "continuous", "range": [0,30]},
		 { "name": "input20", "type": "continuous", "range": [0,30]},
		# { "name": "input2", "type": "categorical", "num": 5},
		# { "name": "input3", "type": "series", "length": 25, "depth": 3, "mutationRate": 0.5},
		# { "name": "input4", "type": "sequence", "length": 10, "mutationRate": 0.3}
		],
	"outputsDef": [
		 { "name": "weight", "type": "objective", "goal": "min"},
		 { "name": "powerOutput", "type": "objective", "goal": "max"},
		# { "name": "constraint1", "type": "constraint", "goal": "less than 1.0" }
		# { "name": "constraint2", "type": "constraint", "goal": "greater than 0" }
		# { "name": "constraint3", "type": "constraint", "goal": "equals 0.005" }
		],
	"algo": "GA",
	"algoOptions": {
		"numGenerations": 200,
		"numPopulation": 59,
		"mutationRate": 0.05,
		"saveElites": 10,
		"DOE": "random",
		# "DOE": ["_job name_", -1],
		},
	"jobOptions": {
		"screenshots": True
		}
	}

#job.createInputFile(jobDescription)
#job.run(jobDescription)