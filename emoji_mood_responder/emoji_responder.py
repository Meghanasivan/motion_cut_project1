# emoji_responder.py

mood_dict = {
    "happy": ("😊", "That's wonderful! Keep smiling!"),
    "sad": ("😢", "It's okay to feel sad. Tomorrow is a new day."),
    "angry": ("😠", "Take a deep breath. It'll get better."),
    "excited": ("🤩", "Yay! Enjoy the excitement!"),
    "tired": ("😴", "Rest well! You deserve it.")
}

user_mood = input("How are you feeling today? ").lower()

if user_mood in mood_dict:
    emoji, message = mood_dict[user_mood]
    print(f"{emoji} {message}")
else:
    print("🤔 Hmm, I don't recognize that mood, but I hope you have a great day!")
