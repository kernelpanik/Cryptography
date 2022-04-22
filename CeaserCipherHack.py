vocabulary = "abcdefghijklmnopqrstuvwxyz"

enc_string = input("Enter string to decrypt: ")

x = 0
while x < 26:
    x = x + 1 
    stringtodecrypt=enc_string
    stringtodecrypt=stringtodecrypt.lower()
    nofshift=int(x)
    stringdecrypted=""
    for character in stringtodecrypt:
        position = vocabulary.find(character)
        tmpposition = position-nofshift
        if character in vocabulary:
            stringdecrypted = stringdecrypted + vocabulary[tmpposition]
        else:
            stringdecrypted = stringdecrypted + character
            
    nofshift=str(nofshift)
    print("Number of shift "+nofshift)
    print(f'Decrypted message: {stringdecrypted} \n')
