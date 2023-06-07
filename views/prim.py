from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl


def primComponent(container,graphe,source:str|None)->tuple:
    """
    Crée une fenêtre Qt contenant une représentation graphique d'un graphe
    ainsi qu'un algorithme de recherche d'arbre couvrant minimal de Prim.

    Args:
        
        container (QtWidgets.QWidget): Le conteneur parent de la fenêtre.
        
        graphe (Graph): Le graphe à afficher.
        
        source (str|None): Le sommet de départ pour l'algorithme de Prim.
                            Si None, le sommet est choisi aléatoirement.

    Returns:
        tuple: Un tuple contenant plusieurs éléments :
                
                frame_prim : la fenêtre principale de l'application
                
                input_source_prim : l'objet QLineEdit pour entrer le sommet de départ
                
                btn_prim : le bouton pour lancer l'algorithme de Prim
                
                note_prim : le label pour afficher des informations à l'utilisateur
                
                prim_repre : la représentation graphique du graphe et de l'arbre couvrant minimal de Prim
    """
    frame_prim=container.newFram(200,300,600,300,'','background-color:None;font-size:7px;')
    prim_repre=frame_prim.newFrameGraphe(0,30,300,270,graphe.getNetworkxGraph(),"graphe",None)
    frame_prim.newLabel(310,50,290,30,'font-size:13px;color:black;','L\'algorithme de <b>Prim</b> est un algorithme glouton',False)
    frame_prim.newLabel(310,70,290,30,'font-size:13px;color:black;','qui calcule <u>un arbre couvrant minimal dans </u>',False)
    frame_prim.newLabel(310,90,290,30,'font-size:13px;color:black;','un graphe <i>connexe pondéré et non orienté</i>',False)
    url = "https://fr.wikipedia.org/wiki/Algorithme_de_Prim"
    frame_url=frame_prim.newLabel(310,110,290,30,'font-size:13px;color:black;',f"<a href={url}>wikipedia</a>",False)
    frame_url.setOpenExternalLinks(True)
    def open_link():
        QDesktopServices.openUrl(QUrl(url))
    frame_url.linkActivated.connect(open_link)
    graphe_info_label=frame_prim.newLabel(0,0,600,30,'font-size:15px;color:blue;','Algorithme de Prim',True)
    btn_prim=frame_prim.newButton(390,200,100,20,'background-color:white;color:black;font-size:15px;','background-color:black;color:white','Prim',None,None)
    if source != None :
       prim_repre=frame_prim.newFrameGraphe(0,30,300,270,graphe.getPrimGraphe(source),"prim",None)
    label_input_source=frame_prim.newLabel(310,150,130,50,'font-size:15px;','Sommet de depart',False)
    input_source_prim=frame_prim.newInput(440,165,130,20,'font-size:15px;','',True,None)
    note_prim=frame_prim.newLabel(305,230,275,30,'color:white;font-size:12px;','',True)
    return frame_prim,input_source_prim,btn_prim,note_prim,prim_repre