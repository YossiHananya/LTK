import argparse
from soccer_application import create_app


if __name__=="__main__":
    app=create_app('dev')
    app.run(host='localhost',port=app.config.get('PORT'))
