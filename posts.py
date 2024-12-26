# Tehdään dictionary postien määrälle,
# kaikille sanoille ja lista top 5 sanoille
user_all_posts = {}
user_all_words = {}
user_word_list = {}
all_words_list = []

# Käydään läpi jokainen posti datassa
def all_posts(data):
    for content in data:
        id_user = content["userId"]
        words = content["body"].split() # Jaetaan postien tekstit sanoiksi
        all_words = len(words)
        all_words_list.extend(words) #Lisätään sanat yleiseen sanalistaan

        # Jos käyttäjää ei vielä ole sanakirjoissa, alustetaan tiedot
        if id_user not in user_all_posts:
            user_all_posts[id_user] = 0
            user_all_words[id_user] = 0
            user_word_list[id_user] = []

        # Tässä päivitetään käyttäjän tiedot
        user_all_posts[id_user] += 1
        user_all_words[id_user] += all_words
        user_word_list[id_user].extend(words)