import random
thing=input("Thing :")
verb=input("Verb :")
fp1=input("Famous Personality :")
fp2=input("Famous Personality :")
adj=input("Adjective :")

red = "\033[91m"
reset = "\033[0m"
sentence = [ 
    f"I kept my {red}{thing}{reset} inside the fridge before I went to {red}{verb}{reset}\nBut {red}{fp1}{reset} stole it and sold it to {red}{fp2}{reset} . Now i am chasing {red}{fp2}{reset}. It is {red}{adj}{reset}! ",
    f"I asked {red}{fp1}{reset} to look after my {red}{thing}{reset} while I went to {red}{verb}{reset}. \nBut {red}{fp1}{reset} gave it to {red}{fp2}{reset}, who claimed it was a {red}{adj}{reset} gift!",
    f"{red}{fp2}{reset} borrowed my {red}{thing}{reset} to impress {red}{fp1}{reset}. \nUnfortunately, it broke while they were trying to {red}{verb}{reset}. What a {red}{adj}{reset} situation!",
    f"I found {red}{fp1}{reset} in my kitchen trying to {red}{verb}{reset} with my {red}{thing}{reset}. \nWhen I asked why, they gave me a {red}{adj}{reset} excuse!",
    f"{red}{fp1}{reset} invited me to a party, but {red}{fp2}{reset} arrived carrying my {red}{thing}{reset}. \nApparently, they had a {red}{adj}{reset} plan to {red}{verb}{reset} all night!",
    f"I challenged {red}{fp2}{reset} to {red}{verb}{reset} faster than me. The winner would get \nmy {red}{thing}{reset}. Unfortunately, {red}{fp1}{reset} joined the competition and made it {red}{adj}{reset}!",
    f"My {red}{thing}{reset} went missing during a family dinner. I questioned everyone until {red}{fp1}{reset} \nconfessed that {red}{fp2}{reset} had taken it for a {red}{adj}{reset} reason!",
    f"{red}{fp1}{reset} accidentally dropped my {red}{thing}{reset} while trying to {red}{verb}{reset} \nin front of {red}{fp2}{reset}. Nobody expected such a {red}{adj}{reset} performance!",
    f"I hired {red}{fp2}{reset} to help me {red}{verb}{reset}, but they spent the entire day playing with \nmy {red}{thing}{reset}. {red}{fp1}{reset} said it was the most {red}{adj}{reset} decision ever!",
    f"{red}{fp1}{reset} found my {red}{thing}{reset} outside a restaurant and decided to sell it \nto {red}{fp2}{reset}. Now both of them are arguing about who gets to {red}{verb}{reset} with it. What a {red}{adj}{reset} mess!",
    f"I saw {red}{fp2}{reset} carrying a {red}{thing}{reset} through the airport. When I asked where they were going, \nthey said they had to {red}{verb}{reset} before sunset. That sounds {red}{adj}{reset}!"

]
rand_sent = random.choice(sentence)

print("\n",rand_sent)