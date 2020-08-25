# Short in ascending order
# Please replace names_file & output_file with your filenames:

with open("names_file", 'r') as file, open("output_file", "w") as outFile:
	names = [name for name in file]
	names.sort()
	outFile.write("".join(name for name in names))

	

