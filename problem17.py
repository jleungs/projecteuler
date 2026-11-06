words = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

def pprint(n):
    ones = n % 10
    tens = (n % 100) // 10 * 10
    hund = (n % 1000) // 100
    if tens < 20:
        tens = tens + ones
        ones = 0
    
    rets = ""
    if hund:
        rets += f"{words[hund]}hundredand"
    if tens:
        rets += words[tens]
    if ones:
        rets += words[ones]

    return rets[:-3] if rets[-3:] == "and" else rets
        
letters = "".join(pprint(i) for i in range(1000)) + "onethousand"
print(letters)
print(len(letters))

