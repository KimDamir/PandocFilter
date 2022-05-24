from panflute import *
import re, sys
headers = set


def filter(elem, doc):
    if type(elem) == Header:
        for elem in headers:
            sys.stderr.write("Error this heading repeats!" + elem.text)

        headers.add(elem)

    if elem.text == "BOLD":
        elem.text = Strong(elem.text)

    if type(elem) == Header and elem.level <= 3:
        elem.text = elem.text.upper()
        return elem

    def main(doc=None):
        return run_filter(caps, doc=doc)


if __name__ == "__main__":
    main()
