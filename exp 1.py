def encryption(plaintText,n):
    res=""
    for ch in plaintText:
        if ch.isupper():
            res+=chr(((ord(ch)+n-65)%26)+65)
        elif ch.islower():
            res+=chr(((ord(ch)+n-97)%26)+97)
        else:
            res+=ch
    print("Chipher text: ",res,'\n')
        
text=input("\nEnter Plaintext: ")
n=int(input("Enter shift: "))
encryption(text,n)