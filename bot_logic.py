import random
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923","\U00002764","\U0001f975","\U0001f1f7\U0001f1fa","\U0001f97a","\U0001f976","\U0001f649"]
    return random.choice(emodji)
def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"
