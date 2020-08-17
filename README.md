# procedure_log2tsv
datalad procedure to preprocess .log files for datalad-hirni 


For log2tsv.py to work, ```pandas``` and ```DataLad``` have to be installed.

The procedure is called by running ```datalad run-procedure log2tsv.py <SOUCE OF .LOG FILES> <LOCATION FOR .TSV FILES>``` in the root dataset.

TODO: find out, why code only runs correctly as procedure when called as ```mat2tsv.py```
