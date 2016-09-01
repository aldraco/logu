# Graphite Batch Upload

**Formatting Graphite Pickled Data**

Graphite's pickle endpoint can receive a list of tuples, formatted as follows:

~~~~~
[(<endpoint>, (<timestamp>, <count>)), ...]
~~~~~

... where the endpoint is a string, and each folder level is separated with dots, i.e. "api.prod.user_info", 

the timestamp is a UNIX integer timestamp, 

and count is an int.