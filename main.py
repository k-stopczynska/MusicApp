import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')

def main():
    print("Hello world")
    print(API_KEY)


if __name__ == "__main__":
    main()