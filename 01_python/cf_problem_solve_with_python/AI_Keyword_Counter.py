sentence = input().split()

keywords =["ai", "model", "data", "learn", "train", "neural"]
count=0
for word in keywords:
    if(sentence.count(word)):
        count+=1
if(count>=2):
    print("AI Detected")
else:
    print("Not AI Related")