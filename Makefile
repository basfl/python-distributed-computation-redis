setup: requirements.txt
	pip install -r requirements.txt

main: 
	cd ./app && python main.py

dev: 
	cd ./worker && python worker.py