import socket
import datetime
import random
import logging

"""
Author:lia yosef
program name:2.6
Description:client and server communication  
date : 17/11/2023
"""
logging.basicConfig(filename="client.log", level="DEBUG")

QUEUE_LEN = 1
MAX_PACKET = 4


def time():
    """
    this function returns a string of the time with the help of datetime
    :return:the time now
    """
    return str(datetime.datetime.now())


def name():
    """
     this function returns the name of the server
    :return:a string parameter
    """
    shem = "server_hero"
    return shem


def rand_number():
    """
    this function returns a random number from 1 to 10 with the help od randint
    :return:an integer between 1-10
    """
    number = random.randint(1, 10)
    return number


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        my_socket.bind(('0.0.0.0', 1729))
        my_socket.listen(QUEUE_LEN)
        while True:
            client_socket, client_address = my_socket.accept()
            try:
                request = client_socket.recv(MAX_PACKET).decode()
                while request != "EXIT":
                    if request == "TIME":
                        logging.debug("server received time" + request)
                        date = time()
                        client_socket.send(date.encode())
                    elif request == "NAME":
                        logging.debug("server received name :" + request)
                        num = name()
                        client_socket.send(num.encode())
                    elif request == "RAND":
                        logging.debug("server received a random number" + request)
                        number = rand_number()
                        number = str(number)
                        client_socket.send(number.encode())
                    else:
                        s = "illegal request, try again"
                        client_socket.send(s.encode())
                    request = client_socket.recv(MAX_PACKET).decode()

            except socket.error as err:
                print('received socket error on client socket' + str(err))

            finally:
                msg = "EXIT"
                client_socket.send(msg.encode())
                client_socket.close()
    except socket.error as err:
        print('received socket error on server socket' + str(err))

    finally:
        my_socket.close()
        logging.log("client socket close")


if __name__ == "__main__":
    assert time() == str(datetime.datetime.now())
    assert name() == "server_hero"
    assert 0 <= rand_number() <= 10
    main()

