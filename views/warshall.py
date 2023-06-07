from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

def warshallComponent(container,graphe)->tuple:
    """

    """
    frame_warshall=container.newFram(200,300,600,300,'','background-color:None;font-size:7px;')
    warshall_repre=frame_warshall.newFrameGraphe(0,30,400,270,graphe.getNetworkxGraph(),"warshall",None)
    frame_warshall.newLabel(410,50,290,30,'font-size:13px;color:black;','<b>L\'algorithme de Warshall</b> est un',False)
    frame_warshall.newLabel(410,70,290,30,'font-size:13px;color:black;','algorithme pour calculer la',False)
    frame_warshall.newLabel(410,90,290,30,'font-size:13px;color:black;','fermeture transitive d\'un',False)
    frame_warshall.newLabel(410,110,290,30,'font-size:13px;color:black;','graphe orienté',False)
    url = "https://fr.wikipedia.org/wiki/Algorithme_de_Warshall"
    frame_url=frame_warshall.newLabel(500,110,290,30,'font-size:13px;color:black;',f"<a href={url}>wikipedia</a>",False)
    frame_url.setOpenExternalLinks(True)
    def open_link():
        QDesktopServices.openUrl(QUrl(url))
    frame_url.linkActivated.connect(open_link)
    graphe_info_label=frame_warshall.newLabel(0,0,600,30,'font-size:15px;color:blue;','L\'algorithme de Warshall',True)
    btn_warshall=frame_warshall.newButton(450,140,100,20,'background-color:white;color:black;font-size:15px;','background-color:black;color:white','warshall',None,None)
    note_warshall=frame_warshall.newLabel(405,170,190,30,'color:white;font-size:12px;background-color:green;','',True)
    return frame_warshall,btn_warshall,note_warshall,warshall_repre
