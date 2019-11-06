from merger import Merger
from exception import MaxFileSizeReachedException
import click


@click.command()
@click.option('--read_base_dir', help='Base directory for input files', required=True)
@click.option('--read_prefix', help='Prefix for input files', required=True)
@click.option('--output_base_dir', help='Base directory for the output file', required=True)
@click.option('--output_prefix', help='Prefix for the output file')
@click.option('--max_file_size', default=1024, help='Max file size allowed in the merged JSON file')
def json_merger(read_base_dir, read_prefix, output_base_dir, output_prefix, max_file_size):
  merger = Merger(read_base_dir, read_prefix, output_base_dir, output_prefix, max_file_size)
  try:
  	merger.execute()
	except MaxFileSizeReachedException:
		print('Failed for the following reason:')
		print('Max file size reached. Please tune your max file size value.')

if __name__ == '__main__':
    main()