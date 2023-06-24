import argparse
from soccer_application import create_app

def menu():
    parser=argparse.ArgumentParser()
    parser.add_argument(
        "--port",
        type=int,
        default=5000,
        help='Port For API'
    )
    args = parser.parse_args()
    
    return args

def main(port):
    app=create_app('dev')
    app.run(host='localhost',port=port)


if __name__=="__main__":
    args = vars(menu())
    main(**args)
