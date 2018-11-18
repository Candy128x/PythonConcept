echo "pingpong"

#git add .
#git add -A
git add -f .

echo Write your commit:
read cmmt
echo You commit: $cmmt
git commit -m "$cmmt </> $(date +"%a, %Y-%m-%d, %H:%M:%S %Z %j")"

git pull origin home
git push origin home
#git push -f origin home


$SHELL