
def enterTheGate():
    input("\n>>>Press [Enter] to Access the Gate<<<\n")

def enterToContinue():
    input("\n>>>Press [Enter] to Continue<<<\n")

def declined():
    print(f"'Aye, The warrior's path is not for everyone, {userName}. Go in peace...'\n'But should you seek glory, return to the Gate someday.'\n")
    enterToContinue()
    print(
        f"{userName} left the Gate of SkAI without claiming glory, but lived to challenge it another day.")
    print("Setanta the brave corgi shall await your return.\nThanks for Playing!\n")
    exec (exit())

def defeat():
    print(f"It was an honorable end, and challenger {userName} shall join the many lauded names upon the Gate of SkAI...")
    enterToContinue()
    print("\nSetanta the corgi will get you medical attention. He's the bestest boi.\n")
    print(f"Thanks for Playing, {userName}. We hope you'll try again!")
    exec (exit())

def victory():
    print("\nAnd with a final, guttaral roar, the beast collapses, unconscious!\n")
    print(f"The arena erupts into cheers and applause as the corgi waddles back over to you.\n'You did it, {userName}! You ACTUALLY did it! Victory is yours!!'\n")
    enterToContinue()
    print(
        "'With this, you have proven yourself worthy of Lady Skai's blessings, and may venture to the isle, to find your destiny.'")
    enterToContinue()
    print("You seized glory! Congrats. Thank you for playing!")
    exec(exit())

def tamed():
    print("\nApproaching the dragon, you tentatively give its rough head a few scritches...\n")
    print("Which elicits a kind of purring from the creature! It licks your face with a forked, warm tongue.")
    enterToContinue()
    print("\nObserving the now-docile dragon, you hear the corgi approaching from behind, clearing his voice.\n")
    print("'By the powers, I haven't seem anyone manage that since the Lady herself!'\nThe corgi shakes his head in amazement.\n")
    enterToContinue()
    print(f"\n'Well, {userName}, I'd certainly say you've proven yourself with this. Worthy of Skai herself.\n")
    print("'With that, you may venture on to the isle, and find your destiny.'")
    print("\nWith that, the crowd erupts into cheers of your name!\n")
    print(f"\nWell done, {userName}, you found a hidden ending! Thanks for playing!\n")
    exec(exit())

def skaiVictory():
    print("\n'As efficient as ever, milady! Well done. Shall I expect you again soon?'\n")
    print("With a knowing smirk, you bend down and ruffle Setanta's soft ears, before standing tall and advancing.")
    print("Setanta watches you go until you are out of sight. He's a good boy, and you know he will return to his post.\nThank you for returning! Until next time, master!\n")
    exec(exit())


print ("\nSo it begins anew!\n")
print("You are walking on a windswept shore, approaching a massive, ornate black gate.\nA small, black corgi with a spear on its back beckons you as you arrive.\n")

while True:
    userName = input("'Let's get started, challenger! What's your name?'").strip().lower()

    if (userName == ("skai").casefold()) or (userName == ("lady skai").casefold):
        print("\n'Oh, Milady! You're back! Forgive me for not recognizing you! Welcome back.'\n")
        break
    elif (userName == ("you")) or (userName == ("whats yours")) or (userName == ("whatsyours")):
        print("\nThe adorable corgi blinks a few times, clearly surprised, before composing himself and clearing his throat\n")
        print("\n'*Ahem* Call me Setanta, pleasure. And uh...thanks for asking. Now let's get back to you.'\n")
        continue
    elif (userName == ("pet")) or (userName == ("pet corgi")) or (userName == ("pet dog")) or (userName == ("can i pet you")) or (userName == ("pet setanta")):
        print("\nThe corgi hops back quickly and shakes his head\n")
        print("\nWhat kind of dog do you take me for? I just met you! Now stay focused!!\n")
        continue
    elif userName == ("setanta"):
        print("\nThe corgi's tiny nub of a tail begins wagging excitedly as he takes a step towards you.\n")
        print("\n'SHUT. UP. That's my name, too!!'\n")
        break
    else:
        confirm = input(f"'So your name is {userName}, right?'\ny/n\n").strip().lower()
        if (confirm == ("yes")) or (confirm == ("y")) or (confirm == ("yeah")):
            userName == True
            print (f"'Great, strong name! It's good to meet you, {userName}!'\n'Best of luck.'\n")
            break
        elif (confirm == ("no")) or (confirm == ("n")) or (confirm == ("nope")):
            userName == False
            print ("'Oh, my mistake. We should probably start over then!'")
            continue
        else:
            print("'Dang, I swear this always happens. Alright, we'll take it from the top! Stay focused!'")
            continue
