sentence = input()
sentence = sentence.lower()
if(sentence.count("happy") or sentence.count("joy") or sentence.count("smile")):
    print("Happy Mood")
elif(sentence.count("sad") or sentence.count("cry") or sentence.count("angry")):
    print("Sad Mood")
else:
    print("Neutral Mood")