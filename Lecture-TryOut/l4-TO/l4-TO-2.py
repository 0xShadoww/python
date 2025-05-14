letters =  "aqzxswcdevfrbgtnhymjukilop";
Word = input("What word in mind: ");

seen = ""
for W in Word:
    if W in letters and W not in seen:
        seen = seen + W

print("Unique letters:", len(seen))
