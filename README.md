# jsonToCsv or csvToJson
Convert paths in JSON to CSV or converted CSV to JSON

> csvToJson
```
1. enter the CSV filename and file path that will be entered in the 'csv_file_path' variable.
2. In the 'json_output_path' variable, enter the name and path to the JSON file that will be output.
3. python3 csvToJson.py
```

> jsonToCsv
```
1. enter the CSV filename and file path that will be entered in the 'large_json_file_path' variable.
2. In the 'csv_output_path' variable, enter the name and path to the JSON file that will be output.
3. python3 jsonToCsv.py
```

> Usage examples

1. json
```
"common": {
  "submit": "Enter",
  "apply": "Apply",
  "save": "Save",
  "snackbar": {
    "message": "Snackbar message"
  },
  "attach": "Attach",
  "close": "Close",
  ...
}
```

2. csv
   
|Key|Value|
|------|---|
|common.submit|Enter|
|common.apply|Apply|
|common.save|Save|
|common.snackbar.message|Snackbar message|
|...|

> Why made it

One very large json data is often modified or new keys are added, so it becomes difficult to manage, so we created it to convert it to csv, collaborate on it, and convert it back to json to store it.
