VENV = pri_venv
PYTHON = python 
PIP = pip 

combineOutput = dataset/Processed-Files/
combineExec = pipeline/combine/



cleanOutput = dataset/Clean-Files/
cleanExec = pipeline/clean/

#TARGETS

.PHONY: all

all: $(VENV)/bin/activate fcombine fclean
	@echo "the code is running..."

fcombine:
	@echo "combining"
	@ $(PYTHON) $(patsubst $(combineOutput)%.csv, $(combineExec)%.py, $@)

fclean:
	@echo "cleaning"
	@ $(PYTHON) $(patsubst $(cleanOutput)%.csv, $(cleanExec)%.py, $@)
	