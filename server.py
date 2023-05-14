import socket
import logging


MyDictionary = {
    "stereotype":"stéréotype",
    "rabbit":"lapin",
    "cotton":"coton",
    "book":"book",
    "dog":"chien",
    "chair":"une chaise",
    "eat":"manger",
    "drink":"boire",
    "frog":"grenouille",
    "programming":"la programmation"
}
#this func returns <STRING> object if there is no matching name in dictionary, it returns exception


def findWordInDict(userRequest):
    for item in MyDictionary.keys():
        if item.lower() == userRequest.lower():
            return MyDictionary[item]
    #if no request in dictionary
    return "NO MATCHING NAMES IN DICTIONARY"


def main():
    logging.basicConfig(level=logging.INFO,filename = "server.log", filemode="w", format="%(asctime)s - %(message)s")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.info("Server started")
    #host and port. host empty, so any interface could be connected,port -  1025 + 8
    server.bind(('', 1035))
    server.listen(1)
    #accept returns two elements - new socet and client adress
    client, addr = server.accept()
    client.send(("Welcome to English-Français translator.").encode())
    logging.info(f"connected from ADDRESS : {addr}")
    while True:
        client.send(("Enter word in english, or 'quit', to close connection: ").encode())
        userRequest = client.recv(1024).decode()
        if not userRequest :
            logging.info("Server received wrong input")
            client.send(("Wrong input").encode())
            break

        elif userRequest.lower() == "quit":
            logging.info(f"Server received : {userRequest}")
            logging.info("Client disconnected")
            client.send(("close").encode())
            break

        elif userRequest.lower() == "who":
            logging.info(f"Server received : {userRequest}")
            client.send(("Maksym Lukovskiy, K16, variant: Dictionary").encode())

        else:
            # invoking findWordInDict that returns <STRING>then sents to client
            logging.info(f"Server received : {userRequest}")
            client.send(("Defenition: "+findWordInDict(userRequest)).encode())
            logging.info(f"Server sent : '{findWordInDict(userRequest)}'")

    client.close()
    logging.info(f"Server closed")

if __name__ == "__main__":
    main()
