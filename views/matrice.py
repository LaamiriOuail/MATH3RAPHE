from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QApplication


def matrixComponent(container)->tuple:
    """
    Crée une fenêtre contenant deux matrices : une matrice d'adjacence et une matrice d'incidence.

    Args:
        container: un objet container (par exemple un objet Window) dans lequel créer la fenêtre

    Returns:
        Un tuple contenant trois éléments : le cadre principal de la fenêtre, la table pour la matrice d'incidence, et la table pour la matrice d'adjacence.
    """
    frame_matrix=container.newFram(200,300,600,300,'','background-color:None;font-size:7px;')
    frame_matrix_adjacent=frame_matrix.newFram(0,0,300,300,'','border:1px solid blue;border-left:none;border-top:none;border-bottom:none;')
    frame_matrix_adjacent.newLabel(0,0,300,30,'font-size:13px;color:blue;border:none',"Matrice d'adjacence",True)
    frame_matrix_adjacent.newLabel(0,20,290,30,'font-size:13px;color:black;border:none',"une matrice <b>d'adjacence</b> pour un graphe fini à n",False)
    frame_matrix_adjacent.newLabel(0,40,290,30,'font-size:13px;color:black;border:none','sommets est une matrice de dimension n x n ',False)
    frame_matrix_adjacent.newLabel(0,60,290,30,'font-size:13px;color:black;border:none',"dont l'élément non diagonal a<sub>ij</sub> est le nombre",False)
    frame_matrix_adjacent.newLabel(0,80,290,30,'font-size:13px;color:black;border:none',"d'arêtes liant le sommet i au sommet j",False)
    url_adj = "https://fr.wikipedia.org/wiki/Matrice_d%27adjacence"
    frame_url_adj=frame_matrix_adjacent.newLabel(232,80,290,30,'font-size:13px;color:black;border:none',f"<a href={url_adj}>wikipedia</a>",False)
    frame_url_adj.setOpenExternalLinks(True)
    def open_link_adj()->None:
        QDesktopServices.openUrl(QUrl(url_adj))
    frame_url_adj.linkActivated.connect(open_link_adj)
    table_matrix_adj = QTableWidget(frame_matrix_adjacent)
    table_matrix_adj.setStyleSheet("border : 1px solid black;font-size:15px;")
    table_matrix_adj.setGeometry(10,110,280,180)
    ####################################################
    frame_matrix_incident=frame_matrix.newFram(300,0,300,300,'','')
    frame_matrix_incident.newLabel(0,0,300,30,'font-size:13px;color:blue;',"Matrice d'incidence",True)
    frame_matrix_incident.newLabel(10,20,290,30,'font-size:13px;color:black;',"La matrice <b>d'incidence</b> d'un graphe est une matrice",False)
    frame_matrix_incident.newLabel(10,40,290,30,'font-size:13px;color:black;','qui décrit le graphe en indiquant quels liens ',False)
    frame_matrix_incident.newLabel(10,60,290,30,'font-size:13px;color:black;',"arrivent sur quels sommets.",False)
    url_inc = "https://fr.wikipedia.org/wiki/Matrice_d%27incidence"
    frame_url_inc=frame_matrix_incident.newLabel(180,60,290,30,'font-size:13px;color:black;',f"<a href={url_inc}>wikipedia</a>",False)
    frame_url_inc.setOpenExternalLinks(True)
    def open_link_inc()->None:
        QDesktopServices.openUrl(QUrl(url_inc))
    frame_url_inc.linkActivated.connect(open_link_inc)
    table_matrix_inc = QTableWidget(frame_matrix_incident)
    table_matrix_inc.setGeometry(10,110,280,180)
    table_matrix_inc.setStyleSheet("border : 1px solid black;font-size:15px;")
    return frame_matrix,table_matrix_inc,table_matrix_adj