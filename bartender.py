import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

segues = ["What else..", "Okay" ,"Let's see...", "Hmmm...", "Well then...", 
          "Let's get some more ideas..."]

def ask_questions():
    ans_dict = {}
    counter = 0
    for k,v in questions.items():
        print v
        ans = raw_input()
        counter += 1
        if ans.lower() in ["y", "yes"]:
            ans_dict[k] = True
            print
            print "Arrr, summin'", k, "iddle be then."
        else:
            print
            print "Arr, nothing", k, "then matey."
            ans_dict[k] = False
        if counter <=4:
            print random.choice(segues)
            print
    print "One sec and I'll have just the right drink ready for ya..."
    print
    return ans_dict

def make_drink(Ans):
    drink = []
    for k,v in Ans.items():
        if v:
            temp = random.choice(ingredients[k])
            drink.append(temp)
    print "There ya go matey, enjoy yer libation!"
    return drink

if __name__ == "__main__":
    answers = ask_questions()
    print make_drink(answers)