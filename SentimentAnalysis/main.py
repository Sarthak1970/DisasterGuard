from textblob import TextBlob

def get_distress_level(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity < 0:
        distress_level = "High Distress"
    elif 0 <= polarity < 0.5:
        distress_level = "Moderate Distress"
    else:
        distress_level = "Low Distress or Neutral"

    return f"Distress Level: {distress_level}, Polarity: {polarity}, Subjectivity: {subjectivity}"

text1 = "There's a massive forest fire spreading rapidly! The smoke is unbearable, and the flames are getting closer to homes. Wildlife is in danger, and the situation is completely out of control. We need immediate help — firefighters, evacuation plans, and safety measures. Please act now before it's too late!"
text2 = "The nearby building is on fire and the fire is spreading, 5 people are dead and 10 are injured. We need help."

print("Text 1 Analysis:", get_distress_level(text1))
print("Text 2 Analysis:", get_distress_level(text2))
