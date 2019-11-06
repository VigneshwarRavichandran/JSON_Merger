from merger.json_merger import JSONMerger

def test_with_clean_data(clean_data, clean_merged_data):
	"""
	Initialising the JSONMerger with dummy dir data and loading the data with preloaded fixture and 
	testing the merge_files() function to work properly
	"""
	merger = JSONMerger('dummy_dir', 'dummy_prefix', 'dummy_dir', 'dummy_prefix')
	merger.data = clean_data
	merger.merge_files()
	assert merger.merged_data == clean_merged_data


def test_with_hindi_data(data_with_hindi, merged_data_with_hindi):
	"""
	Initialising the JSONMerger with dummy dir data and loading the data with preloaded fixture and 
	testing the merge_files() function to work properly
	"""
	merger = JSONMerger('dummy_dir', 'dummy_prefix', 'dummy_dir', 'dummy_prefix')
	merger.data = data_with_hindi
	merger.merge_files()
	assert merger.merged_data == merged_data_with_hindi