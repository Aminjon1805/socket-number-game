import socket
from functions import is_int

# Define the constants
HOST_IP = socket.gethostbyname(socket.gethostname())
PORT = 12346
ENCODER = "utf-8"
BYTESIZE = 1024

# Server name
server_name = input("Server Name: ")

# Create server socket and bind it + listen !!!
server_socker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socker.bind((HOST_IP, PORT))
server_socker.listen()

# Accept any incoming connections and response that they sre connected
print("Server is running...\n")
client_server , client_addr = server_socker.accept()
client_server.send("You are successfully connected!".encode(ENCODER))
client_server.send(server_name.encode("utf-8"))


# Get client name
client_name = client_server.recv(1024).decode("utf-8")

# Show handshaked user's names
print("\n#########################################")
print(f"Server: You\nClient: {client_name}")
print("#########################################\n")

# To store sended value by client
holder = 0

# This function help us to get the messege from client, we dont need to verify it is string,
# bcz we client will validate and hold error and then sends clear number or quit messege,
# so we only need to look at quit
def server_get_number():
    # We make holder access to this function
    global holder

    # We take client's messege
    msg = client_server.recv(1024).decode("utf-8")

    # We check whether it is quit or integer

    # If it is int we display it in terminal for ability to know what client sends
    if is_int(msg):
        # If it is int we display it in terminal for ability to know what client sends
        print(f"{client_name.capitalize()}: {msg}")

        # We save it in holder for future usage
        holder += int(msg)

    # We check if our client wants to leave
    elif msg.lower() == "quit":
        # We are displaying for us confirmation that client is leaving
        print("End of conversation, client leaved chat!!!".lower())

        # We close our server and stop connection
        client_server.shutdown(socket.SHUT_RDWR)
        client_server.close()

        # Used to break the main loop which perform whole stuff
        return False

def server_send_number():
    # We are getting access to holder 
    global holder

    # Making loop to constrol error and validation, once everything is clear and correct we stop this loop
    while True:
        # Used to handle error that may occure, especially when server sending incorrect messege
        try:
            messege = input("You: ")

            # we check whether serve wants to leave chat
            if messege.lower() == "quit":
                client_server.send(messege.lower().encode(ENCODER))
                client_server.close()
                break

            # We check whether server sending a number(if not the loop repeats
            #  without sending messege till server will not write correct version)
            # Also here we check for range(if not in range loop repeats and server must write correct messege)
            elif is_int(messege) and 1 <= int(messege) <= 100:
                
                # We add up our client's and server's numbers
                result = holder + int(messege)

                # We display it for server to see result
                print(f"Result => {messege} + {holder.__str__()} = {result.__str__()}")

                # We send result to client also
                client_server.send(f"Result => {messege} + {holder.__str__()} = {result.__str__()}".encode("utf-8"))

                # if everything goes correctly this loop will stop and we will preform our operation
                break

            # If everything gone wrong, we repeate our journey going directly to except by raising error
            else:
                raise ValueError
        
        except ValueError:
            print("Error: Invalid input, please type number!")


# Main loop which perform whole stuf, keeping chat alive till smb will leave chat
while True:
    server_get_number()
    server_send_number()

    # restart value of holder
    holder = 0



