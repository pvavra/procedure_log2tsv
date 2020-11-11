# procedure_log2tsv
Addon for `datalad-hirni` for converting Siemens' physiological .log files into BIDS-format. 

There are two procedures, one for the `..PULS.log` files, and the second one for the `..RESP.log` files. 

Each procedure can be used in two modes:
In mode 1, the procedure simply writes out the resulting tsv-file into the specified directory. The filename will match the input's file, except for the file ending. This mode is intended for asserting that the content of the files is correct, when applying it for the first time in a new project (The file-format of the log-files was reverse engineered and is not relying on any "official" documents by Siemens, so it could be wrong. user beware..).
In mode 2, the procedure requires additional BIDS-information, like subject number, session, etc., to name and place the file according to BIDS-specs. This latter mode is best used directly via Hirni's `studyspec.json` file. 

The names of the procedures are `puls2tsv` and `resp2tsv`. 

To run in mode 1, call `datalad run-procedure puls2tsv input_file_PULS.log output_folder`.

To run in mode 2, specify the procedure in the studyspec.json file, and then call `datalad hirni_spec2bids path_to_studyspec.json`. 
