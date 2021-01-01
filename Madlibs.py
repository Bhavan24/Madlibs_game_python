import random

player_name = input("Please Enter your Name: ")
welcome_text = "Welcome to Madlibs game... Enter the correct words"

while True:
    adjective1 = input("Adjective: ")
    adjective2 = input("Adjective: ")
    adjective3 = input("Adjective: ")
    adjective4 = input("Adjective: ")
    adverb1 = input("Adverb: ")
    adverb2 = input("Adverb: ")
    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    noun3 = input("Noun: ")
    noun4 = input("Noun: ")
    noun5 = input("Noun: ")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    verb3 = input("Verb: ")

    madlib1 = f'''           
                                A Day At The Zoo!
    Today I went to the zoo. I saw an {adjective1} {noun1} jumping up and down in its tree.
    He {verb1} {adverb1} through the large tunnel that led to its {adjective2} {noun2}. 
    I got some peanuts and passed them through the cage to a gigantic gray {noun3}
    towering above my head. Feeding that animal made me hungry. 
    I went to get a {adjective3} scoop of ice cream. It filled my stomach. 
    Afterwards I had to {verb2} {adverb2} to catch our bus. When I got home I {verb3} my
    mom for a {adjective4} day at the zoo.'''

    madlib2 = f'''                             
                                     The Fun Park!
    Today, my fabulous camp group went to a {adjective1} amusement park. It was a
    fun park with lots of cool {noun1} and enjoyable play structures. When we got there, my
    kind counselor shouted loudly, "Everybody off the {noun2}." We all pushed out in a terrible
    hurry. My counselor handed out yellow tickets, and we scurried in. I was so excited! I couldn't figure out
    what exciting thing to do first. I saw a scary roller coaster I really liked so, I {adverb1} ran
    over to get in the long line that had about 10 people in it. When I finally
    got on the roller coaster I was {verb1}. In fact I was so nervous my two knees
    were knocking together. This was the {adjective2} ride I had ever been on! In about two
    minutes I heard the crank and grinding of the gears. That’s when the ride began! When I got to the bottom,
    I was a little  {verb2} but I was proud of myself. The rest of the day went {adverb2}. 
    It was a {adjective3} day at the fun park. 
    '''

    madlib3 = f'''    
                                    At The Arcade!
    When I go to the arcade with my {noun1} there are lots of games to play.
    I spend lots of time there with my friends. In the game X-Men you can be different {noun2}.
    The point of the game is to {verb1} every robot. You also need to save people.
    Then you can go to the next level. In the game Star Wars you are Luke Skywalker and you try to destroy every {noun3}.
    In a car racing/motorcycle racing game you need to beat every computerized vehicle that you are {verb2} against.
    There are a whole lot of other cool games. When you play some games you win {noun3} for certain scores. 
    Once you're done you can cash in your tickets to get a big {noun4}. You
    can save your {noun5} for another time. When I went to this arcade I didn't believe how much fun it would be.
    So far I have had a lot of fun every time I've been to this great arcade! 
    '''
    madlib_list = [madlib1,madlib2,madlib3]
    
    print()
    print(random.choice(madlib_list))
    print("\nGood job! " + player_name)

    another_game = input("\nDo you want to play another game!(y/n): ")

    if another_game == "n":
        break
    else:
        continue

print("Thank you playing!")