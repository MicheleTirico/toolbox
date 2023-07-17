#!/bin/bash
git add .
git commit -m "update package"
git push
pip install git+https://github.com/MicheleTirico/toolbox
