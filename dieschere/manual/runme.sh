#!/bin/sh
mkdir out 2>/dev/null
rst2qhc handbook.txt howto.txt -o out --namespace dieschere --filterattributes dieschere --rst2htmlopts="--stylesheet=style.css --link-stylesheet" --manifest MANIFEST --create-qhcp
cd out
qcollectiongenerator project.qhcp -o collection.qhc
assistant -collectionFile collection.qhc -register doc.qhc 
assistant -collectionFile collection.qhc&
cd ..
