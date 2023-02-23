import adjectives


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
