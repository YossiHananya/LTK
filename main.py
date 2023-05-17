import argparse
from api.api import app

def menu():
    parser=argparse.ArgumentParser()
    parser.add_argument("--port",type=int,default=5000,help='Port For API')
    args=parser.parse_args()
    return args

def main(port):
    app.run(host='localhost',port=port)


if __name__=="__main__":
    args = menu()
    main(port=args.port)
