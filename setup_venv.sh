
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source scripts/activate_venv.sh
pip install -r requirements.txt
