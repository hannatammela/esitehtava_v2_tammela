import requests
from collections import Counter
import json
import get
from posts import all_posts, user_all_posts, user_all_words, user_word_list
from save import json_save
from get import get_interface


def main():
    data = get_interface()
    all_posts(data)
    json_save(user_all_posts, user_all_words, user_word_list)

if __name__ == "__main__":
    main()
