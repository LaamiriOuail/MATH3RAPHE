from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

def bfsComponent(container,graphe,source:str|None)->tuple:
    """
    Crée un composant d'affichage d'un parcours en largeur d'un graphe.

    Args:
        
        container (Container): Le conteneur parent du composant.
        
        graphe (Graphe): Le graphe à parcourir.
        
        source (str, optional): Le sommet de départ du parcours. Si aucun sommet n'est donné, le parcours commencera par un sommet au hasard. Par défaut None.

    Returns:
        tuple: 
           
            Un tuple contenant les différents éléments du composant :
                
                frame_bfs (Frame) : Le cadre contenant le composant.
                
                input_source_bfs (Input) : Le champ de saisie du sommet de départ.
                
                btn_bfs (Button) : Le bouton pour lancer le parcours.
                
                note_bfs (Label) : L'étiquette affichant les informations sur le parcours.
                
                bfs_repre (FrameGraphe) : Le cadre d'affichage du graphe parcouru.

    """
    frame_bfs=container.newFram(200,300,600,300,'','background-color:None;font-size:7px;')
    bfs_repre=frame_bfs.newFrameGraphe(0,30,300,270,graphe.getNetworkxGraph(),"graphe",None)
    frame_bfs.newLabel(310,50,290,30,'font-size:13px;color:black;','<b>Le parcours en largeur</b> est un algorithme',False)
    frame_bfs.newLabel(310,70,290,30,'font-size:13px;color:black;','de parcours de graphe qui explore d\'abord',False)
    frame_bfs.newLabel(310,90,290,30,'font-size:13px;color:black;','les voisins d\'un nœud avant de passer',False)
    frame_bfs.newLabel(310,110,290,30,'font-size:13px;color:black;','aux nœuds suivants, parcourant le graphe',False)
    frame_bfs.newLabel(310,130,290,30,'font-size:13px;color:black;','en largeur plutôt qu\'en profondeur.',False)
    url = "https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur"
    frame_url=frame_bfs.newLabel(520,130,290,30,'font-size:13px;color:black;',f"<a href={url}>wikipedia</a>",False)
    frame_url.setOpenExternalLinks(True)
    def open_link():
        QDesktopServices.openUrl(QUrl(url))
    frame_url.linkActivated.connect(open_link)
    graphe_info_label=frame_bfs.newLabel(0,0,600,30,'font-size:15px;color:blue;','Parcours en largeur(BFS)',True)
    btn_bfs=frame_bfs.newButton(390,200,100,20,'background-color:white;color:black;font-size:15px;','background-color:black;color:white','BFS',None,None)
    if source != None :
       bfs_repre=frame_bfs.newFrameGraphe(0,30,300,270,graphe.getBfsGraphe(source),"bfs",None)
    label_input_source=frame_bfs.newLabel(310,150,130,50,'font-size:15px;','Sommet de depart',False)
    input_source_bfs=frame_bfs.newInput(440,165,130,20,'font-size:15px;','',True,None)
    note_bfs=frame_bfs.newLabel(305,230,275,30,'color:white;font-size:12px;','',True)
    return frame_bfs,input_source_bfs,btn_bfs,note_bfs,bfs_repre