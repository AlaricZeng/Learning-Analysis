import csv
class FileOperation(object):
	def __init__(self, read_file_path, write_file_path):
		self.content = list()
		self.read_file_path = read_file_path
		self.write_file_path = write_file_path
	
	def ReadFile(self, data_delimiter, skipinitialspace_or_not):
		with open(self.read_file_path, 'rt') as f:
			reader = csv.reader(f, delimiter = data_delimiter, skipinitialspace=skipinitialspace_or_not)
			cols = next(reader)

			for line in reader:
				if line[0] != "":
					self.content.append(line)

	def WriteFile(self, file_content):
		with open(self.write_file_path, 'w') as f:
			for i in range(len(file_content)):
				for j in range(len(file_content[i]) - 1):
					f.write("%s," % file_content[i][j])
				f.write("%s\n" % file_content[i][len(file_content[i]) - 1])

	def GetContent(self):
		return self.content

