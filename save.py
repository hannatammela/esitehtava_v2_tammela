import json
from collections import Counter

def json_save(user_all_posts, user_all_words, user_word_list):
    # Pääsanakirja JSON-datan tallennusta varten
    json_data = {"users": {}}

    # Käydään läpi kaikki käyttäjä-ID:t
    for id_user in user_all_posts.keys():
        total_posts = user_all_posts[id_user] # Postausten kokonaismäärä
        total_words = user_all_words[id_user] # Sanojen kokonaismäärä
        average_words = total_words / total_posts
        top_5_words_user = Counter(user_word_list[id_user]).most_common(5)

    # Tallennetaan tiedot JSONiin
        json_data["users"][id_user] = {
            "Posteja": total_posts,
            "Sanoja": total_words,
            "Sanoja keskimaarin": average_words,
            "Top 5 sanat" : top_5_words_user
    }

    # Tallennetaan JSONiin nimellä userdata.json
    with open ("userdata.json", "w") as json_file:
        json.dump(json_data, json_file, indent=4)