from feature_labels import FeatureLabelList, filenamer

def cells(line, datatype):
	for cell in line.split(",")[1:]: #	skip Id
		cell = cell.strip()
		yield str(float(cell) - 2) if cell and datatype == "numeric" else cell
		
def convert_files(segments=("numeric", "cat", "date"), directory=str(), response_char=-4):
	with open(filenamer(directory, segments[0])) as fi:
		print("\tcounting rows . . .", end="\r")
		n_rows = sum(1 for line in fi) - 1
	file_n = dict((segment, index) for index, segment in enumerate(segments))
	if "categorical" not in segments:
		file_n["categorical"] = file_n["cat"]
	features = FeatureLabelList(segments=segments, directory=directory)
	files = tuple(open(filenamer(directory, segment)) for segment in segments)
	output_files = tuple(open(filenamer(directory, response, prefix=str()) , "w") for response in ("pass","fail"))
	for fi in files:
		next(fi) #	skip headers
	for row_n, lines in enumerate(zip(*files), 1):
		if not row_n % 100:
			print("\trow {} / {}  ({:.4}%)".format(row_n, n_rows, 100 * row_n / n_rows), end="\r")
		response = int(lines[file_n["numeric"]][response_char])
		current_cells = tuple(cells(*details) for details in zip(lines, segments))
		current_station = 0
		current_separator = str()
		current_station_values = list()
		for feature in features:
			if feature.station == current_station:
				current_station_values.append(next(current_cells[file_n[feature.datatype]]))
			else:
				if any(current_station_values):
					output_files[response].write("{}S{}:{}".format(current_separator, current_station, ",".join(current_station_values)))
					current_separator = ","
				current_station = feature.station
				current_station_values = [next(current_cells[file_n[feature.datatype]])]
		output_files[response].write("\n")
	print()
	for file_group in (files, output_files):
		for fi in file_group:
			fi.close()
