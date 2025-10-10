emoji_categories = {
    'faces': ['😀', '😊', '😎', '🥳', '😍', '🤔'],
    'animals': ['🐶', '🐱', '🐼', '🦁', '🐬', '🦄'],
    'food': ['🍕', '🍎', '🍦', '🍩', '🥑', '🍣'],
    'objects': ['📱', '💻', '🎮', '📚', '🎸', '🚗'],
    'nature': ['🌞', '🌈', '🌺', '🌊', '⛄', '🔥']
}

import random

def get_random_emoji(category):
    if category in emoji_categories:
        return random.choice(emoji_categories[category])
    return None

print(get_random_emoji('faces'))  

for category, emoji_list in emoji_categories.items():
    print(f"{category}: {''.join(emoji_list)}")
