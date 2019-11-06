import json
import glob
import os

from .exception import MaxFileSizeReachedException


class JSONMerger(object):
  def __init__(self, read_base_dir, read_file_prefix, output_base_dir, output_file_prefix, max_file_size=1024):
    self.data = []
    self.merged_data = {}
    self.read_base_dir = read_base_dir
    self.read_file_prefix = read_file_prefix
    self.output_base_dir = output_base_dir
    self.output_file_prefix = output_file_prefix
    self.max_file_size = max_file_size

  """
  The function validate_max_size is used validate the size of the output file before insertion.
  JSON object is obtained as string using json.dumps and string len gives the byte size of the file.
  """
  def validate_max_size(self):
  	if len(json.dumps(self.merged_data)) > self.max_file_size:
  		raise MaxFileSizeReachedException 

  """
  The function read_files appends the JSON data in self.data
  glob.glob(os.path.join(base_dir, prefix + '*.json')) obtains all the file starts with the prefix value and 
  ends with .json
  """
  def read_files(self, base_dir, prefix):
    filenames = glob.glob(os.path.join(base_dir, prefix + '*.json'))
    for filename in filenames:
      with open(filename, 'r') as json_file:
        json_file_data = json.load(json_file)
      self.data.append(json_file_data)

  """
  The function merge_files stores the merged data in self.merged_data
  The isinstance checks whether the single_data obtained is a list or not.
  If the key already exsists in the self.merged_data then its extends or else new key is created and value is simply assigned
  """
  def merge_files(self):
    for value in self.data:
      if self.merged_data:
        for key, single_data in value.items():
          if isinstance(single_data, list):
            if key in self.merged_data.keys():
              self.merged_data[key].extend(single_data)
            else:
              self.merged_data[key] = single_data
            self.validate_max_size()
      else:
        self.merged_data.update(value)

  """
  The function write_file writes self.merged_data into the output file.
  """
  def write_file(self, output_dir, prefix):
    if not (os.path.isdir(output_dir)):
    	# Using mkdir creates directory recursively
    	os.makedirs(output_dir)
    output_file_name = os.path.join(output_dir, '{0}{1}.json'.format(prefix, len(self.data) + 1))
    with open(output_file_name, 'w') as output_file:
      json.dump(self.merged_data, output_file, ensure_ascii=False)
    print('Written successfully to {0}'.format(os.path.abspath(output_file_name)))

  def execute(self):
	  self.read_files(self.read_base_dir, self.read_file_prefix)
	  self.merge_files()
	  self.write_file(self.output_base_dir, self.output_file_prefix)