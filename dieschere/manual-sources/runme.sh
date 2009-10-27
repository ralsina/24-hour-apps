#!/bin/sh
rst2qhc handbook.txt howto.txt -o . --namespace dieschere --filterattributes dieschere --rst2htmlopts="--stylesheet=style.css --link-stylesheet" --manifest MANIFEST --create-qhcp
qcollectiongenerator project.qhcp -o collection.qhc
