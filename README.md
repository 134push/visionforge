# how to access the git 

# remove old git 
Remove-Item -Recurse -Force .git

# initialize git
git init
git add .
git commit -m "Initial commit"

# connect to remote git 
git remote add origin https://github.com/134push/visionforge.git

# branch main
git branch -M main

git push -u origin main --force