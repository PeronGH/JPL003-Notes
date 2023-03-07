from enum import Enum
from abc import ABC
import jaconv


class Verb(ABC):
    def __init__(self, kana: str):
        self.kana = kana


class PlainVerb(Verb):
    def __init__(self, kana: str):
        Verb.__init__(self, kana)

    def group(self):
        return VerbGroup.from_verb(self)

    def to_polite(self):
        romaji = jaconv.kana2alphabet(self.kana)
        group = self.group()

        if group == VerbGroup.GodanVerbs:
            romaji = romaji.removesuffix('u') + 'imasu'
        elif group == VerbGroup.IchidanVerbs:
            romaji = romaji.removesuffix('ru') + 'masu'
        elif romaji == 'kuru':
            romaji = 'kimasu'
        elif romaji.endswith('suru'):
            romaji = romaji.removesuffix('suru') + 'shimasu'

        return PoliteVerb(jaconv.alphabet2kana(romaji))


class PoliteVerb(Verb):
    def __init__(self, kana: str):
        Verb.__init__(self, kana)


class VerbGroup(Enum):
    GodanVerbs = 1
    IchidanVerbs = 2
    IrregularVerbs = 3

    @staticmethod
    def from_verb(verb: PlainVerb):
        exceptions = {
            'かえる': VerbGroup.GodanVerbs,
            'きる': VerbGroup.GodanVerbs,
            'しる': VerbGroup.GodanVerbs,
            'はりる': VerbGroup.GodanVerbs,
            'はしる': VerbGroup.GodanVerbs,
        }

        if verb.kana in exceptions:
            return exceptions[verb.kana]

        # ~する / くる -> 3
        if verb.kana.endswith('する') or verb.kana == 'くる':
            return VerbGroup.IrregularVerbs

        # -e or -i + る -> 2
        if verb.kana.endswith('る') and len(verb.kana) >= 2:
            secondLastRomaji = jaconv.kana2alphabet(verb.kana[-2])
            if secondLastRomaji[-1] in {'e', 'i'}:
                return VerbGroup.IchidanVerbs

        # Others -> 1
        return VerbGroup.GodanVerbs
