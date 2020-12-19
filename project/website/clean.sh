#!/bin/bash

# File:        clean.sh
# Date:        Dec. 17. 2020
# Author:      Anthony Ngoma (an474), Tsetse Kludze(akk72)
# Quick way to close already used ports. 

kill -9 $(lsof -t -i:8000)
kill -9 $(lsof -t -i:5000)
