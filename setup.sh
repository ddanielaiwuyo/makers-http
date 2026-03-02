#!/usr/bin/env zsh
set -e

target_dir="$HOME/makers_http"

if python3 --version | grep -q "3.13"; then
else
	echo "python version 3.13 not found, please install or continue the manual setup"
fi

new_dir=$1
if [ -d  "$target_dir" ]; then
	read new_dir\?"$target_dir already exists, enter name of folder to clone: "
fi

target_dir="$HOME/$new_dir"

git clone https://github.com/ddanielaiwuyo/makers-http.git "$target_dir" 

cd $target_dir
export PYTHONPATH=$(pwd)

python3 -m venv env && source ./env/bin/activate

echo "installing dependencies from:"
cat -n requirements.txt
pip install -r requirements.txt

echo "Done with the installation"
echo "Please make sure you have psql installed and running!"
echo "Run the following after you've confiured psql, preferrably version 15"
echo "1. cd $target_dir"
echo "2. flask --app main run"
