1
'''
In these tasks you will be given one or more examples of code.

- Look at each example , study it carefully.
- Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms list, item and index in your predictions.
- Run the code, compare what happens to your prediction.
- Add comments to note down and differences between your prediction and what actually happened.

'''

# Example Code 1

Sentence = ["Always", "look", "on", "the", "bright", "side", "of",]
print(Sentence)
# will print all items in the list by order
print(Sentence[1])
# it will print look
Sentence.append("life")
# adds one more word to the list
Sentence[4] = "sunny"
# bright --> sunny, changing the 5th word
print(Sentence[4])
# sunny
print(Sentence[0] + " " + Sentence[3])
# Always the
print(Sentence)
# [Always, look, on, the, sunny, side, of , life]