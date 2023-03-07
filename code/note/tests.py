import adjectives
from verbs import VerbGroup, PlainVerb


def test_adj(word: str):
    print(f'Present Aff. {word}')
    print(f'Present Neg. {adjectives.to_neg(word)}')
    print(f'Past Aff.    {adjectives.to_past(word)}')
    print(f'Past Neg.    {adjectives.to_past_neg(word)}')
    print()


i_adjectives = ['あついです', 'おいしい']

for i_adjective in i_adjectives:
    test_adj(i_adjective)

na_adjectives = ['きれいです', 'すきだ']

for na_adjective in na_adjectives:
    test_adj(na_adjective)


verbs = [
    # Group 1
    'ある', 'かう', 'かく',
    # Group 2
    'いる', 'おきる',
    # Group 3
    'する', 'くる',
    # Practice
    'あそぷ', 'のむ', 'わすれる', 'わくれる', 'しめ', 'べんきょうする', 'できる', 'くる', 'かえる',
]

for verb in verbs:
    print(f'{verb} is in group {VerbGroup.from_verb(PlainVerb(verb)).value}')
    print(f'Polite form: {PlainVerb(verb).to_polite().kana}')
    print()