enterTheGate()
print(f"\n{userName} has entered the Gate of SkAI!\n")


print("As the massive dark gates sweep open, a massive arena greets you, and the corgi continues speaking as he follows you.")
print("\n'Sorry, protocol. You're stuck with me, and I've gotta announce you.'\n")
enterToContinue()
print("He stops you a small ways into the arena, which you now see has many people around its outer wall, watching.\nThe corgi then calls out loudly:\n")
print("\n'The challenger's abilities shall now be evaluated!'\n")
enterToContinue()

pwr = input(f"'Challenger {userName}, how STRONG are you?' \n(0-5):").casefold()
Strength = pwr
honestStrength = True
if (pwr == ("skai")) or (pwr == ("lady skai")):
    pwr = 7
    print(f"\n'Of course, a {pwr}! As strong as ever then, Milady!'\n")
else:
    try:
        pwr = int(pwr)
        print(f"'Challenger {userName}'s strength is {pwr}!'")
    except (TypeError, ValueError):
        honestStrength = False
        pwr = 0
    if pwr < 0:
        honestStrength = False
        pwr = 0
    elif pwr > 5:
        honestStrength = False
    if not honestStrength:
        hiddenPower = 5
        truePower = int(pwr) + int(hiddenPower)
        print(
            f"\n'Wait, what do you mean your strength is {str(Strength)}?? What's the protocol for this...'\n")
        print("\nThe corgi materializes a small scroll from the rig holding his spear on his back, and begins consulting it.\n")
        enterToContinue()
        print(
            f"'Ah here it is, you're a special challenger, then! We'll account for your...unique power...'")
        enterToContinue()
        print("\nHidden Strength Unlocked!\n")
        print(f"\n'By the powers, it appears challenger {userName}'s strength is {truePower}!!'\n\nUpon his decree, murmurs can be heard around the arena.\n")

def tPwr_t():
    return int(pwr)
def tPwr_f():
    return int(truePower)
if honestStrength == True:
    tPwr_func = tPwr_t
else:
    tPwr_func = tPwr_f
totalPower = tPwr_func()




spd = input(f"'And how FAST would you say you are, {userName}?'\n(0-5)\n").casefold()
Agility = spd
honestAgi = True
if (spd == ("skai")) or (spd == ("lady skai")):
    spd = 10
    print(f"\n'{spd}, naturally! Ahem...apologies, Milady, but these questions are required for every challenger,'\n")
    print("'per YOUR mandate, of course.'")
else:
    try:
        spd = int(spd)
        print(f"\n'Challenger {userName}'s agility is {spd}!'\n")
    except (TypeError, ValueError):
        honestAgi = False
        spd = 0
    if spd < 0:
        honestAgi = False
        spd = 0
    elif spd > 5:
        honestAgi = False
    if not honestAgi:
        arrowedKnee = 2
        superSpeed = 5
        trueSpeed = int(spd) + int(superSpeed)
        print(
            "'Oh not another one, that's not right...Let me consult the verba on this...'\nAgain, he materializes the small scroll."
        )
        enterToContinue()
        mobility = input(f"'Ah, here we are. Now, {userName}...did you take an arrow to the knee?'\ny/n\n").casefold()
        if (mobility == ("y")) or (mobility == ("yes")):
            mobility = False
            print(f"'Ah I see, my condolences. Then {userName}'s agility is limited to {arrowedKnee}.'")
        elif (mobility == ("n")) or (mobility == ("no")):
            mobility = True
            print("'I think I understand, now. A speedster, eh? We don't get many of those.'")
            enterToContinue()
            print("Enhanced Agility Unlocked!")
            print(f"'Accounting for that...By the divine, {userName}'s agility is {trueSpeed}!!'")
        else:
            spd = arrowedKnee
            print("'...I'm just going to put down a 2, and you'll have to make do.'")
            enterToContinue()
            print(f"'*Ahem*, Challenger {userName}'s agility is {spd}!'")

