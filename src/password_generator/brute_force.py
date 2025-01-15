# src/password_generator/brute_force.py

def brute_force_options():
    """Menu pour choisir les options d'attaque par force brute."""
    print("Options d'attaque par force brute :")
    print("1. Utiliser John the Ripper")
    print("2. Utiliser Hashcat")
    print("3. Retour au menu principal")
    
    choice = input("Entrez votre choix : ")
    if choice == '1':
        print("Commandes pour John the Ripper :")
        print("john --wordlist=path/to/dictionary.txt --format=hash_type hash_file")
    elif choice == '2':
        print("Commandes pour Hashcat :")
        print("hashcat -m hash_type -a 0 hash_file path/to/dictionary.txt")
    elif choice == '3':
        return
    else:
        print("Choix invalide.")
