#!/usr/bin/env python3

import json
import sys

try:
    data = json.load(open(sys.argv[1]))
    input = data["report"]["tests"]
except IndexError:
    print("Please specify a valid JSON file as first argument")
    sys.exit(1)

print("TAP version 13")
print("1..{}".format(len(input)))
for idx, test in enumerate(input):
    result = "ok" if test["state"] == "successful" else "not ok"
    description = test["name"]
    print("{} {} {}".format(result, idx + 1, description))
