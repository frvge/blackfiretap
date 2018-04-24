# blackfiretap
TAP convertor for Blackfire.io reports

## How to use
Assuming you have the JSON output of Blackfire (generated with `--json`) in a file called `output.json` in your local folder:
```
docker run --rm -it -v $(pwd):/data frvge/blackfiretap /data/output.json
```

You can also store it in a file:
```
docker run --rm -it -v $(pwd):/data frvge/blackfiretap /data/output.json > my_tap_output.tap
```

Example output:
```
TAP version 13
1..6
ok 1 Pages should be fast enough
ok 2 Pages should not have a high IO wait time
ok 3 Pages should not fetch lots of data over the network
ok 4 Pages should not consume too much memory
not ok 5 Pages should not do too many SQL queries
ok 6 Pages should be light
```
