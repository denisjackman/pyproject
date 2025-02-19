'''
    Name : TabConverter.py

    Function :
    This is a converter for the Data items from TAB files to JSON files
    The TAB files are from the DnD 5e SRD
'''
__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.00 $"
__date__ = "$Date: 2022/11/01 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
import json

FILEPATH = "Z:/Resources/development/"
# pylint: disable=too-many-locals


def main():
    '''
        main function
    '''
    oracle_noun = ("endless capacity", "life", "wondering person", "intention",
                   "core", "fluid", "delicious fruit", "fruition", "wheel",
                   "dream", "purpose", "desire", "reason", "world", "light",
                   "power", "work", "change", "energy", "job", "choice",
                   "Spirit", "nature", "connection", "fire", "dancer",
                   "offering", "peace", "simple unity", "forgiving act",
                   "center", "source", "glowing ember", "spiritual food",
                   "practical purpose", "ocean", "doubt", "faith", "ritual",
                   "practice", "student", "teacher", "sacred time", "soul",
                   "winding path", "challenge", "transformation", "transience",
                   "burden", "release", "support", "oracle", "direction",
                   "wondering", "God", "local community", "world community",
                   "creation", "relaxation", "moving planet", "gift",
                   "present", "never-failing Source", "body", "part", "mind",
                   "river", "waterfall", "leader", "community", "soul",
                   "lesson", "destination", "journey", "confusion",
                   "striking clarity", "lover", "home", "serendipitous design",
                   "similar dream", "hope", "loving action", "joy", "path",
                   "gateway", "transcendent experience", "angel", "soul guide",
                   "curious spirit", "song", "method", "map", "blueprint",
                   "received wisdom", "block", "true wonder", "star",
                   "entire universe", "immense sky", "whole", "tree", "branch",
                   "power", "peace maker", "genius", "seed", "marvelous ruby",
                   "wondrous alchemy", "turning", "hidden science", "jewel",
                   "forest", "exchange", "remembered passion",
                   "fiery stillness", "elder", "communication", "root",
                   "crossroads", "nexus", "way", "integrated reality",
                   "integral notion", "catharsis", "distinction",
                   "compassionate action", "forgiving word", "action", "cycle",
                   "feeling", "season", "harvest", "dawn", "birth", "notion",
                   "circle", "ring", "myth", "radical truth", "essence",
                   "infinite and gentle force", "spiritual cycle", "reason",
                   "graceful act", "discovery", "need", "forgotton mystery",
                   "wing", "motivation", "structure")
    oracle_preposition = ("of", "from", "near", "about", "around", "for",
                          "toward", "over", "behind", "beyond", "related to",
                          "defined by", "within", "living with")
    oracle_adverb = ("knowingly", "consciously", "gently", "emphatically",
                     "enthusiastically", "strangely", "surprisingly", "nearly",
                     "yearningly", "non-chalantly", "hardly", "eagerly",
                     "purposefully", "actively", "inexorably", "accurately",
                     "accidentally", "completely", "differently",
                     "single-handledly", "consciously", "almost", "wisely",
                     "creatively", "somewhat", "overwhelmingly", "seldom",
                     "often")
    oracle_adjective = ("quick", "kind", "gentle", "optimal", "challenging",
                        "loyal", "sweet", "ravishing", "stimulating", "strong",
                        "activating", "graceful", "devoted", "global",
                        "genuine", "magnificent", "masked", "separated",
                        "gratifying", "elusive", "revered", "rigorous",
                        "righteous", "mysterious", "infinite", "salient",
                        "magnificent", "activated", "sharing", "feeling",
                        "powerful", "clear", "energized", "rainbow", "perfect",
                        "truly united", "world", "local", "ripe", "loving",
                        "anticipating", "pleasant", "personalized",
                        "transient", "individualized", "truly-unique",
                        "ancient", "loving", "experienced", "creative",
                        "foreign", "familiar", "worthy", "precise",
                        "intelligent", "gifted", "strained", "free-spirited",
                        "true", "clear", "caring", "dreamlike", "imaginative",
                        "collaborative", "service-oriented", "straightforward",
                        "strong", "orbiting", "glowing", "stable", "outer",
                        "nearest", "most-difficult", "transient",
                        "full", "round", "fluid", "opaque", "known",
                        "highly-valued", "smooth", "warm", "loose",
                        "ready", "burning", "effervescent", "impactful",
                        "parental", "childlike", "soft", "simple", "subtle",
                        "new", "abundant", "intergalactic", "questioning",
                        "resplendent", "terrific", "energetic", "powerful",
                        "discriminating", "self-actualized",  "ecological",
                        "planetary")
    oracle_instransient_verb_phrase = ("arrives", "beckons", "takes a rest",
                                       "becomes clear", "learns",
                                       "removes a block", "meditates",
                                       "remembers the soul",
                                       "jumps without a net",
                                       "remembers everything",
                                       "cleans the window of awareness",
                                       "feels truth", "returns", "rejoices",
                                       "prays", "takes action", "dreams",
                                       "ceases to exist", "hides", "chooses",
                                       "laughs with joy",
                                       "plays without questioning",
                                       "loves", "wakes up",
                                       "hesitates and moves anyway",
                                       "trembles with comprehension",
                                       "reflects", "is born",
                                       "finds inspiration",
                                       "feels completely full", "senses",
                                       "sees", "joins the path", "listens",
                                       "reasons", "sits", "flies", "sings",
                                       "knows")
    oracle_conjuction = ("and", "but", "for", "nor",
                         "or", "so", "yet", "becuase")
    oracle_complete_visions = ("There is a storm in your past and yet"
                               " another in your future, but persistence and "
                               "clear thinking will show you the road once "
                               "more",
                               "The answers you seek will be found within. "
                               "Seek the obvious to address the unknown",
                               "What one man has wrought, another can undo. "
                               "Although they differ, they are one "
                               "and the same",
                               "The path you walk is built on faith. Fear not "
                               "your choices, as they are the stepping stones"
                               " that bridge the chasm",
                               "One cannot be truly wrong if he is really"
                               " right. Believe in yourself, and you will"
                               " find the answers you seek",
                               "What you possess is all you need. Don’t be "
                               "swayed by the illusion of what’s needed",
                               "Although you fear your choices, they are all"
                               " you have. Fear the Choice you‘ve lost more "
                               "than the choices that you still possess",
                               "Don’t be blinded by the tree that blocks "
                               "your sight, skirt its trunk to see the forest",
                               "The one you seek will need you more. He is "
                               "hanging from the precipice of shattered"
                               " dreams, and has lost what cannot be found",
                               "Trust what you know, since it is also "
                               "the answer to what you do not")

    with open(f"{FILEPATH}/referencedata/Oracles.json",
              "w",
              encoding='utf-8-sig') as file:
        json.dump({"oracle_noun": oracle_noun,
                   "oracle_prepostion": oracle_preposition,
                   "oracle_adverb": oracle_adverb,
                   "oracle_adjective": oracle_adjective,
                   "oracle_instransient_verb_phrase": oracle_instransient_verb_phrase,
                   "oracle_conjuction": oracle_conjuction,
                   "oracle_complete_visions": oracle_complete_visions},
                  file,
                  indent=4,
                  ensure_ascii=False)


if __name__ == "__main__":
    main()
