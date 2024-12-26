username = str(input())

password = str(input())

def is_valid(username, password):
    
    if username == "user" and password == "qweasd":
        return True
    elif username == "admin":
        return True
    else:
        return False

print(is_valid(username, password))