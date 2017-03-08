#!/bin/bash
DIR=$(dirname $0)
for f in ${DIR}/*; do rm -rf "$DIR/../game/$f"; done
