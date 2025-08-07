.PHONY: etl

setup:
	pip install -r requirements.txt

notebook:
	jupyter notebook

etl:
	python etl/load_to_postgres.py