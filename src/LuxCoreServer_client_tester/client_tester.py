import requests

cfg = {}
scn = {}

with open('simple/simple.cfg', 'r') as cfg_file:
	for line in cfg_file:
		line = line.strip()
		if line.startswith("#"): continue 

		k, v = line.split("=", 1)
		cfg[k.strip()] = v.strip()

with open('simple/simple.scn', 'r') as cfg_file:
	for line in cfg_file:
		line = line.strip()
		if line.startswith("#"): continue 

		k, v = line.split("=", 1)
		scn[k.strip()] = v.strip()


requests.post('http://localhost:5000/config/',json=cfg)
requests.post('http://localhost:5000/scene/',json=scn)