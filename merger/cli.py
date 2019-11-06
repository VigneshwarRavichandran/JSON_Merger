from merger.json_merger import JSONMerger
from merger.exception import MaxFileSizeReachedException
import click


@click.command()
@click.option('--read-base-dir', help='Base directory for input files', required=True)
@click.option('--read-file-prefix', help='Prefix for input files', required=True)
@click.option('--output-base-dir', help='Base directory for the output file', required=True)
@click.option('--output-file-prefix', help='Prefix for the output file')
@click.option('--max-file-size', default=1024, help='Max file size allowed in the merged JSON file')
def json_merger(read_base_dir, read_file_prefix, output_base_dir, output_file_prefix, max_file_size):
	merger = JSONMerger(read_base_dir, read_file_prefix, output_base_dir, output_file_prefix, max_file_size)
	try:
		merger.execute()
	except MaxFileSizeReachedException:
		print('Failed for the following reason:')
		print('Max file size reached. Please tune your max file size value.')

if __name__ == '__main__':
	json_merger()