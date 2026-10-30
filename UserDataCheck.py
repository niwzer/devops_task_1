import re
import socket
input_file = open("users.txt")
result_file = open("result.txt", "w")
error_file = open("error.txt", "w")
next(input_file)

for line in input_file:
    userdata = line.strip().split(",")

    if len(userdata) < 3:
        error_file.write(f"Error: Incomplete user data in line: {line.strip()}\n")
        continue
    try:
        UserID = int(userdata[2])
    except ValueError:
        error_file.write(f"Invalid ID {line.strip()}\n")
        continue

    email = userdata[1]
    
    pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

    if not re.fullmatch(pattern, email):
        error_file.write(f"Invalid email format {email} FOR USER {userdata[0]}\n")
        continue
    domain = email.split('@')[1]

    try:
        ip_address = socket.gethostbyname(domain) 
    except socket.gaierror:
       error_file.write(f"Invalid domain {domain} FOR USER {userdata[0]}\n")
       continue

    if UserID % 2 == 0:
        result_file.write(f"The {UserID} of {email} is even number.\n")
    else:
        result_file.write(f"The {UserID} of {email} is odd number.\n")

input_file.close()
result_file.close()
error_file.close()