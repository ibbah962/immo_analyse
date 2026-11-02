import pandas as pd

def charger_csv(chemin, separateur, encodage):
    """Lit un fichier CSV et retourne un DataFrame.
    
    chemin : chemin du fichier (str)
    sep : separateur de colonnes ("," ou ";")
    encoding : encodage du fichier ("utf-8", "latin-1", ...)
    """
    return pd.read_csv(chemin, sep=separateur, encoding=encodage)