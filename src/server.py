from app import app
from config import PORT
from controllers import root_controller

app.run("127.0.0.1", PORT, debug=True)