def tSpd_t():
    return int(spd)
def tSpd_f():
    return int(arrowedKnee)
def tSpd_s():
    return int(trueSpeed)
if honestAgi == True:
    tSpd_func = tSpd_t
elif mobility == True:
    tSpd_func = tSpd_s
else:
    tSpd_func = tSpd_f
totalSpeed = tSpd_func()





print(f"\n'Excellent! So challenger {userName}'s strength is {totalPower} and their speed is {totalSpeed}!'\n")
print("You can check these by typing 'stats' during most prompts!")

while True:
    creationComplete = input(f"'Now, are you ready to continue, {userName}?'\ny/n\n").casefold()
    if creationComplete == ("stats"):
        print(f"\n{userName}'s strength is {totalPower}, and their speed is {totalSpeed}.\n")
        continue        
    elif (creationComplete ==("n")) or (creationComplete == ("no")):
        print("\n'Oh? Well, you've come a long way to stop now. Take a moment, then!'\n")
        continue
    elif (creationComplete == ("y")) or (creationComplete == ("yes")):
        print("\n'Aye, that's the spirit!'\n")
        break
    else:
        print("\n'*Sigh*, you're not making this easy, are you? Ok, time to move on.'\n")
        break







print("\nThe corgi leads you to the center of the arena, where he stops and takes a breath\n")
print(f"'I'm gonna level with you, {userName}...if you wanna pass through, you need to fight a dragon.'")
enterToContinue()

print("\nThe corgi watches you carefully for a moment, before sitting down in front of you.\n")

while True:
    riseToOccasion = input("\n'Sooo...are you in? There's no shame in going back the way you came.'\n\ny/n\n").casefold()

    if (riseToOccasion == ("y")) or (riseToOccasion == ("yes")):
        print(f"\n'That's the spirit, {userName}! To glory!!'\n")
        print("The corgi spins excitedly in place, before howling upwards loudly.")
        break
    elif riseToOccasion == ("stats"):
        print(f"\n{userName}'s strength is {totalPower}, and their speed is {totalSpeed}\n")
        continue
    elif (riseToOccasion == ("n")) or (riseToOccasion == ("no")):
        print("\nThe corgi's ears droop slightly, but he nods calmly in thought before meeting your eyes.\n")
        print(f"\n'I understand, {userName}, I do. Then, I'll escort you back through the Gate.'\n")
        enterToContinue()
        declined()
    else:
        print("\nThe corgi grumbles, and shifts in place.\n\n'Would it kill ye tae just givva straight answer, mate?'\n")
        continue



print("\nThe observers surrounding the arena give a hearty cheer as well, before a deep horn sounds from nearby.\n")
enterToContinue()

print("The corgi scampers a ways off, leaving you alone in the center of the arena.")
print(f"\n'Don't hurt it too bad, okay? You just have to knock it out, {userName}'.\n\n'I'm rooting for you!!'\n")
enterToContinue()

print("\nNearby, a roar beckons your attention upwards!\n")
print("With a gust of wind, a dark dragon lands from the skies above not 10 feet ahead of you!")
print("\nThe dark creature isn't much larger than a horse, so it must still be rather young.\n\nIt watches you with sharp, yellow eyes.\n")
enterToContinue()

