# blackfiretap
TAP convertor for Blackfire.io reports

## How to use
Assuming you have the JSON output of Blackfire (generated with `--json`) in a file called `output.json` in your local folder:
```
docker run -it -v $(pwd):/data frvge/blackfiretap /data/output.json
```

You can also store it in a file:
```
docker run -it -v $(pwd):/data frvge/blackfiretap /data/output.json > my_tap_output.tap
```
