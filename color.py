# !\usr\bin\env python
# -*- coding: UTF-8 -*-

#importer des modules
import sys, re

##############################
# Mettre un terme dans une   #
# tranche en couleur         #
# -------------------------  #
# Créé : le 28/05/2015       #
# Auteur : Freshloic         #
# Tuteur : Mr BYRAM Miguel   #
##############################

"""
procédure à lancer
début: recherche term2find au sein de file2lookinto
fin: affiche term2find dans les tranches en couleur
"""
COLOR_GREP="\033[1;33m"
# END_COLOR="\033[1;m"
END_COLOR="\033[m"

def color(term2find, tranche):
    
    mot = r"^(.*)("+term2find+")(.*)$"
    ismot = re.search(mot,str(tranche))

    if ismot:
        print ismot.group(1) + COLOR_GREP + term2find + END_COLOR + ismot.group(3)
      
    
if __name__ == "__main__":
    try:
        term2find = sys.argv[1]
    except:
        print "Indiquez le terme à rechercher"
        sys.exit(2)
    try:
        tranche =sys.argv[2]
    except:
        print "Indiquez la phrase ou la tranche où sera recherché le terme"
        sys.exit(2)
    color(term2find, tranche)
