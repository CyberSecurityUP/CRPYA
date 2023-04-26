import base64
import re
import socket
import threading
import pyaes
from hashlib import sha256
from base64 import b64decode
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
from Crypto.Random import get_random_bytes
import time
import random
from scapy.all import *

def challenge_1():
    print("Challenge 1: Decode the following base64 string: YjRzMzY0X3MzY3IzdEZsNGc=")
    user_input = input("Type your Answer: ")
    encoded_string = "YjRzMzY0X3MzY3IzdEZsNGc="
    decoded_string = base64.b64decode(encoded_string).decode("utf-8")
    return user_input.strip() == decoded_string

def challenge_2():
    print("Challenge 2: Parse the 'qakbot.pcap' file and find the source IP address in the HTTP requests.")
    user_input = input("Enter the IP you found: ")

    pcap_file = "qakbot.pcap"
    packets = rdpcap(pcap_file)

    ip_found = False

    for packet in packets:
        if packet.haslayer('IP'):
            src_ip = packet['IP'].src
            if src_ip == "179.60.146.16":
                ip_found = True
                break

    if not ip_found:
        print("The source IP correct was not found.")
        return False

    return user_input.strip().lower() == "179.60.146.16"

def challenge_3():
    print("Challenge 3: Filter IP addresses using Regex in a file called 'sample_log.log'")
    user_input = input("Type your Answer: ")
    with open("sample_log.log", "r") as f:
        log_data = f.read()

    ip_pattern = r"172\.31\.44\.101"
    match = re.search(ip_pattern, log_data)

    if match is None:
        return False

    return user_input.strip() == match.group(0)

def scramble_text(text):
    text_list = list(text)
    random.shuffle(text_list)
    return ''.join(text_list)

def challenge_4():
    original_text = "H0k1ngisc0m1ng"
    scrambled_text = scramble_text(original_text)

    print(f"Challenge 4: The following text has been scrambled: {scrambled_text}. Discover the original text.")
    user_input = input("Type your Answer: ")

    return user_input.strip() == original_text

def challenge_5():
    print("Challenge 5: Decrypt the 'test.txt.hacked' file using the 'blackhatpythoncs' key and get the contents of the file.")
    user_input = input("Type your Answer: ")

    file_name = "test.txt.hacked"
    with open(file_name, "rb") as file:
        file_data = file.read()

    key = b"blackhatpythoncs"
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    new_file = "test.txt"
    with open(new_file, "wb") as f:
        f.write(decrypt_data)

    with open(new_file, "r") as f:
        decrypted_content = f.read()

    return user_input.strip() == decrypted_content.strip()

def main():
    challenges = [challenge_1, challenge_2, challenge_3, challenge_4, challenge_5]
    score = 0

    for challenge in challenges:
        if challenge():
            print("Right answer!")
            score += 10
        else:
            print("Incorrect answer!")

    print(f"Congratulations! Your final score is: {score}")

if __name__ == "__main__":
    main()
