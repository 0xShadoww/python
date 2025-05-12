SecretNUM = 69;
guess = int(input('Guess a Number: '));
if SecretNUM == guess:
    print("guess is equal to Secret");
elif SecretNUM > guess:
    print("guess is lower than secret");
else:
    print("guess is higher than secret");