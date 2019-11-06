# JSON Merger


## Installation
JSON Merger requires python3.

This install all the necessary dependancies:
```
$ pip install -r requirements.txt
```

This install the json_merger as python packages:
```
$ python setup.py develop
```


## Get Started
The main class is logic which is located in the `JSON_Merger/logic/__init__.py`
The cli commands were referred from click `https://click.palletsprojects.com/en/7.x/`


#### To do json_merger

```
$ json_merger --read-base-dir='data' --read-file-prefix='data' --output-base-dir='output' --output-file-prefix='output' --max-file-size=500D 
```
returns "Written successfully to /home/vigneshwar/Documents/probable-octo-succotash1/probable-octo-succotash/output/output4.json" for the above case.



```
$ json_merger --read-base-dir='data' --read-file-prefix='data' --output-base-dir='output' --output-file-prefix='output' --max-file-size=300
```
returns "Failed for the following reason:
Max file size reached. Please tune your max file size value." for the above case.



## Testing
The test file is located in the `JSON_Merger/tests/test_merger.py`
The testing were referred from pytest `https://docs.pytest.org/en/latest/getting-started.html`

The command to do test:
``
pytest
``

The function to tests for english alphabetic data
```
test_with_clean_data(clean_data, clean_merged_data)
````

The function to tests for english and hindi alphabetic data
```
test_with_hindi_data(data_with_hindi, merged_data_with_hindi)
```