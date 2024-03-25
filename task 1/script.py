import re
import os

all_posts = []
file_path = os.path.join(os.path.dirname(__file__), '..', 'Presidential_Debate.txt')

with open(file_path, 'r') as file:
    all_posts = file.readlines()

biden_mentions = [post for post in all_posts if re.search(r'\b(?:Biden|Joe|JoeBiden|@joebiden)\b', post, re.IGNORECASE)]

trump_mentions = [post for post in all_posts if re.search(r'\b(?:Trump|Donald|@realDonaldTrump)\b', post, re.IGNORECASE)]

wallace_mentions = [post for post in all_posts if re.search(r'\b(?:Chris|Wallace)\b', post, re.IGNORECASE)]

print('BIDEN MENTIONS: ', len(biden_mentions))
print('TRUMP MENTIONS: ', len(trump_mentions))
print('WALLCE MENTIONS: ', len(wallace_mentions))