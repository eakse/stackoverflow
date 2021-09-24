#!/bin/bash

git add *
git commit -m "Commit done from: $(hostname)
$(date '+%d/%m/%Y %H:%M:%S')"
git push