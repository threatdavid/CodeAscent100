from typing import List, Literal, TypedDict

WORD_SET = {
    "1": {
        "noun": ["time", "year", "hand", "life", "part", "word", "girl", "city", "face", "area"],
        "pronoun": ["they", "this", "your", "ours", "mine", "hers", "them", "that", "these", "those"],
        "verb": ["have", "know", "make", "take", "give", "look", "find", "call", "work", "keep"],
        "adjective": ["good", "last", "long", "high", "hard", "full", "real", "open", "able", "small"],
        "adverb": ["very", "well", "just", "only", "even", "also", "much", "more", "most", "away"]
    },
    "2": {
        "noun": ["family", "school", "number", "system", "course", "friend", "market", "office", "center", "church"],
        "pronoun": ["another", "himself", "herself", "someone", "anyone", "nobody", "nothing", "themselves", "whenever",
                    "wherever"],
        "verb": ["believe", "receive", "contain", "support", "suggest", "provide", "include", "achieve", "improve",
                 "produce"],
        "adjective": ["several", "important", "popular", "special", "natural", "serious", "various", "further",
                      "central", "certain"],
        "adverb": ["quickly", "already", "clearly", "exactly", "finally", "usually", "recently", "perfectly",
                   "directly", "probably"]
    },
    "3": {
        "noun": ["government", "information", "development", "environment", "relationship", "communication",
                 "responsibility", "organization", "understanding", "experience"],
        "pronoun": ["everything", "themselves", "everybody", "themselves", "whichever", "whatsoever", "whomsoever",
                    "whatever", "whosoever", "whenever"],
        "verb": ["understand", "appreciate", "communicate", "demonstrate", "participate", "acknowledge", "accommodate",
                 "differentiate", "incorporate", "facilitate"],
        "adjective": ["significant", "appropriate", "comfortable", "comprehensive", "independent", "influential",
                      "responsible", "traditional", "universal", "sophisticated"],
        "adverb": ["specifically", "approximately", "unfortunately", "deliberately", "simultaneously", "consequently",
                   "comparatively", "increasingly", "significantly", "subsequently"]
    }
}

CATEGORY_SET = ["noun", "pronoun", "verb", "adjective", "adverb"]


# Custom Typing

class WordSet(TypedDict):
    noun: List[str]
    pronoun: List[str]
    verb: List[str]
    adjective: List[str]
    adverb: List[str]


Category = Literal["noun", "pronoun", "verb", "adjective", "adverb"]

Level = Literal["1", "2", "3"]
