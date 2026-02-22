# Socket Number Game (TCP Client/Server)

This project is a simple TCP socket client-server "number game" written in Python.

The client and server connect, exchange names (handshake), and then exchange numbers between 1 and 100. The server calculates the sum and sends the result back to the client.

---

## Files

- server_num_game.py — TCP server program  
- client_num_game.py — TCP client program  
- functions.py — helper function is_int() for input validation  

---

## Requirements

- Python 3.x

---

## How It Works

### Handshake

- Server starts and asks for Server Name  
- Client starts and asks for Client Name  
- Server sends connection confirmation and server name  
- Client sends client name  
- Both sides display connected users  

---

### Game Loop

- Client enters a number (1–100)  
- Server receives the client number  
- Server enters its own number (1–100)  
- Server calculates the sum  
- Server sends result to client  
- Client displays the result  

If either side types quit, the connection closes.

---

### Result Format

```
Result => <server_number> + <client_number> = <sum>
```

Example:

```
Result => 40 + 25 = 65
```

---

## Run Instructions

### 1) Start the server (Terminal 1)

```bash
python server_num_game.py
```

Write server name when asked.

### Server Screenshot

![Server Screenshot](screenshots/server_running.png)

---

### 2) Start the client (Terminal 2)

```bash
python client_num_game.py
```

Write client name when asked.

### Client Screenshot

![Client Screenshot](screenshots/client_running.png)

---

### 3) Both Server and Client interface

![Server Client Interface](screenshots/server_client_chat_interface.png)

---

### 4) Example chat output

![Chat Example](screenshots/example.png)

---

## Input Rules

- Only integers from 1 to 100 are allowed  
- Invalid input shows error message  
- Typing quit closes the connection  

---

## Author

Aminjon Asoev  
GitHub: Aminjon1805