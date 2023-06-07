from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

def dijkstraComponent(container,graphe,source:str|None,pointFinal:str|None)->tuple:
    """
    Affiche une fenêtre avec une représentation graphique du graphe, permettant l'exécution de l'algorithme de Dijkstra.
    
    Args:
        
        container: le conteneur parent où la fenêtre doit être affichée.
        
        graphe: le graphe à représenter.
        
        source: le sommet de départ pour l'algorithme de Dijkstra.
        
        pointFinal: le sommet d'arrivée pour l'algorithme de Dijkstra.
    
    Returns:
    
        Un tuple contenant :
        
            frame_dijkstra : le cadre contenant l'interface graphique de l'algorithme de Dijkstra.
            
            input_source_dijkstra : le champ d'entrée pour le sommet de départ.
            
            input_pointFinal_dijkstra : le champ d'entrée pour le sommet d'arrivée.
            
            btn_dijkstra : le bouton pour lancer l'algorithme de Dijkstra.
            
            note_dijkstra : le champ pour afficher des notes ou des messages d'erreur.
            
            dijkstra_repre : la représentation graphique du résultat de l'algorithme de Dijkstra, si les sommets de départ et d'arrivée sont spécifiés.
    """
    frame_dijkstra=container.newFram(200,300,600,300,'','background-color:None;font-size:7px;')
    dijkstra_repre=frame_dijkstra.newFrameGraphe(0,30,300,270,graphe.getNetworkxGraph(),"graphe",None)
    frame_dijkstra.newLabel(310,50,290,30,'font-size:13px;color:black;','L\'algorithme de <b>Dijkstra</b> est un algorithme',False)
    frame_dijkstra.newLabel(310,70,290,30,'font-size:13px;color:black;','de recherche de chemin le plus court dans',False)
    frame_dijkstra.newLabel(310,90,290,30,'font-size:13px;color:black;','un graphe <u>pondéré</u>. Il utilise une approche',False)
    frame_dijkstra.newLabel(310,110,290,30,'font-size:13px;color:black;','gloutonne pour trouver le chemin optimal.',False)
    url = "https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra"
    frame_url=frame_dijkstra.newLabel(310,130,290,30,'font-size:13px;color:black;',f"<a href={url}>wikipedia</a>",False)
    frame_url.setOpenExternalLinks(True)
    def open_link():
        QDesktopServices.openUrl(QUrl(url))
    frame_url.linkActivated.connect(open_link)
    graphe_info_label=frame_dijkstra.newLabel(0,0,600,30,'font-size:15px;color:blue;','L\'algorithme de Dijkstra',True)
    btn_dijkstra=frame_dijkstra.newButton(390,230,100,20,'background-color:white;color:black;font-size:15px;','background-color:black;color:white','Dijkstra',None,None)
    if source != None and pointFinal!=None:
       dijkstra_repre=frame_dijkstra.newFrameGraphe(0,30,300,270,graphe.getNetworkxGraph(),"dijkstra",graphe.getListeDijkstra(source,pointFinal))
    frame_dijkstra.newLabel(310,150,130,50,'font-size:15px;','Sommet de depart',False)
    input_source_dijkstra=frame_dijkstra.newInput(440,165,130,20,'font-size:15px;','',True,None)
    frame_dijkstra.newLabel(310,175,130,50,'font-size:15px;','Sommet d\'arrive',False)
    input_pointFinal_dijkstra=frame_dijkstra.newInput(440,193,130,20,'font-size:15px;','',True,None)
    note_dijkstra=frame_dijkstra.newLabel(305,260,275,30,'color:white;font-size:12px;','',True)

    return frame_dijkstra,input_source_dijkstra,input_pointFinal_dijkstra,btn_dijkstra,note_dijkstra,dijkstra_repre