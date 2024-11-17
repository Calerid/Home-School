import os
from dotenv import load_dotenv
from school import start_school

load_dotenv()

school = start_school()

if __name__ == '__main__':
    school.run(host='127.0.0.1, port=5000, debug=True')
