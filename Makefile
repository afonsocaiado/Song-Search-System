# Makefile

all: expand

# Expand on the data to obtain more data through generalizing album genre
expand: clean_data
	python3 src/extend.py

# Remove unwanted columns and duplicate values
clean_data: combine
	python3 src/clean.py

# Combine all data to get a single file
combine: 
	python3 src/combine.py

# Delete all temporary files
#clean:
#	rm dataset/clean.csv dataset/combined.csv