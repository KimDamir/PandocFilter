#!/usr/bin/env python
from panflute import *
import re, sys
headers = set()


def filter(elem, doc):
    if type(elem) == Header:
        header = stringify(elem)
        if header in headers:
            sys.stderr.write("Error this heading repeats!" + header)
        else: headers.add(header)

    if type(elem) == Str and elem.text == "BOLD":
        return Strong(Str(elem.text))

    if type(elem) == Header and elem.level < 4:
        return elem.walk(upper)

def upper(elem, doc):
    if type(elem) == Str:
        return Str(elem.text.upper)


if __name__ == "__main__":
    run_filter(filter)
