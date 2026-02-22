import socket
from functions import is_int

# Define constants
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12346
ENCODER = "utf-8"

# Clients Name
client_name = input("Client Name: ")


# Create client socket and connect it
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

# recv successfull connection message and server name
print(client_socket.recv(1024).decode("utf-8"))
server_name = client_socket.recv(1024).decode("utf-8")

# Send client name to server
client_socket.send(client_name.encode("utf-8"))

# Show handshaked user's names
print("\n#########################################")
print(f"Server: {server_name}\nClient: You")
print("#########################################\n")


# Used to send from client to server messege
def client_send_number():
    # while loop used for error handling, if it happens it will be asked to rewrite messege
    while True:
        # For error handling
        try:
            # Messege we want to send
            messege = input("You: ")

            # check whether client wants to leave chat
            # .lower() used if client types Quit or smth like that
            # After confimation our client send confirmation letter and then leaves chat
            # If we enter this section break will stop this while loop so we will get our return result
            if messege.lower() == "quit":
                client_socket.sendall("End of conversation, client leaved chat!".lower().encode(ENCODER))
                client_socket.close()
                break

            # Check whether int is sended and does it keeps range correctly
            # If we enter this section break will stop this while loop so we will get our return result
            # So we filter sending function of client, so we dont need to worry about recieving part of server(we will se it later)
            elif is_int(messege) and 1 <= int(messege) <= 100:
                client_socket.sendall(messege.lower().encode(ENCODER))
                break

            # if user types other than number or quit it is not accepted so loop repeats,
            # letting us to rewrite messege and send correct one
            else:
                raise ValueError
        
        # Messege for user in order to know where is error
        except ValueError:
            print("Error: Invalid input, please type number!")


# this is clients get messege from server(number or quit messege)
def client_get_number():
    # Here we recieve our messege
    messege = client_socket.recv(1024).decode("utf-8")

    # We diplay or delivered messege to our terminal in order to read
    print(f"{server_name.capitalize()}: {messege}")

    # We check whether server wants to leave chat
    # After confirmation of quitting we leave chat and stop loop(it is crusial to stop loop also) 
    if messege.lower() == "quit":
        # Confirmation letter for us when server leaving chat
        print("End of conversation, Server leaved the chat!")

        # Here we close socket operation
        client_socket.close()

        # In order to stop main loop which operate the whole stuff
        return False


# Main loop which operate whole stuff
while True:
    # We run our functions 
    client_send_number()
    client_get_number()










