import datetime

#the following function takes a letter and returns a number for its position.

def alphabet_position(letter):
  alpha = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
  for ctr in range(len(alpha)):
    if alpha[ctr] == letter:
        return int(ctr/2)

#the following function rotates a letter according to a certain code.

def rotate_character(char, rot):
  lettersrot = ("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")  
  if char.isalpha():
      num1 = alphabet_position(char)
      num2 = num1 + rot
      if num2 > 25:
        num2 = num2 - 26
      if num2 < 0:
        num2 = num2 + 26
      for elem in lettersrot:
          if alphabet_position(elem) == (num2):
              for num3 in range(len(lettersrot)):
                  if char == lettersrot[num3]:
                      num4 = num3
              if num4%2==0:
                elem=elem.upper()
              else:
                elem=elem.lower()  
              return elem
  elif char.isnumeric():
      dig = int(char)
      dig2 = dig + 3
      if dig2 > 9:
          dig2 = dig2 - 9
      dig3 = str(dig2)
      return dig3
  else:
      return char

#this code uses the other functions to encrypt a message.

def encrypt(message, code):
    ctr = 0
    answ = ""
    for elem in message:
        if elem.isalpha() or elem.isnumeric():
            answ += rotate_character(elem, int(code[ctr]))
            ctr += 1
            if ctr == len(code):
                ctr = 0
        else:
            answ += elem
    return answ

#this code is used to decrypt a message. It essentially reverses the encrypt functions.

def decrypt(message, code):
    ctr = 0
    answ = ""
    for elem in message:
        if elem.isalpha():
            answ += rotate_character(elem,(-1* int(code[ctr])))
            ctr += 1
            if ctr == len(code):
                ctr = 0

        elif elem.isnumeric():
            diga = int(elem)
            digb = diga - 3
            if digb < 0:
              digb = digb + 9
            digc = str(digb)
            answ += digc
            ctr += 1
            if ctr == len(code):
                ctr = 0
        else:
            answ += elem
    return answ

#this function retrieves the date and time and returns it as a string.

def retrieve_time():
    right_now = datetime.datetime.now().isoformat()
    list = []

    for i in right_now:
        if i.isnumeric():
           list.append(i)

    tim = "".join(list)

    return tim

#this is the main function. It encrypts or decrypts based on user input.

def main():
    codin = retrieve_time()
    quer = input("Please enter 1 to encrypt or 2 to decrypt: ")
    if quer == "1":
        print("Encryption:")
        msgin = input("What message would you like to encrypt? ")
        codin = retrieve_time()
        encmsg = encrypt(msgin, codin)
        codtot = "12252001" + codin
        outfile = open("ShadowDataOut.txt", "w")
        outfile.write(encmsg + "\n")
        outfile.write(codtot + "\n")
        outfile.close()

    if quer == "2":
        print("Decryption:")
        infile = open("ShadowDataOut.txt", "r")
        aline = infile.readline()
        recmsg = aline[0:-1]
        aline = infile.readline()
        rectim = aline[8:-1]
        infile.close()
        dcpmsg = decrypt(recmsg, rectim)
        print("The translation is:", dcpmsg)

## THE GHOST OF THE SHADOW ##

if __name__ == "__main__":
    main()