def search4vowels(phrase:str) -> set:
    """Return any vowels found in a supplied phrase"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str,letters:str) -> set:
    """Return a set letters found in a phrase"""
    return set(letters).intersection(set(phrase))
