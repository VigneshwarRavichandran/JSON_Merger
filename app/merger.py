import json
import glob
import os
import timeit


class Merger(object):
  def __init__(self, read_base_dir, read_file_prefix, output_base_dir, output_file_prefix, max_file_size=1024):
    self.data = []
    self.merged_data = {}
    self.read_base_dir = read_base_dir
    self.read_file_prefix = read_file_prefix
    self.output_base_dir = output_base_dir
    self.output_file_prefix = output_file_prefix
    self.max_file_size = max_file_size

  def read_files(self, base_dir, prefix):
    filenames = glob.glob(os.path.join(base_dir, prefix + '*.json'))
    for filename in filenames:
      with open(filename, 'r') as json_file:
        json_file_data = json.load(json_file)
      self.data.append(json_file_data)

  def merge_files(self):
    for value in self.data:
      if self.merged_data:
        for key, single_data in value.items():
        	if isinstance(single_data, list):
						if key in self.merged_data.keys():
							self.merged_data[key].extend(single_data)
						else:
							self.merged_data[key] = single_data
      else:
        self.merged_data.update(value)

  def write_file(self, output_dir, prefix):
    if not (os.path.isdir(output_dir)):
    	# Using mkdir creates directory recursively
    	os.makedirs(output_dir)
  	counter = str(len(self.data) + 1)
  	with open(os.path.join(output_dir, prefix + counter + '.json'), 'w') as output_file:
  		json.dump(self.merged_data, output_file)

  def execute(self):
	  self.read_files(self.read_base_dir, self.read_file_prefix)
	  self.merge_files()
	  self.write_file(self.output_base_dir, self.output_file_prefix)


def main():
  merger = Merger('../data', 'data', '../output', 'output')
  merger.execute()

main()