#!/bin/sh

docker build -f Dockerfile -t dibz_takehome .

docker run -v /vivianetrindade/Projects/dibz_backend_takehome-main -it -p 5001:5001 dibz_takehome
