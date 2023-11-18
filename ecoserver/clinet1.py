import socket


MAX_PACKET = 1024
IP = "127.0.0.1"
PORT = 1729


def isvalid(msg):
    """
    this function gets a message and returns true if its TIME/RAND/NAME/EXIT and false if it's not
    :param msg:a string that contains a message
    :return:a bool value
    """
    return msg == "TIME" or msg == "NAME" or msg == "RAND" or msg == "EXIT"


def cheaking(msg, my_socket):
    """
    this function checks if isvalid function return true it sends the message to the server and if isvalid function
    returns false it's printing a message
    :param msg:a sting which contains the message which we want to send to the server
    :param my_socket:contains my socket which I use to transform messages from the client to my server
    :return:the answer from the server or ''
    """
    if isvalid(msg):
        my_socket.send(msg.encode())
        return my_socket.recv(MAX_PACKET).decode()
    else:
        print("illegal request , try again")
        return ''


def main():
    my_socket = socket.socket()
    try:
        my_socket.connect((IP, PORT))
        msg = input("pls enter a message: ")
        response = cheaking(msg, my_socket)
        while response != "EXIT":
            print("server responded with: " + response)
            msg = input("pls enter a message: ")
            response = cheaking(msg, my_socket)
    except socket.error as error:
        print("socket error:" + str(error))

    finally:
        my_socket.close()


if __name__ == "__main__":
    assert isvalid('TIME')
    assert isvalid('RAND')
    assert isvalid('NAME')
    assert not isvalid('haha')
    main()
