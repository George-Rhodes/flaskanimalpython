sudo apt update
sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venf 
. ./venf/bin/activate
pip3 install -r requirements.txt
cd application1
pytest --cov ./application 
cd ..
cd application2
pytest --cov ./application 

deactivate

rm -rf venf