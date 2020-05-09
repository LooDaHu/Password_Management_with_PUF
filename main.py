import sys, getopt
import hash_helper
import database_helper
import PUF_helper


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "ea")
    except getopt.GetoptError:
        print('Enrollment: main.py -e <username> <password>')
        print('Or')
        print('Authentication: main.py -a <username> <password>')
        sys.exit(2)
    username = args[0]
    password = args[1]
    instruction = opts[0][0]
    if instruction == '-e':
        enrollment(username, password)
    elif instruction == '-a':
        authentication(username, password)
    else:
        print("invalid input")


def enrollment(username: str, password: str):
    password_hash = hash_helper.get_password_hash(password)
    x_puf, y_puf = hash_helper.get_address_PUF(password_hash)
    challenge = PUF_helper.PUF_reader(x_puf, y_puf, type="challenge")
    username_hash = hash_helper.get_username_hash(username)
    x_database, y_database = hash_helper.get_address_database(username_hash, password_hash)
    database_helper.enrollment(x_col=x_database, y_row=y_database, challenge=challenge)
    print("Enrollment has done")


def authentication(username: str, password: str):
    password_hash = hash_helper.get_password_hash(password)
    x_puf, y_puf = hash_helper.get_address_PUF(password_hash)
    response = PUF_helper.PUF_reader(x_puf, y_puf, type="response")
    username_hash = hash_helper.get_username_hash(username)
    x, y = hash_helper.get_address_database(username_hash, password_hash)
    result = database_helper.authentication(x_col=x, y_row=y, response=response)
    if result:
        print("Success")
    else:
        print("Fail")


if __name__ == "__main__":
    main(sys.argv[1:])