while True:
    firstMove = input("It curls its tail around, poised to strike at you! \nHow do you respond?(Attack, Dodge, Hold.)\n").casefold()

    if firstMove == ("stats"):
        print(f"\n{userName}'s strength is {totalPower}, and their speed is {totalSpeed}.\n")
        continue
    elif firstMove == ("attack"):
        if totalPower >= 10:
            print("\nyou step in quickly and slam your fist into the dragon, sending it reeling back with overwhelming force!!\n")
            print("The arena falls silent for a moment...")
            enterToContinue()
            print("\nThe crowd then breaks into deafening cheers and applause!\n")
            victory()
                        
        elif totalPower >= 5:
            print("\nScrambling quickly, you manage a hearty strike against the beast, surprising it as it steps back.\n")
            break
        elif totalPower >= 3:
            print("\nDaringly, you stumble forward and sock the beast's face, and it takes a moment to reorient itself.\n")
            print("\nThe dragon meets your gaze, your strike clearly ineffective, but it seems to appreciate your gusto.\n")            
            break
        else:
            print("\nYou fling your limp, noodle-like arm at the beast, and crack your fist against its hide.\n")
            print("\nThe dragon stares back at you, unimpressed, before slamming its tail into you, sending you flying back!\n")
            enterToContinue()
            print("With great effort, you find your footing again, as the crowd reacts to the strike.\nYour chest aches from the blow.\n")
            break
    elif firstMove == ("dodge"):
        if totalSpeed >= 5:
            print("\nYou move with blinding speed, tearing through the air as you swiftly evade the dragon's tail!\n")
            print("The crowd is stunned into silence by your display of agility, and the dragon rushes to find you again.")
            break
        elif totalSpeed >= 2 :
            print("\nYou move in time with the dragon's strike, and while it hits you, you lessen the greatly lessen the impact!\n")
            print("Stumbling back, you size eachother up again, the crowd cheering around you.")
            break
        else:
            print("\nAs you bumble to the side, the dragon's tail catches you square in the chest, and you're sent flying!!\n")
            print("\nYou slam back to the ground heavily, and need a moment to find your breath again. The crowd winces.\n")
            break
    elif firstMove == ("hold"):
        print("\nYou don't move, and instead hold the dragon's fearsome gaze steadily.\n")
        enterToContinue()
        print("\nTo your surprise, the dragon does the same, and it tilts its head inquisitively for a moment...\n")
        break
    elif firstMove == ("skai"):
        print("\nWith unshaken confidence, you command the dragon to recognize its owner with a thump of your spear.\n")
        print("As if snapping out of a daze, the young dragon sits down with a mewl, and gazes at you in recognition!")
        enterToContinue()
        skaiVictory()        
    else:
        print(f"\nIn the distance, you can hear the corgi calling out to you:\n\n'Now's not the time for that! Stay focused, {userName}!'\n")
        continue



print("\nCentering itself opposite you, the dragon now digs its maw into the earth, and lifts out a rock the size of your head!\n")
enterToContinue()

