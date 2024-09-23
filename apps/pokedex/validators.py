import re

def img_pokemon_invalid(img_pokemon):
    if img_pokemon != '':
        pattern = r'^(http|https):\/\/([\w.-]+)(\.[\w.-]+)+([\/\w\.-]*)*\/?$'
        value = bool(re.match(pattern, img_pokemon))
        return not value
    