#! /bin/zsh

git fetch
git pull origin main
git add .
git commit -am "$*  $(date)"
git push origin main
