
user =

init:
	@./run_smth.sh


setup_deps:
	echo "hi there"


test:
	python -m pytest "tests/${user}"
