alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(message, shift_number):
    encoded_mess = ""
    for letter in message():
        if letter not in alphabets:
            encoded_mess += letter
            continue
        mess_index = alphabets.index(letter)
        mess_index += shift_number
        encoded_mess += alphabets[mess_index]
        
    print(f"The encoded text is: {encoded_mess}")   
    
def decrypt(message, shift_number):
    decoded_mess = ""
    for letter in message():
        if letter not in alphabets:
            decoded_mess += letter
            continue
        mess_index = alphabets.index(letter)
        mess_index -= shift_number
        decoded_mess += alphabets[mess_index]
        
    print(f"The decoded text is: {decoded_mess}")    
    
ans = "yes"

while ans == "yes":
    option = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if option == "encode":
        text = input("Type your message: ").lower
        shift = int(input("Type the shift number: "))
        if shift > 26:
            shift %= 26
        encrypt(message = text, shift_number = shift)
        
    elif option == "decode":
        text = input("Type your message: ").lower
        shift = int(input("Type the shift number: "))
        decrypt(message = text, shift_number = shift)
    
    else:
        print("Type correctly!!!")
    
    ans = input("Type 'yes' if you want to go again, otherwise 'no'. \n").lower()


