emotions={"happy":"😊","sad":"😢","angry":"😠","love":"❤️","surprised":"😲","confused":"😕",
          "bored":"😐","tired":"😴","excited":"🤩","nervous":"😬"}
print(emotions)
text=input("Enter your message: ").strip()
for word, emoji in emotions.items():
    text = text.replace(word, emoji)
print("converted message:",text)
