# Graphite Batch Upload

This project aims to be a simple adapter for batch uploads from data/log processing scripts into common graphing software.


Many stats database/visualization stacks, like statsd/Graphite, only accept statistics in realtime, making uploading historical statistical data somewhat more complicated. Graphite has a bulk upload feature that allows the user to bypass the statsd server, which simply requires setting up a socket and sending pickled data through it.

This project aims to be an abstraction of that process for Graphite, and facilitate batch upload of historical stats.

## How to Use

~~~~~
import ancientlogs

loader = ancientlogs.GraphiteUploader()
loader.send(data)
# data is a list of tuples, see docs for formatting
~~~~~


See docs for more details on correct format for data. I plan to add some helpful formatting utilities to aid this process.

The batch uploader is meant to abstract all of the processes of dealing with large batches of historical data, such as 

 - dealing with max size limits
 - setting up and tearing down sockets
 - conveniently naming sets of data with the same stat name.

