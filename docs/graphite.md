# Graphite Batch Upload

**Formatting Graphite Pickled Data**

Graphite's pickle endpoint can receive a list of tuples, formatted as follows:

~~~~~
[(<endpoint>, (<timestamp>, <count>)), ...]
~~~~~

... where the endpoint is a string, and each folder level in the UI is separated with dots, i.e. "stats.server3.bookstore_endpoint", etc.

... the timestamp is a UNIX integer timestamp,

.... and count is an int.