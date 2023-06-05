import argparse
from api.api import app

def menu():
    parser=argparse.ArgumentParser()
    parser.add_argument(
        "--port",
        type=int,
        default=5000,
        help='Port For API'
    )
    
    parser.add_argument(
        "-d",
        "--debug", 
        action="store_true",
        help='Activate debug mode, code changes will automatically updated in the browser'
    )
    args = parser.parse_args()
    
    return args

def main(port, debug):
    app.run(host='localhost',port=port, debug=debug)


if __name__=="__main__":
    args = vars(menu())
    main(**args)