while True:
    nextMove = input("\nWith a growl, the dragon prepares to hurl the rock at you!\n\nWhat do you do?(Catch, Dodge, Nothing)\n").casefold()

    if nextMove == ("stats"):
        print(f"\n{userName}'s strength is {totalPower}, and their speed is {totalSpeed}.\n")
        continue
    elif (nextMove == ("catch")) or (nextMove == ("catch it")) or (nextMove == ("catch rock")):
        if totalPower >= 10:
            print("\nHolding a palm out, you easily absorb the projectile's force,\n\nand the crowd murmers as you crush the stone to pieces within your grasp.\n")
            enterToContinue()
            print("The beast seems to recognize the power required for this feat, and actually retreats slightly!")
            hasRock = False
            enterToContinue()
            break
        elif totalPower >= 5:
            print("\nEmptying your lungs quickly, you brace your entire body as you catch the rock, and shuffle back with it, unharmed!\n")
            print("\nAs the crowd cheers, the beast watches you with interest, and you swear it narrows its eyes at you.\n")
            hasRock = True
            enterToContinue()
            break
        elif totalPower >= 3:
            print("\nYou hunker down as best you can and catch the rock with both arms as it careens into your stomach!\n")
            print("\nThe wind is knocked out of you, as you are bowled over in kind, sliding a few feet across the ground.\n")
            enterToContinue()
            print("\nAs the crowd winces, some begin to clap as they realize the rock rests between your hands.\n")
            print("The dragon's gaze falls from you to the rock in your hands as you work yourslef back to your feet.\nYou could swear you notice its tail wagging...\n")
            hasRock = True
            enterToContinue()
            break
        else:
            print("\nYou watch the rock as it is hurled towards you, and lunge to grab it out of the air!\n")
            enterToContinue()
            print("\nWith a hefty thump, and perhaps a couple of crunches, the projectile slams your arm into your chest, bowling you over!\n")
            print("\nThe crowd winces sharply, and someone gags at your forearm's...interesting new angle. But you're still alive!\n")
            print("You could swear the dragon laughs at you as it flashes its fangs.")
            hasRock = False
            enterToContinue()
            break
    elif nextMove == ("dodge"):
        if totalSpeed >= 10:
            print("\nWith a burst of wind, you blast past the rock before it's even half-way to you, and skid to a halt past the dragon!\n")
            print("As the crowd is stunned into silence at your display, the dragon spins around to face you again, nervous")
            hasRock = False
            enterToContinue()
            break
        elif totalSpeed >= 5:
            print("\nWith superfluous agility and grace, you effortlessy bend your body back, watching as the rock hurtles just past your face!\n")
            print("The crowd exclaims in amazement at your agility, as the dragon seems taken aback, but impressed, by your maneuver.")
            hasRock = False
            enterToContinue()
            break
        elif totalSpeed >= 3:
            print("\nAs you see the rock leave the dragon's grasp, you recklessly hurl yourself to the side!\n")
            enterToContinue()
            print("\nBut you're not quite fast enough, and the rock slams into your shoulder, spinning you onto your back.\n")
            print("The crowd winces as you fumble on the rock and find your footing again, \nonce up, the dragon focuses in on you again. That's gonna bruise...\n")
            hasRock = False
            break
        else:
            print("\nYou move to evade the rock, but stumble forward clumsily, and you can hear the crowd wince as\n\nthe rock meets your face in a most unceremonious fashion...\n")
            enterToContinue()
            print("You are VERY much knocked unconcious.")
            enterToContinue()
            defeat()
            break
    elif nextMove == ("nothing"):
        print("\nWith a sigh, you...do nothing as you watch the rock hurtle towards you??\n")
        enterToContinue()
        print("\nSuddenly, a spear flies in from behind you, and knocks the rock to the ground where it rolls to your foot!.\n")
        print("You watch as the spear is bounced out of sight from the impact.")
        enterToContinue()
        print("\nFrom the perimeter of the arena, you hear the corgi calling out to you:\n")
        print(f"'Get your head in the game, {userName}! I don't have another spear to bail you out with!!'")
        aRock = input("Do you...wanna pick up the rock?\n(y/n)\n").casefold()
        if (aRock == ("y")) or (aRock == ("yes)")):
            print(f"\n{userName} picked up the rock!\n")
            hasRock = True
            enterToContinue()
            break
        elif (aRock == ("n")) or (aRock == ("no")):
            print(f"\n{userName} leaves the rock on the ground.\n")
            hasRock = False
            enterToContinue()
            break
        else:
            print(f"\n{userName} looked at the rock before mumbling incoherently, and turned back to the dragon.\n")
            hasRock = False
            enterToContinue()
            break
    else:
        print("\nAs you deliberate on how to pull that off, the corgi calls out to you:\n")
        print(f"\n'Get your head in the game, {userName}! Show some warrior spirit!!'\n")
        continue

def rock_t():
    return ("are holding a rock")
def rock_f():
    return ("aren't holding a rock")
if hasRock == True:
    rock_func = rock_t
else:
    rock_func = rock_f
rockCheck = rock_func()


print("\nWatching you carefully, the dragon hunkers itself down, as if to pounce!\n")
enterToContinue()

