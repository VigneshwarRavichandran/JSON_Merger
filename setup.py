from setuptools import setup

setup(
	name='JSONMerger',
  version='1.0.0',
  description='Merge many JSON files to a single file.',
  authors_email=['vigneshwarravichandran@gmail.com'],
  entry_points={
    'console_scripts': [
      'json_merger = merger.cli:json_merger'
    ],
  })