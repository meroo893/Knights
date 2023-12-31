from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    And(
        Or(AKnight, AKnave),
        Not(And(AKnight, AKnave))   # knight Xor knave
    ),
    And(
        Or(BKnight, BKnave),
        Not(And(BKnight, BKnave))   # knight Xor knave
    ),
    And(
        Or(CKnight, CKnave),
        Not(And(CKnight, CKnave))   # knight Xor knave
    ),
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnave, AKnight)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    And(
        Or(AKnight, AKnave),
        Not(And(AKnight, AKnave))   # knight Xor knave
    ),
    And(
        Or(BKnight, BKnave),
        Not(And(BKnight, BKnave))   # knight Xor knave
    ),
    Implication(AKnight, Or(And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnave, BKnave))))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    And(
        Or(AKnight, AKnave),
        Not(And(AKnight, AKnave))  # Aknight Xor Aknave
    ),
    And(
        Or(BKnight, BKnave),
        Not(And(BKnight, BKnave))  # Bknight Xor Bknave
    ),
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),

    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(And(Or(AKnight, BKnave), Or(AKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    And(
        Or(AKnight, AKnave),
        Not(And(AKnight, AKnave))  # knight Xor knave
    ),
    And(
        Or(BKnight, BKnave),
        Not(And(BKnight, BKnave))  # knight Xor knave
    ),
    And(
        Or(CKnight, CKnave),
        Not(And(CKnight, CKnave))  # knight Xor knave
    ),
    # If B is a knight A says "I am a knave" and C is a knave
    Implication(BKnight, CKnave),
    Implication(BKnight, And(
        # A then says "I am a knave"; A may be a knight or a knave
        Implication(AKnight, AKnave),
        Implication(AKnave, Not(AKnave))
    )),
    # If B is a knave A says "I am a knight" and C is not a knave
    Implication(BKnave, CKnight),
    Implication(BKnave, And(
        # A then says "I am a knight"
        Implication(AKnight, AKnight),
        Implication(AKnave, Not(AKnight))
    )),
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
