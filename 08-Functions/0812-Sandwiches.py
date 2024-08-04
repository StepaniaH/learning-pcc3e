def sandwich(*items):
    print("\nThis sandwich has the following items:")
    for item in items:
        print(f"- {item}")


sandwich("ham", "cheese", "tomato")
sandwich("ham", "cheese", "tomato", "lettuce")
sandwich("ham", "cheese", "tomato", "lettuce", "mayo")
