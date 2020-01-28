#!/bin/bash
find docs/ -name '*.md' -print0 |   wc -w --files0-from=-
