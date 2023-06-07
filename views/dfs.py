from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

def dfsComponent(container,graphe,source:str|None)->tuple:
    """
    Calcule le parcours en profondeur d'un graphe et affiche le résultat dans une fenêtre.

    Args:
        
        container: le conteneur où afficher la fenêtre.
        
        graphe: le graphe à parcourir.
        
        source: le sommet de départ du parcours. Si None, le parcours commencera au premier sommet du graphe.

    Returns:
        
        Un tuple contenant les widgets créés :
            
            frame_dfs : la fenêtre contenant l'affichage du parcours en profondeur.
            
            input_source_dfs : un champ d'entrée permettant de saisir le sommet de départ du parcours.
            
            btn_dfs : le bouton permettant de lancer le parcours en profondeur.
            
            note_dfs : une étiquette affichant des informations sur le parcours en profondeur.
            
            dfs_repre : l'affichage graphique du parcours en profondeur.

    Exemple:
        Pour lancer le parcours en profondeur avec le sommet "A" comme point de départ et afficher le résultat dans
        une fenêtre, il suffit de faire :

        >>> dfsComponent(container, graphe, "A")
    """
    frame_dfs=container.newFram(200,300,600,300,'','background-color:None;font-size:7px;')
    dfs_repre=frame_dfs.newFrameGraphe(0,30,300,270,graphe.getNetworkxGraph(),"graphe",None)
    frame_dfs.newLabel(310,50,290,30,'font-size:13px;color:black;','<b>Le parcours en profondeur</b> est une méthode ',False)
    frame_dfs.newLabel(310,70,290,30,'font-size:13px;color:black;','de parcours des graphes qui explore le plus',False)
    frame_dfs.newLabel(310,90,290,30,'font-size:13px;color:black;','profondément possible chaque branche avant',False)
    frame_dfs.newLabel(310,110,290,30,'font-size:13px;color:black;','de revenir en arrière et d\'explorer les autres',False)
    frame_dfs.newLabel(310,130,290,30,'font-size:13px;color:black;','branches.',False)
    url = "https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur"
    frame_url=frame_dfs.newLabel(370,130,290,30,'font-size:13px;color:black;',f"<a href={url}>wikipedia</a>",False)
    frame_url.setOpenExternalLinks(True)
    def open_link():
        QDesktopServices.openUrl(QUrl(url))
    frame_url.linkActivated.connect(open_link)
    graphe_info_label=frame_dfs.newLabel(0,0,600,30,'font-size:15px;color:blue;','Parcours en profondeur(DFS)',True)
    btn_dfs=frame_dfs.newButton(390,200,100,20,'background-color:white;color:black;font-size:15px;','background-color:black;color:white','DFS',None,None)
    if source != None :
       dfs_repre=frame_dfs.newFrameGraphe(0,30,300,270,graphe.getDfsGraphe(source),"dfs",None)
    label_input_source=frame_dfs.newLabel(310,150,130,50,'font-size:15px;','Sommet de depart',False)
    input_source_dfs=frame_dfs.newInput(440,165,130,20,'font-size:15px;','',True,None)
    note_dfs=frame_dfs.newLabel(305,230,275,30,'color:white;font-size:12px;','',True)
    return frame_dfs,input_source_dfs,btn_dfs,note_dfs,dfs_repre