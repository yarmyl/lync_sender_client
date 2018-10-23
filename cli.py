#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mess', nargs='?') # сообщение
    parser.add_argument('--to', nargs='?') # адресат
    parser.add_argument('--srv', nargs='?') # сервер
    parser.add_argument('--users', action='store_true') # список пользователей
    parser.add_argument('--sip', nargs='?') # по sip
    parser.add_argument('--port', nargs='?') # port сервера
    return parser

def send_mess(srv, port, mess):
    sock = socket.socket()
    sock.connect((srv, port))
    sock.send(bytes(mess, "utf8"))
    data = sock.recv(2048)
    sock.close()
    return data.decode()


def main():
    parser = createParser()
    namespace = parser.parse_args()
    if namespace.srv:
        srv = namespace.srv
    else:
        srv = '127.0.0.1'
    if namespace.port:
        port = int(namespace.port)
    else:
        port = 1112
    if namespace.users:
        print(send_mess(srv, port, "print users"))
    elif namespace.mess:
        if namespace.to:
            print(send_mess(srv, port, namespace.mess + '--->' + namespace.to))
        elif namespace.sip:
            print(send_mess(srv, port, namespace.mess + '+++>' + namespace.sip))
        else:
            print("Bad type!")
    else:
        print("Bad type!")

if __name__ == "__main__":
    main()