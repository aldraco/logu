# Logu: easy batch upload for logs

This project aims to be a simple adapter for batch uploads from data/log processing scripts into common graphing software.

## Installation

~~~~~
pip install logu
~~~~~


Many stats database/visualization stacks, like statsd/Graphite, only accept statistics in realtime, making uploading historical statistical data somewhat more complicated. Graphite has a bulk upload feature that allows the user to bypass the statsd server, which simply requires setting up a socket and sending pickled data through it.

This project aims to be an abstraction of that process for Graphite, and facilitate batch upload of historical stats.

## How to Use

~~~~~
from logu import GraphiteUploader

with GraphiteUploader(host="graphite.yourhost.com") as gu:
    gu.send(data)

# data is a list of tuples, see docs for formatting

# to change the port number:
with GraphiteUploader(host="graphite.yourhost.com") as gu:
    gu.use_port(2004)
    gu.send(data)

~~~~~

The uploader will verify your data for you, clean up sockets when done (if used as a context manager), and help you organize your logs.


