from quart import Quart
from threading import Thread

app = Quart('')

@app.route('/')
def home():
    return 'App is running!'

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
