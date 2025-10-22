#PS 1st Encoder and Decode

#list for characters in the alphabet

#function for encrypting
def Encrypt(Message, Cipher_Number):
    Message = Message.lower()
    Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    new_message = ""
    for x in Message:
        Position = Letters.index(x)
        Position += Cipher_Number
        new_message = new_message + Letters(Position)
        new_message = new_message.capitalize()
    return new_message



#function for Decrypting
def Decrypt(Message, Ciper_Number):
    Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    Message = Message.lower()


#asks user if they want to decrypt or encrypt
Mode = int(input("Welcome to the Casaer ciper Encoder and Decoder \n Press 1 for Encrypter \n Press 2 for Decrypter \n ").strip())

#Asks user for their message
Message = input("Write a message to be encrypted or decrypted \n Rules \n No Numbers \n No special Characters \n Write your message here: ").strip()
#conditional for decode encode and invalid input
Cipher = int(input("What is the ciper number you would like to use? \n Put an integer here: ").strip())
if Mode == 1:
    print("Encrypter chosen")
    Encrypt(Message, Cipher)
elif Mode == 2:
    print("Decrypter chosen ")
    Decrypt(Message, Cipher)
else:
    print("Invalid Input")