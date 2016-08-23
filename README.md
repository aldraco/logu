# Graphite Batch Upload

This project aims to be a simple adapter for batch uploads from data/log processing scripts into common graphing software.


Many stats database/visualization stacks, like statsd/Graphite, only accept statistics in realtime, making uploading historical statistical data somewhat more complicated. Graphite has a bulk upload feature that allows the user to bypass the statsd server, which simply requires setting up a socket and sending pickled data through it.

This project aims to be an abstraction of that process, and facilitate batch upload of stats for many services.
