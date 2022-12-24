import secrets, re
sk = str(secrets.token_urlsafe())
print(f"secret key is: {sk}")

with open("secret.txt", "w") as f:
    f.write(sk)
    print("secret key written to secret.txt")

with open("allowed_hosts.txt","a") as fa: 
    with open("allowed_hosts.txt","r") as fr:
        if "localhost" not in fr.read():
            fa.write("localhost\n")
            print("wrote 'localhost' to allowed_hosts.txt")

with open("allowed_hosts.txt","a") as fa: 
    with open("allowed_hosts.txt","r") as fr:
        if "127.0.0.1" not in fr.read():
            fa.write("127.0.0.1\n")
            print("wrote '127.0.0.1' to allowed_hosts.txt")
