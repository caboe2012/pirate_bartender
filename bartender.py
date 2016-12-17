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


ingredient_count = {}

segues = ["What else..", "Okay" ,"Let's see...", "Hmmm...", "Well then...", 
          "Let's get some more ideas..."]

drink_adjs = ["Rabid", "Sea-Sick", "Shredded", "Tired", "Flaccid", "Two-Faced", "Broken", "Restless", "Tireless", "Unbeatable"]

drink_nouns = ["Leviathon", "Krackin'", "White-Whale", "Moby Dick", "Sea-Legs", "Land-Lubbarrr", "Will-o-the-Wisp", "Siren",
              "Treasure Chest", "Treasure Map"]

customers = {}

patrons = []

def ask_name():
    repeat = False
    print "Ahoy! My name's Max.  What's yours?"
    print
    name = raw_input()
    another = True
    if name in patrons:
        repeat = True
        print "Of course,", name, "I see you like my drinks ya ol sea-dog!"
        print "I'm like an Elephant Seal, I never forget"
        print "As I recall ya like yer drinks " + ", ".join([pref for pref in customers[name]])
        print "Would you like me to mix another elixir for yee?"
        una_mas = raw_input()
        print
        if una_mas.lower() in ["y", "yes"]:
            print "Una mas it is!"
            for each in customers[name]:
                ingredient_count[each] = ingredient_count.get(each, 0) + 1
            print ingredient_count
        else:
            another = False
            print "Alrighty then, thanks for stopping by, have a nice night!"
            print
    else:            
        patrons.append(name)
        print "Avast, welcome to my humble priate-bar", name, "pleasure to make yer acquaintance."
    return [repeat, name, another]

def ask_questions(name):
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
    customers[name] = [k for k,v in ans_dict.items() if v == True]
    print "One sec and I'll have just the right drink ready for ya..."
    print
    return ans_dict

def make_drink(Ans):
    drink = []
    for k,v in Ans.items():
        if v:
            temp = random.choice(ingredients[k])
            ingredient_count[temp] = ingredient_count.get(temp, 0) + 1
            drink.append(temp)
    print "There ya go matey!"
    return drink

def name_drink():
    print "House special...I call it a", random.choice(drink_adjs), random.choice(drink_nouns)
    print "Enjoy yer libation!"
    need_more = [k for k,v in ingredient_count.items() if v > 3]
    if len(need_more) > 0:
        print "Time to restock the " + ", ".join([more for more in need_more])
        print "Be right back...and stay thirsty friends"
    print
    

if __name__ == "__main__":
    thirsty = True
    repeat_customer = False
    n = 1
    check = 0
    while n > 0:
        repeat_customer = ask_name()
        if not repeat_customer[0]:    
            answers = ask_questions(repeat_customer[1])
            print make_drink(answers)
        if repeat_customer[2]:
            name_drink()
        else:
            # remove the person from the patron list for that night
            patrons.remove(repeat_customer[1])
        print
        n = len(patrons)
        print "Patrons", patrons
        print "Number of patrons left", n
        check += 1
        if check > 10:
            break
    print 
    if check > 5:
        print "Wow, look at the time!"
    else:
        print "Looks like I'm all outta customers for tonight"
    print "Time to close up shop and head home."
        
