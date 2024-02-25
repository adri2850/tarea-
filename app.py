from rdkit import Chem
from rdkit.Chem.Draw import MolsToGridImage
#molécula random
molecula = Chem.MolFromSmiles('O=C1CN(C(OC(C)(C)C)=O)[C@](C=C1)([H])CC2=CN(S(=O)(C3=CC=C(C)C=C3)=O)C4=CC=CC=C42')
molecula
