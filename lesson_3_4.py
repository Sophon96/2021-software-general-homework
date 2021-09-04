################################################
# Instead of printing out the dictionary when the program is done, ask the user 
# for a sentence and “translate” it, word-by-word, as output. 

# If a word has no translation, use the word unchanged.

if __name__ == '__main__':
    import pickle
    import os

    translations = {}

    if os.path.exists("dict.pickle"):
        try:
            with open('dict.pickle', 'rb') as fin:
                translations = pickle.load(fin)
        except PermissionError:
            print('Unable to open dict.pickle -- Skipping.')

    if translations:
        print(f'Found existing translations: {translations}')

    while (action1 := input("What would you like to do? ")) != "quit":
        if action1 == "help":
            print("Available Actions:\nhelp\nnew\nmod\ndel\nquit")
        elif action1 == "new":
            while (orig := input("Enter a word, or press enter to end: ")) != "":
                if orig in translations:
                    print("A translation already exists for that word!")
                    continue
                if ' ' in orig:
                    print("Words must not contain spaces!")
                    continue

                trans = input("Enter the word's translation: ")
                translations[orig] = trans
        elif action1 == "mod":
            if not translations:
                print("No translations exist yet! Use the 'new' action to create translations!")
                continue

            print(f"Words: {', '.join(translations.keys())}")
            while (orig := input("Enter a word, or press enter to end: ")) != "":
                if orig not in translations:
                    print("That word has not been translated yet!")
                    continue

                trans = input("Enter the word's new translation: ")
                translations[orig] = trans
        elif action1 == "del":
            if not translations:
                print("No translations exist yet!")
                continue

            print(f"Words: {', '.join(translations.keys())}")
            while (orig := input("Enter a word, or press enter to end: ")) != "" and translations:
                if orig not in translations:
                    print("Word does not exist!")
                    continue

                translations.pop(orig)

    print(f"Translations: {translations}")
    store = input("Store translations? (y/n): ")
    if store == 'y':
        try:
            with open("dict.pickle", "wb+") as fout:
                pickle.dump(translations, fout)
        except PermissionError:
            print("Insufficient permissions to store translations!")

    sentence = input("Enter a sentence to translate: ").split()
    changed = []
    for i in sentence:
        if i in translations:
            changed.append(translations[i])
        else:
            changed.append(i)
    print(f'Translation: {" ".join(changed)}')
