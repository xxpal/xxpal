def search4vowels(phrase: str) -> set:
    """Display any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    # word = input('Provide a word to search for vowels:')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


if __name__ == '__main__':
    print(search4vowels('hitch-hiker'))
    print(search4vowels('galaxy'))
    print(search4vowels('life, the universe and everything'))
    print(search4vowels('sky'))

    help(search4letters)
    print(search4letters('hitch-hiker', 'aeiou'))
    print(search4letters('galaxy', 'xyz'))
    print(search4letters('life, the universe, and everything.', 'o'))
