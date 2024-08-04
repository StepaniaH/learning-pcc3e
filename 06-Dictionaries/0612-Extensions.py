# The extensions of 0603-Glossary.py
glossary = {
    "python": ["high-level", "interpreted", "programming", "language"],
    "list": ["data", "structure", "collection", "items"],
    "dictionary": ["data", "structure", "mapping", "keys", "values"],
    "if": ["conditional", "statement", "execute", "block", "certain", "condition", "true"],
    "else": ["conditional", "statement", "execute", "block", "certain", "condition", "false"],
    "for": ["loop", "execute", "block", "collection"],
    "while": ["loop", "execute", "block", "certain", "condition", "true"],
    "break": ["statement", "exit", "loop"],
    "continue": ["statement", "skip", "rest", "iteration", "loop", "move", "next", "iteration"],
    "pass": ["statement", "nothing"]
}

for k, v in glossary.items():
    print(f"{k}: {', '.join(v)}\n")
