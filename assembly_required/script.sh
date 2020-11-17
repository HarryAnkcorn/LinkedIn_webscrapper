#! /user/bin/bash

# mkdir test

cd /c/Users/Harry/Desktop/My_Generation/webpage/HarryAnkcorn.github.io

aws s3 ls s3://linkedinwebscrap

aws s3 cp s3://linkedinwebscrap/plot.png plot.png

git commit -am "graph update"

git push

echo  fin

exec $SHELL
