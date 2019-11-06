import json
import glob
import os
import timeit


class Merger(object):
  def __init__(self):
    self.data = []
    self.merged_data = {}

  def read_files(self, base_dir, prefix):
    filenames = glob.glob(os.path.join(base_dir, prefix + '*.json'))
    for filename in filenames:
      with open(filename, 'r') as json_file:
        json_file_data = json.load(json_file)
      self.data.append(json_file_data)

  def write_file(self, output_dir, prefix):
    pass

  def merge_files(self):
    for value in self.data:
      if self.merged_data:
        for key, single_data in value.items():
          self.merged_data[key].extend(single_data)
      else:
        self.merged_data.update(value)


def main():
  merger = Merger()
  merger.read_files('../data', 'data')
  merger.merge_files()
  print(merger.merged_data)

main()