#### Steps to use <br />
Assuming git, ruby are installed and configured correctly.<br />
Build from source:<br />
``` 
   git clone https://github.com/a2un/crawlpy.git
   cd crawlpy
   python __init__.py
```

In the repl shell that appears type "stop" to leave or supply three arguments as below:
```
    > https://about.gitlab.com 10 1      #<url> <interval(in seconds)> <totaltime(in minutes)> to run the probe
```