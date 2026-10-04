install:
	python3 -m pip install -r requirements.txt
train:
	python scripts/train.py
app:
	streamlit run app.py
test:
	pytest -q
