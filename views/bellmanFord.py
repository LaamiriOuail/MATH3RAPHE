from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

def bellmanFordComponent(container,graphe,source:str|None,pointFinal:str|None)->tuple:
    frame_bellman_ford=container.newFram(200,300,600,300,'','background-color:None;font-size:7px;')
    bellman_ford_repre=frame_bellman_ford.newFrameGraphe(0,30,300,270,graphe.getNetworkxGraph(),"graphe",None)
    frame_bellman_ford.newLabel(310,50,290,30,'font-size:13px;color:black;',"L'algorithme <b>de Bellman-Ford</b>,est un",False)
    frame_bellman_ford.newLabel(310,70,290,30,'font-size:13px;color:black;',"algorithme qui calcule des plus courts chemins",False)
    frame_bellman_ford.newLabel(310,90,290,30,'font-size:13px;color:black;','depuis un sommet source donné dans un graphe',False)
    frame_bellman_ford.newLabel(310,110,290,30,'font-size:13px;color:black;','<i><u>orienté pondéré</u></i>',False)
    url = "https://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford"
    frame_url=frame_bellman_ford.newLabel(420,110,290,30,'font-size:13px;color:black;',f"<a href={url}>wikipedia</a>",False)
    frame_url.setOpenExternalLinks(True)
    def open_link():
        QDesktopServices.openUrl(QUrl(url))
    frame_url.linkActivated.connect(open_link)
    graphe_info_label=frame_bellman_ford.newLabel(0,0,600,30,'font-size:15px;color:blue;','L\'algorithme de Bellman-Ford',True)
    btn_bellman_ford=frame_bellman_ford.newButton(390,230,100,20,'background-color:white;color:black;font-size:15px;','background-color:black;color:white','Bellman-Ford',None,None)
    if source != None and pointFinal!=None:
       bellman_ford_repre=frame_bellman_ford.newFrameGraphe(0,30,300,270,graphe.getNetworkxGraph(),"bellman_ford",graphe.getListeBellmanFord(source,pointFinal))
    frame_bellman_ford.newLabel(310,150,130,50,'font-size:15px;','Sommet de depart',False)
    input_source_bellman_ford=frame_bellman_ford.newInput(440,165,130,20,'font-size:15px;','',True,None)
    frame_bellman_ford.newLabel(310,175,130,50,'font-size:15px;','Sommet d\'arrive',False)
    input_pointFinal_bellman_ford=frame_bellman_ford.newInput(440,193,130,20,'font-size:15px;','',True,None)
    note_bellman_ford=frame_bellman_ford.newLabel(305,260,275,30,'color:white;font-size:12px;','',True)

    return frame_bellman_ford,input_source_bellman_ford,input_pointFinal_bellman_ford,btn_bellman_ford,note_bellman_ford,bellman_ford_repre