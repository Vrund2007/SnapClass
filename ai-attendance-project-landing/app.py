import os
from flask import Flask, render_template

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)

STREAMLIT_APP_URL = os.environ.get("STREAMLIT_APP_URL", "http://localhost:8501")

@app.route('/')
def home():
    return render_template('index.html', streamlit_url=STREAMLIT_APP_URL)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
