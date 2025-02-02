from flask import Flask

app = Flask(__name__)

# Import configuration
from search import config

# Apply configuration
app.config.from_object(config)

# Import views and models
from search.views import main
from search import model

# Load data into memory
model.load_data()