while True:
    lastMove = input("As a decisive glint enters its yellow eyes, you know you must act now!\n(Attack, Dodge, Sit, Rock)\n").casefold()

    if lastMove == ("stats"):
        print(f"\n{userName}'s strength is {totalPower}, their speed is {totalSpeed}, and they {rockCheck}.\n")
        continue

    elif lastMove == ("attack"):
        if totalPower >= 10:
            print("\nWaiting until the dragon makes its move, you prepare your strike...\n")
            enterToContinue()
            print("\nThe dragon launches itself at you through the air, but you're more than ready.\n\nAs it bears down on you, you send a fist straight into its hide!\n")
            print("With a draconic wheeze, the beast is flung back through the air until it crashes back into the earth, a smirk on your face.")
            enterToContinue()
            print("\nThe arena is silent for a moment...\n")
            enterToContinue()
            victory()
        elif totalPower >= 5:
            print("\nCracking your knuckles, you leap to meet the dragon in the air as it pounces!\n")
            enterToContinue()
            print("\nWith a roar of your own, you bring down a mighty blow over its head, sending it careening into the ground below!\n")
            print("The crowd watches on in shocked silence as you land powerfully, and swipe some dust from your shoulder.")
            enterToContinue()
            victory() 
        elif totalPower >=3:
            print("\nWatching as the beast launches itself through the air, you wind back your punch!\n")
            enterToContinue()
            print("\nYou set your best strike against the dragon as it slams down onto you, crushing you to the ground.\n")
            print("As your vision fades, you see the dragon stumbling in place. At least it definitely felt that...")
            enterToContinue()
            defeat()
        else:
            print("\nThe dragon careens through the air with a mighty roar and you let loose your strike to meet it!\n")
            enterToContinue()
            print("\nUnfortunately, you aren't as strong as a hopped-up dragon, and it thoroughly crushes you...\n")
            enterToContinue()
            defeat()
    elif lastMove == ("dodge"):
        if totalSpeed >= 10:
            print("\nThe air around you struggles to move out of your way as you blast under the dragon like a comet!\n")
            enterToContinue()
            print("\nLooking over your shoulder, you watch as the dragon slams into the ground with enough force to stagger itself.\n")
            print("All around you, the crowd exclaims loudly at your feat of speed!")
            enterToContinue()
            victory()
        elif totalSpeed >= 5:
            print("\nA small smirk appears on your face as you watch the dragon launch itself into the air.\n")
            enterToContinue()
            print("\nTiming it perfectly, you wait as the dragon comes careening down towards you,\n")
            print("and you dive right past it at the last possible moment!! Dust flies up, obscuring you both.")
            print("The entire arena seems to hold its breath...")
            enterToContinue()
            victory()
        elif totalSpeed >= 3:
            print("\nNervously, you watch the dragon launch itself over towards you, your legs prepared to move...\n")
            enterToContinue()
            print("\nAt the last moment, you launch yourself to the side!\n")
            print("And watch with a sinking sensation as you realize you aren't fast enough, and the dragon lands on you...")
            enterToContinue()
            defeat()
        else:
            print("You move as the dragon leaps into the air!")
            enterToContinue()
            print("\nAnd trip over yourself, landing face-first on the ground, eliciting audible winces from the crowd.\n")
            print("You have a moment to yourself on the ground to sigh and accept your fate, before the dragon crashes onto you.")
            enterToContinue()
            defeat()
    elif lastMove == ("sit"):
        print("\nFollowing an incomprehensible string of logic, you choose to simply sit down, and lock eyes with the dragon?!\n")
        enterToContinue()
        print("\nThe dragon cocks its head to the side as it stare at you, seemingly confused.\n")
        print("A tense silence fills the arena as the beast flicks its yellow gaze over your posture...\nIt approaches you, and sniffs you curiously, before staring deep into your eyes...\n")
        enterToContinue()
        print("\nThen, for some reason, the dragon mirrors your action, and sits down across from you??\n")
        print("Cautiously, you rise back to your feet, and while the dragon watches you with round eyes, it remains seated.")
        tamed()
    elif lastMove == ("rock"):
        if hasRock == True:
            print("\nHefting the rock previously aimed at your head in your arms, you watch the dragon carefully.\n")
            print("Its focus immediately shifts to the rock, and you smirk as you notice its tail wag.")
            enterToContinue()
            print("\nWith some effort, you manage an acceptible toss of the weighty object,\n")
            print("and nearly stumble back as the dragon bounds upwards to catch the rock in its mouth!")
            print("As the dragon lands on the ground, it throws the rock to the ground, nudging it back to you.")
            print("The creature then...sits down in front of you, round yellow eyes watching you excitedly.")
            enterToContinue()
            tamed()
        else:
            print("\nThinking quickly, your attention goes to what's left of the rock on the ground,\n\nand you scramble towards it!\n")
            enterToContinue()
            print("\nUnfortunately, it seems it was unwise to take your attention away from the dragon.\n")
            print("Focused on the rock as you are, you don't even know what the dragon clobbers you with...")
            enterToContinue()
            print("\nOnly that it hurt. A lot.\n")
            defeat()
    else:
        print("\nShuffling in place, you try to figure out how you'd manage that, when the corgi calls out to you again:\n")
        print(f"\n'Head out of the clouds, {userName}, you can do this!!'\n")
        continue


