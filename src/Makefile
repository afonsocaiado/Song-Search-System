# Makefile

all: expand

# Expand on the data to obtain more data through generalizing album genre
expand: clean_data
	python3 extend.py

# Remove unwanted columns and duplicate values
clean_data: combine
	python3 clean.py

# Combine all data to get a single file
combine: 
	python3 combine.py