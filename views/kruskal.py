from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl


def kruskalComponent(container,graphe,source:str|None)->tuple:
    """
    Crée un composant pour l'algorithme de Kruskal.

    Args:
        
        container: Le conteneur pour le composant.
        
        graphe: Le graphe sur lequel l'algorithme sera appliqué.
        
        source (str, optionnel): Le sommet de départ pour le graphe kruskal.

    Returns:
        Un tuple contenant le cadre du composant, le champ de saisie pour le sommet de départ, le bouton pour lancer l'algorithme, une note pour les résultats et le cadre du graphe.
    """
    frame_kruskal=container.newFram(200,300,600,300,'','background-color:None;font-size:7px;')
    kruskal_repre=frame_kruskal.newFrameGraphe(0,30,300,270,graphe.getNetworkxGraph(),"graphe",None)
    frame_kruskal.newLabel(310,50,290,30,'font-size:13px;color:black;','L\'algorithme de <b>Kruskal<b> est un algorithme ',False)
    frame_kruskal.newLabel(310,70,290,30,'font-size:13px;color:black;','de recherche d\'arbre recouvrant de poids minimum ',False)
    frame_kruskal.newLabel(310,90,290,30,'font-size:13px;color:black;','<b>(ARPM)</b> dans un graphe <u>connexe non-orienté</u>',False)
    frame_kruskal.newLabel(310,110,290,30,'font-size:13px;color:black;','<u>et pondéré</u>.Il a été conçu en 1956 par ',False)
    frame_kruskal.newLabel(310,130,290,30,'font-size:13px;color:black;','<b>Joseph Kruskal</b>.',False)
    url = "https://fr.wikipedia.org/wiki/Algorithme_de_Kruskal"
    frame_url=frame_kruskal.newLabel(420,130,290,30,'font-size:13px;color:black;',f"<a href={url}>wikipedia</a>",False)
    frame_url.setOpenExternalLinks(True)
    def open_link():
        QDesktopServices.openUrl(QUrl(url))
    frame_url.linkActivated.connect(open_link)
    graphe_info_label=frame_kruskal.newLabel(0,0,600,30,'font-size:15px;color:blue;','Algorithme de Kruskal',True)
    btn_kruskal=frame_kruskal.newButton(390,200,100,20,'background-color:white;color:black;font-size:15px;','background-color:black;color:white','kruskal',None,None)
    if source != None :
       kruskal_repre=frame_kruskal.newFrameGraphe(0,30,300,270,graphe.getkruskalGraphe(source),"Kruskal",None)
    label_input_source=frame_kruskal.newLabel(310,150,130,50,'font-size:15px;','Sommet de depart',False)
    input_source_kruskal=frame_kruskal.newInput(440,165,130,20,'font-size:15px;','',True,None)
    note_kruskal=frame_kruskal.newLabel(305,230,275,30,'color:white;font-size:12px;','',True)
    return frame_kruskal,input_source_kruskal,btn_kruskal,note_kruskal,kruskal_repre