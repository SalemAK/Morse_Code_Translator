from morse_code import morse_latters


on = True
while on:
    Decode_or_Encode = input("\nDo you want to Encode Or Decode Morse Code?(Enter off to close)  ").lower()

    if Decode_or_Encode == "encode":
        letter = input("Please Enter your letter to Translate to Morse Code: ")
        for n in letter:
            if n in morse_latters.keys():
                print(morse_latters[n], end=" ")

    if Decode_or_Encode =="decode":
        decode_symbol = ["-", "."]
        code = input("Please Enter your letter to Translate to Morse Code: ").split()
        if code in decode_symbol:
            for i in code:
                key = [key for key, val in morse_latters.items() if val == i]
                print(key[0].capitalize(), end="")
        else:
            pass

    if Decode_or_Encode == "off".lower():
        on = False
