from enum import Enum


class AdjectiveGroup(Enum):
    I = 'i'
    NA = 'na'


ADJECTIVE_GROUP_EXCEPTIONS = {
    'きれい': AdjectiveGroup.NA,
}


def get_group(word: str) -> AdjectiveGroup:
    """Return the adjective group of the given adjective."""

    # Remove the particle です from the word
    word = word.removesuffix('です')

    # Check if the word is in the list of exceptions
    if word in ADJECTIVE_GROUP_EXCEPTIONS:
        return ADJECTIVE_GROUP_EXCEPTIONS[word]

    # Check if the word ends with い
    if word.endswith('い'):
        return AdjectiveGroup.I

    # If the word doesn't end with い, then it is in the na group
    return AdjectiveGroup.NA


def to_neg(word: str) -> str:
    """Return the negative form of the given adjective."""

    group = get_group(word)

    if group == AdjectiveGroup.I:
        if word.endswith('です'):
            return word.removesuffix('いです') + 'くないです'
        else:
            return word.removesuffix('い') + 'くない'

    elif group == AdjectiveGroup.NA:
        if word.endswith('です'):
            return word.removesuffix('です') + 'じゃないです'
        else:
            return word.removesuffix('だ') + 'じゃない'

    raise ValueError(f'Failed to convert to negative form: {word}')


def to_past(word: str) -> str:
    """Return the past form of the given adjective."""

    group = get_group(word)

    if group == AdjectiveGroup.I:
        if word.endswith('です'):
            return word.removesuffix('いです') + 'かったです'
        elif word.endswith('い'):
            return word.removesuffix('い') + 'かった'

    elif group == AdjectiveGroup.NA:
        if word.endswith('です'):
            return word.removesuffix('です') + 'でした'
        elif word.endswith('だ'):
            return word.removesuffix('だ') + 'だった'
        else:
            return word + 'だった'

    raise ValueError(f'Failed to convert to past form: {word}')


def to_past_neg(word: str) -> str:
    """Return the past negative form of the given adjective."""

    return to_past(to_neg(word))
