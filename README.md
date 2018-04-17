# pythonSimpleDataStreamer

This program streams a file over IP from server to standard input(stdin) of client. It can also be used to stream sound waves by piping stdin to speakers.

I wrote it as an intoduction to network programming. 

To pipe stdin to speakers run [python abapClient.py | aplay] on 'newer' linux systems.
On 'older' linux systems you might want to try [python abapClient.py > /dev/dsp] .
