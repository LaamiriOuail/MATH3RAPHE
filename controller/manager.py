import os
import sys
parent_dir = os.path.abspath(os.path.join(os.getcwd(), '.'))
sys.path.append(parent_dir)
from package.UI import Window
from package.Graphe import Graph
#SQL
from package.DBGSQL import DBG
#NoSQL
# from package.DBGNoSQL import DBG
from package.PDF import generate_pdf
from PyQt5.QtWidgets import QApplication ,QTableWidgetItem , QFrame ,QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from functools import partial
from views.edgeManipulation import EdgeComponent
from views.grapheInfor import infoComponent
from views.bareChoix import bareChoix
from views.bfs import bfsComponent
from views.dfs import dfsComponent
from views.dijkstra import dijkstraComponent
from views.prim import primComponent
from views.kruskal import kruskalComponent
from views.tableauDB import tableauBaseDonner
from views.matrice import matrixComponent
from views.warshall import warshallComponent
from views.generatePdf import pdfComponent
from views.grapheRepresentation import grapheRepresentationComponent
from views.bellmanFord import bellmanFordComponent
import pygame
import datetime



theorie_graphe_app=QApplication(sys.argv)
graphe=Graph(False,False)
############################################
icon_app='.\\public\\icon\\app.png'

generale_container=Window(800,600,"MATH3RAPHE",icon_app,'','background-color:white;',True,0.903)

############################################
frame_graphe_manipulation,frame_add_del_edge,type_graphe,input_sommet_depart,input_sommet_arriver,poids_arrete,input_poids_arrete,ajouter_arrete,supprimer_arrete,initialiser_graphe,enregistrer_graphe,note_ajouter_edge=EdgeComponent(generale_container)
frame_info,is_directed,is_weighted,number_of_nodes,liste_nodes,number_of_edges,liste_edges,density,degre_nodes,is_eulerian,is_planaire,is_connexe=infoComponent(generale_container)
frame_bfs,input_source_bfs,btn_bfs,note_bfs,bfs_repre=bfsComponent(generale_container,graphe,None)
frame_dfs,input_source_dfs,btn_dfs,note_dfs,dfs_repre=dfsComponent(generale_container,graphe,None)
frame_dijkstra,input_source_dijkstra,input_pointFinal_dijkstra,btn_dijkstra,note_dijkstra,dijkstra_repre=dijkstraComponent(generale_container,graphe,None,None)
frame_prim,input_source_prim,btn_prim,note_prim,prim_repre=primComponent(generale_container,graphe,None)
frame_kruskal,input_source_kruskal,btn_kruskal,note_kruskal,kruskal_repre=kruskalComponent(generale_container,graphe,None)
frame_tableau_bd,input_id,btn_recherche,btn_delete,btn_utiliser,table_historique_graphe,note_table_db=tableauBaseDonner(generale_container)
btn_home_bare,btn_historique_bare,btn_info_graphe_bare,btn_bfs_bare,btn_dfs_bare,btn_dijkstra_bare,btn_prim_bare,btn_kruskal_bare,btn_matrix_bare,btn_warshall_bare,btn_graphe_manipulation_bare,btn_genere_pdf_bare,btn_bellman_ford_bare=bareChoix(generale_container)
frame_matrix,table_matrix_inc,table_matrix_adj = matrixComponent(generale_container)
frame_warshall,btn_warshall,note_warshall,warshall_repre=warshallComponent(generale_container,graphe)
frame_graphe_rep,frame_graphe_rep_nx=grapheRepresentationComponent(generale_container,graphe)
frame_pdf,input_pointFinal_dijkstra_pdf,input_source_bfs_pdf,input_source_dfs_pdf,input_source_dijkstra_pdf,input_source_prim_pdf,btn_pdf,note_pdf,btn_choisir_dossier_pdf,title_pdf,nom_complete_pdf=pdfComponent(generale_container)
frame_bellman_ford,input_source_bellman_ford,input_pointFinal_bellman_ford,btn_bellman_ford,note_bellman_ford,bellman_ford_repre=bellmanFordComponent(generale_container,graphe,None,None)
############################################

def btn_genere_pdf_bare_event():
    """
    Affiche le cadre du PDF et configure les options en fonction des caractéristiques du graphe.

    Si le graphe n'est pas orienté, connexe et pondéré, certaines options seront désactivées.

    Si le graphe est pondéré, les options pour l'algorithme de Prim et Dijkstra seront activées.

    return: 
    
    Aucune valeur de retour.
    """
    show_frame_sound(frame_pdf)
    if graphe.isDirected()==False and graphe.isConnexe() and graphe.isPondere():
        input_source_prim_pdf.setEnabled(True)
    else:
        input_source_prim_pdf.setEnabled(False)
    if graphe.isPondere():
        input_source_dijkstra_pdf.setEnabled(True)
        input_pointFinal_dijkstra_pdf.setEnabled(True)
    else:
        input_source_dijkstra_pdf.setEnabled(False)
        input_pointFinal_dijkstra_pdf.setEnabled(False)
        
def btn_pdf_event():
    """
    Fonction gérant l'événement du bouton PDF.

        Cette fonction effectue les actions suivantes :
        Appelle la fonction audio_btn().
        
        Vérifie si le graphe est vide.
        
        Vérifie si un dossier a été choisi.
        
        Affiche le graphe initial.
        
        Affiche le graphe BFS si le sommet source est valide.
        
        Affiche le graphe DFS si le sommet source est valide.
        
        Affiche le graphe de Prim si le graphe est non orienté, connexe et pondéré et le sommet source est valide.
        
        Affiche le graphe de Warshall si le graphe est orienté.
        
        Affiche le graphe de Bellman-Ford si le graphe est pondéré et les sommets source et destination sont valides.
        
        Génère le PDF avec les informations fournies.
        
        Réinitialise les champs de saisie des sommets pour Bellman-Ford.

    Returns:
    None
    """
    audio_btn()
    cond=True
    if graphe.isVide():
        note_pdf.setStyleSheet("background-color: red ; color : white;font-size:15px;")
        note_pdf.setText("Graphe vide !!!")
        cond=False
    elif btn_choisir_dossier_pdf.text()=="" or btn_choisir_dossier_pdf.text()=="Choisir un dossier":
        note_pdf.setStyleSheet("background-color: red ; color : white;font-size:15px;")
        note_pdf.setText("Choisir un dossier !!!")
        cond=False
    elif title_pdf.text()=="":
        note_pdf.setStyleSheet("background-color: red ; color : white;font-size:15px;")
        note_pdf.setText("title vide !!!")
        cond=False
    elif nom_complete_pdf.text()=="":
        note_pdf.setStyleSheet("background-color: red ; color : white;font-size:15px;")
        note_pdf.setText("nom vide !!!")
        cond=False
    else :
        frame_graphe_rep.newFrameGraphe(0,0,600,300,graphe.getNetworkxGraph(),"graphe",None)
        if input_source_bfs_pdf.text() in graphe.getListeSommet():
            frame_graphe_rep.newFrameGraphe(0,0,600,300,graphe.getBfsGraphe(input_source_bfs_pdf.text()),"bfs",None)
        else :
            note_pdf.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_pdf.setText(f"{input_source_bfs_pdf.text()} n'est pas un sommet de graphe")
            cond=False
        if input_source_dfs_pdf.text() in graphe.getListeSommet():
            frame_graphe_rep.newFrameGraphe(0,0,600,300,graphe.getDfsGraphe(input_source_dfs_pdf.text()),"dfs",None)
        else :
            note_pdf.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_pdf.setText(f"{input_source_dfs_pdf.text()} n'est pas un sommet de graphe")
            cond=False
        if graphe.isDirected()==False and graphe.isConnexe() and graphe.isPondere():
            if input_source_prim_pdf.text() in graphe.getListeSommet():
                frame_graphe_rep.newFrameGraphe(0,0,600,300,graphe.getPrimGraphe(input_source_prim_pdf.text()),"prim",None)
            else :
                note_pdf.setStyleSheet("background-color: red ; color : white;font-size:15px;")
                note_pdf.setText(f"{input_source_prim_pdf.text()} n'est pas un sommet de graphe")
                cond=False
        if graphe.isDirected():
                frame_graphe_rep.newFrameGraphe(0,0,600,300,graphe.getWarshallGraphe(),"warshall",None,graphe.getNetworkxGraph())
        if graphe.isPondere():
            if input_source_dijkstra_pdf.text() in graphe.getListeSommet():
                if input_pointFinal_dijkstra_pdf.text() in graphe.getListeSommet():
                    frame_graphe_rep.newFrameGraphe(0,0,600,300,graphe.getNetworkxGraph(),"bellman_ford",graphe.getListeBellmanFord(input_source_dijkstra_pdf.text(),input_pointFinal_dijkstra_pdf.text()))
                else :
                    note_pdf.setStyleSheet("background-color: red ; color : white;font-size:15px;")
                    note_pdf.setText(f"{input_pointFinal_dijkstra_pdf.text()} n'est pas un sommet de graphe")
                    cond=False
            else :
                note_pdf.setStyleSheet("background-color: red ; color : white;font-size:15px;")
                note_pdf.setText(f"{input_source_dijkstra_pdf.text()} n'est pas un sommet de graphe")
                cond=False
    if cond:
        generate_pdf(title_pdf.text(),nom_complete_pdf.text(),btn_choisir_dossier_pdf.text(),graphe,note_pdf)
        input_pointFinal_dijkstra_pdf.setText("")
        input_source_dijkstra_pdf.setText("")
        input_source_prim_pdf.setText("")
        input_source_dfs_pdf.setText("")
        input_source_bfs_pdf.setText("")
btn_pdf.clicked.connect(btn_pdf_event)
############################################
def graphe_rep():
    """Affiche le graphe représenté par le réseau networkx dans une fenêtre graphique."""
    frame_graphe_rep.close()
    frame_graphe_rep_nx=frame_graphe_rep.newFrameGraphe(0,0,600,300,graphe.getNetworkxGraph(),"graphe",None)
    frame_graphe_rep.show()
def viderInputChamps():
    """Vide les champs de saisie."""
    input_poids_arrete.setText("")
    input_sommet_depart.setText("")
    input_sommet_arriver.setText("")
############################################
def showDialog():
    """Affiche une boîte de dialogue pour choisir un dossier."""
    options = QFileDialog.Options()
    options |= QFileDialog.ShowDirsOnly
    dossier = QFileDialog.getExistingDirectory(frame_pdf, "Choisir un dossier", options=options)
    dossier=dossier.replace('/', '\\')
    btn_choisir_dossier_pdf.setText(dossier)
    btn_choisir_dossier_pdf.clicked.connect(showDialog)
        
btn_choisir_dossier_pdf.clicked.connect(showDialog)
############################################
def audio_btn()->None:
    """
    Joue un fichier audio lorsqu'un bouton est pressé.

    Paramètres :
        Aucun

    Retour :
        Aucun
    """
    pygame.mixer.init()
    pygame.mixer.music.load(".\\public\\audio\\audioButton.mp3")
    pygame.mixer.music.play()
def dateTime()->list:
    """
    Renvoie la date et l'heure actuelles sous forme de liste.

    Paramètres :
        Aucun

    Retour :
        Une liste contenant la date au format 'AAAA-MM-JJ' en tant que première
        valeur, et l'heure au format 'HH:MM:SS' en tant que deuxième valeur.
    """
    return [str(datetime.date.today()),datetime.datetime.now().strftime('%H:%M:%S')]
##################################################################################
def enregistrer_graphe_event():
    """
    Enregistre le graphe dans la base de donnees.
    
    Returns:
        None
    """
    audio_btn()
    if graphe.isVide():
        note_ajouter_edge.setStyleSheet("background-color: red ; color : white;font-size:15px;")
        note_ajouter_edge.setText("Graphe vide !!!")
    else :
        db = DBG("graphe") 
        if graphe.isDirected():
            directed="Oui"
        else :
            directed="Non"
        if graphe.isPondere():
            pondere = "Oui"
        else :
            pondere = "Non"
        date_time=dateTime()
        db.insert(str(date_time[0]),str(date_time[1]),directed,pondere,str(graphe.getListeSommet())[1:-1],str(graphe.getListeArrete())[1:-1])
        note_ajouter_edge.setStyleSheet("background-color: green ; color : white;font-size:15px;")
        note_ajouter_edge.setText("Le graphe est enregistre ")
enregistrer_graphe.clicked.connect(enregistrer_graphe_event)
##################################################################################
def btn_kruskal_event()->None:
    """Représente le graphe kruskal du graphe courant à partir du sommet source saisi par l'utilisateur.

    Returns:
        None
    """
    global kruskal_repre
    audio_btn()
    if graphe.isPondere()==True and graphe.isConnexe()==True and graphe.isDirected()==False :
        if input_source_kruskal.text()=="":
            if frame_kruskal.isVisible():
                frame_kruskal.close()
            note_kruskal.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_kruskal.setText("Champs vide !!")
            frame_kruskal.show()
        else :
            if input_source_kruskal.text() in graphe.getNetworkxGraph():
                if frame_kruskal.isVisible():
                    frame_kruskal.close()
                kruskal_repre=frame_kruskal.newFrameGraphe(0,30,300,270,graphe.getNetworkxGraph(),"graphe",None)
                note_kruskal.setStyleSheet("background-color: green ; color : white;font-size:15px;")
                frame_graphe_rep.close()
                frame_graphe_rep_nx=frame_graphe_rep.newFrameGraphe(0,0,600,300,graphe.getKruskalGraphe(input_source_kruskal.text()),"kruskal",None)
                frame_graphe_rep.show()
                note_kruskal.setText("kruskal representer ...")
                frame_kruskal.show()
            else :
                if frame_kruskal.isVisible():
                    frame_kruskal.close()
                kruskal_repre=frame_kruskal.newFrameGraphe(0,30,300,270,graphe.getVideGraphe(),"kruskal",None)
                note_kruskal.setStyleSheet("background-color: red ; color : white;font-size:15px;")
                note_kruskal.setText(f"{input_source_kruskal.text()} n'est pas un sommet de graphe !!!")
                frame_kruskal.show()
    else :
        if graphe.isVide():
            if frame_kruskal.isVisible():
                frame_kruskal.close()
            note_kruskal.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_kruskal.setText("Graphe vide !!!")
            frame_kruskal.show()
        elif graphe.isPondere()==False :
            note_kruskal.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_kruskal.setText("Graphe n'est pas pondére !!!")
        elif graphe.isDirected()==True :
            note_kruskal.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_kruskal.setText("Graphe oriénter !!!")
        elif graphe.isConnexe()==False :
            note_kruskal.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_kruskal.setText("Graphe n'est pas connexe !!!")
btn_kruskal.clicked.connect(btn_kruskal_event)
##################################################################################

def btn_prim_event()->None:
    """
    Fonction qui représente le graphe sous forme d'un arbre couvrant minimal avec l'algorithme de Prim.

    Returns:
        Aucune valeur de retour.
    """
    global prim_repre
    audio_btn()
    if graphe.isPondere()==True and graphe.isConnexe()==True and graphe.isDirected()==False :
        if input_source_prim.text()=="":
            if frame_prim.isVisible():
                frame_prim.close()
            note_prim.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_prim.setText("Champs vide !!")
            frame_prim.show()
        else :
            if input_source_prim.text() in graphe.getNetworkxGraph():
                if frame_prim.isVisible():
                    frame_prim.close()
                prim_repre=frame_prim.newFrameGraphe(0,30,300,270,graphe.getNetworkxGraph(),"graphe",None)
                frame_graphe_rep.close()
                frame_graphe_rep_nx=frame_graphe_rep.newFrameGraphe(0,0,600,300,graphe.getPrimGraphe(input_source_prim.text()),"prim",None)
                frame_graphe_rep.show()
                note_prim.setStyleSheet("background-color: green ; color : white;font-size:15px;")
                note_prim.setText("Prim representer ...")
                frame_prim.show()
            else :
                if frame_prim.isVisible():
                    frame_prim.close()
                prim_repre=frame_prim.newFrameGraphe(0,30,300,270,graphe.getVideGraphe(),"prim",None)
                note_prim.setStyleSheet("background-color: red ; color : white;font-size:15px;")
                note_prim.setText(f"{input_source_prim.text()} n'est pas un sommet de graphe !!!")
                frame_prim.show()
    else :
        if graphe.isVide():
            if frame_prim.isVisible():
                frame_prim.close()
                # prim_repre=frame_prim.newFrameGraphe(0,30,300,270,graphe.getPrimGraphe(input_source_prim.text()),"prim",None)
            note_prim.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_prim.setText("Graphe vide !!!")
            frame_prim.show()
        elif graphe.isPondere()==False :
            note_prim.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_prim.setText("Graphe n'est pas pondére !!!")
        elif graphe.isDirected()==True :
            note_prim.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_prim.setText("Graphe oriénter !!!")
        elif graphe.isConnexe()==False :
            note_prim.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_prim.setText("Graphe n'est pas connexe !!!")
            
                
btn_prim.clicked.connect(btn_prim_event)
######################################
def btn_bellman_ford_event()->None:
    """
    Effectue l'algorithme de Bellman-Ford et affiche la représentation graphique du résultat.

    Returns:
        None
    """
    global bellman_ford_repre
    audio_btn()
    if graphe.isPondere():
        if input_source_bellman_ford.text()=='' or input_pointFinal_bellman_ford.text()=='':
            if frame_bellman_ford.isVisible():
                frame_bellman_ford.close()
            bellman_ford_repre=frame_bellman_ford.newFrameGraphe(0,30,300,270,graphe.getVideGraphe(),"bfs",None)
            note_bellman_ford.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_bellman_ford.setText("Champs vide !!")
            frame_bellman_ford.show()
        else :
            if input_source_bellman_ford.text() in graphe.getNetworkxGraph() and input_pointFinal_bellman_ford.text() in graphe.getNetworkxGraph():
                if frame_bellman_ford.isVisible():
                    frame_bellman_ford.close()
                bellman_ford_repre=frame_bellman_ford.newFrameGraphe(0,30,300,270,graphe.getNetworkxGraph(),"graphe",None)
                frame_graphe_rep.close()
                print(graphe.getListeBellmanFord(input_source_bellman_ford.text(),input_pointFinal_bellman_ford.text()))
                frame_graphe_rep_nx=frame_graphe_rep.newFrameGraphe(0,0,600,300,graphe.getNetworkxGraph(),"bellman_ford",graphe.getListeBellmanFord(input_source_bellman_ford.text(),input_pointFinal_bellman_ford.text()))
                frame_graphe_rep.show()
                note_bellman_ford.setStyleSheet("background-color: green ; color : white;font-size:15px;")
                note_bellman_ford.setText("Bellman-Ford representer...")
                frame_bellman_ford.show()
            else :
                if frame_bellman_ford.isVisible():
                    frame_bellman_ford.close()
                bellman_ford_repre=frame_bellman_ford.newFrameGraphe(0,30,300,270,graphe.getVideGraphe(),"bfs",None)
                note_bellman_ford.setStyleSheet("background-color: red ; color : white;font-size:15px;")
                note_bellman_ford.setText(f"{input_source_bellman_ford.text()} ou {input_pointFinal_bellman_ford.text()} n'est pas un sommet de graphe")
                frame_bellman_ford.show()
    else:
        # btn_dijkstra.setEnabled(False)
        note_dijkstra.setStyleSheet("background-color:red;font-size:10px;")
        note_dijkstra.setText("<b>Bellman-Ford</b> ne s'applique pas au graphe non pondére !!!")
btn_bellman_ford.clicked.connect(btn_bellman_ford_event)
#######################################
def btn_dijkstra_event()->None:
    """
    Événement déclenché lors du clic sur le bouton "Dijkstra".
    Représente le résultat de l'algorithme de Dijkstra sur le graphe s'il est pondéré et que les champs "source" 
    et "point final" sont remplis. Sinon, affiche un message d'erreur et un graphe vide. Si le graphe n'est pas 
    pondéré, affiche un message d'erreur spécifique et un graphe vide.
    """
    global dijkstra_repre
    audio_btn()
    if graphe.isPondere():
        if graphe.isAllPositive()==False:
            note_dijkstra.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_dijkstra.setText("Graphe admet des arrete avec poids negative")
        elif input_source_dijkstra.text()=='' or input_pointFinal_dijkstra.text()=='':
            if frame_dijkstra.isVisible():
                frame_dijkstra.close()
            dijkstra_repre=frame_dijkstra.newFrameGraphe(0,30,300,270,graphe.getVideGraphe(),"bfs",None)
            note_dijkstra.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_dijkstra.setText("Champs vide !!")
            frame_dijkstra.show()
        else :
            if input_source_dijkstra.text() in graphe.getNetworkxGraph() and input_pointFinal_dijkstra.text() in graphe.getNetworkxGraph():
                try:
                    dijkstra_repre=frame_dijkstra.newFrameGraphe(0,30,300,270,graphe.getNetworkxGraph(),"graphe",None)
                    frame_graphe_rep.close()
                    frame_graphe_rep_nx=frame_graphe_rep.newFrameGraphe(0,0,600,300,graphe.getNetworkxGraph(),"dijkstra",graphe.getListeDijkstra(input_source_dijkstra.text(),input_pointFinal_dijkstra.text()))
                    note_dijkstra.setStyleSheet("background-color: green ; color : white;font-size:15px;")
                    note_dijkstra.setText("Dijkstra representer...")
                    if frame_dijkstra.isVisible():
                        dijkstra_repre.close()
                    frame_graphe_rep.show()
                    dijkstra_repre.show()
                except:
                    note_dijkstra.setStyleSheet("background-color:red;font-size:15px;color : white;")
                    note_dijkstra.setText(f"aucun route entre {input_source_dijkstra.text()} et {input_pointFinal_dijkstra.text()}")
            else :
                if frame_dijkstra.isVisible():
                    frame_dijkstra.close()
                dijkstra_repre=frame_dijkstra.newFrameGraphe(0,30,300,270,graphe.getVideGraphe(),"bfs",None)
                note_dijkstra.setStyleSheet("background-color: red ; color : white;font-size:15px;")
                note_dijkstra.setText(f"{input_source_dijkstra.text()} ou {input_pointFinal_dijkstra.text()} n'est pas un sommet de graphe")
                frame_dijkstra.show()
    else:
        # btn_dijkstra.setEnabled(False)
        note_dijkstra.setStyleSheet("background-color:red;font-size:10px;")
        note_dijkstra.setText("<b>Dijkstra</b> ne s'applique pas au graphe non pondére !!!")
btn_dijkstra.clicked.connect(btn_dijkstra_event)
##############################################
def btn_bfs_event()->None:
    """Lance l'événement du bouton BFS.

    Cette fonction récupère le texte de l'entrée de source BFS et vérifie si elle n'est pas vide et si elle est 
    présente dans le graphe. Si elle est valide, cette fonction ferme la fenêtre d'affichage BFS précédente, 
    crée un nouveau graphique pour afficher le BFS du graphe à partir du nœud source donné, puis affiche le graphique 
    créé et définit le texte de la note pour indiquer que le BFS est représenté. Si le texte de l'entrée de source 
    BFS est vide, cette fonction crée un graphique vide et définit le texte de la note pour indiquer que le champ 
    est vide. Si l'entrée de source BFS n'est pas un sommet du graphe, cette fonction crée un graphique vide et 
    définit le texte de la note pour indiquer que l'entrée n'est pas un sommet du graphe.
    """
    global bfs_repre
    audio_btn()
    if input_source_bfs.text()=='':
        frame_bfs.close()
        bfs_repre=frame_bfs.newFrameGraphe(0,30,300,270,graphe.getVideGraphe(),"bfs",None)
        note_bfs.setStyleSheet("background-color: red ; color : white;font-size:15px;")
        note_bfs.setText("Champs vide !!")
        frame_bfs.show()
    else :
        if input_source_bfs.text() in graphe.getNetworkxGraph():
            frame_bfs.close()
            bfs_repre=frame_bfs.newFrameGraphe(0,30,300,270,graphe.getNetworkxGraph(),"graphe",None)
            frame_graphe_rep.close()
            frame_graphe_rep_nx=frame_graphe_rep.newFrameGraphe(0,0,600,300,graphe.getBfsGraphe(input_source_bfs.text()),"bfs",None)
            frame_graphe_rep.show()
            note_bfs.setStyleSheet("background-color: green ; color : white;font-size:15px;")
            note_bfs.setText("Le BFS representer...")
            frame_bfs.show()
        else :
            frame_bfs.close()
            bfs_repre=frame_bfs.newFrameGraphe(0,30,300,270,graphe.getVideGraphe(),"bfs",None)
            note_bfs.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_bfs.setText(f"{input_source_bfs.text()} n'est pas un sommet de grahe")
            frame_bfs.show()
btn_bfs.clicked.connect(btn_bfs_event)

    
#########################################
#frame_warshall,btn_warshall,note_warshall,warshall_repre
def btn_warshall_event():
    """
    Effectue l'algorithme de Warshall et affiche la représentation graphique du résultat.

    Returns:
        None
    """
    audio_btn()
    if graphe.isVide():
        frame_warshall.close()
        note_warshall.setStyleSheet("background-color: red ; color : white;font-size:15px;")
        note_warshall.setText(f"graphe vide !!!")
        frame_warshall.show()
    elif graphe.isDirected()==False:
        frame_warshall.close()
        note_warshall.setStyleSheet("background-color: red ; color : white;font-size:15px;")
        note_warshall.setText(f"graphe non-oriénter!!!")
        frame_warshall.show()
    else:
        frame_warshall.close()
        warshall_repre=frame_warshall.newFrameGraphe(0,30,400,270,graphe.getNetworkxGraph(),"graphe",None)
        frame_graphe_rep.close()
        frame_graphe_rep_nx=frame_graphe_rep.newFrameGraphe(0,0,600,300,graphe.getWarshallGraphe(),"warshall",None,graphe.getNetworkxGraph())
        frame_graphe_rep.show()
        note_warshall.setStyleSheet("background-color: green ; color : white;font-size:15px;")
        note_warshall.setText(f"Warshall representer")
        frame_warshall.show()
btn_warshall.clicked.connect(btn_warshall_event)
#########################################
    
def btn_dfs_event()->None:
    """
    Représente le parcours en profondeur (DFS) à partir d'un sommet donné sur le graphe.
    
    Returns:
        None
    """
    global dfs_repre
    audio_btn()
    if input_source_dfs.text()=='':
        dfs_repre=frame_dfs.newFrameGraphe(0,30,300,270,graphe.getVideGraphe(),"dfs",None)
        note_dfs.setStyleSheet("background-color: red ; color : white;font-size:15px;")
        note_dfs.setText("Champs vide !!")
    else :
        if input_source_dfs.text() in graphe.getNetworkxGraph():
            frame_dfs.close()
            dfs_repre=frame_dfs.newFrameGraphe(0,30,300,270,graphe.getNetworkxGraph(),"graphe",None)
            frame_graphe_rep.close()
            frame_graphe_rep_nx=frame_graphe_rep.newFrameGraphe(0,0,600,300,graphe.getDfsGraphe(input_source_dfs.text()),"dfs",None)
            frame_graphe_rep.show()
            note_dfs.setStyleSheet("background-color: green ; color : white;font-size:15px;")
            note_dfs.setText("Le DFS representer...")
            frame_dfs.show()
        else :
            dfs_repre=frame_dfs.newFrameGraphe(0,30,300,270,graphe.getVideGraphe(),"dfs",None)
            note_dfs.setStyleSheet("background-color: red ; color : white;font-size:15px;")
            note_dfs.setText(f"{input_source_dfs.text()} n'est pas un sommet de grahe")
btn_dfs.clicked.connect(btn_dfs_event)

def show_info_graph()->None:
    """
    Affiche les informations sur le graphe dans la fenêtre d'informations.
    
    Si la fenêtre d'informations est visible, cette fonction met à jour les informations.
    Si la fenêtre de parcours BFS est visible, cette fonction lance la fonction d'affichage du parcours BFS.
    Si la fenêtre de parcours DFS est visible, cette fonction lance la fonction d'affichage du parcours DFS.
    """
    if frame_info.isVisible():
        frame_info.closeFrame()
    if graphe.getNombreSommet()!=0:
        if graphe.isDirected() :
            is_directed.setText("Graphe oriénter : Oui") 
        else : 
            is_directed.setText("Graphe oriénter : Non")
        if graphe.isPondere() :
            is_weighted.setText("Graphe pondére : Oui") 
        else : 
            is_weighted.setText("Graphe pondére : Non")
        number_of_nodes.setText(f'Nombre des sommet : '+str(graphe.getNombreSommet()))
        if graphe.isDirected():
            number_of_edges.setText("Nombre des arcs : "+str(graphe.getNombreArrete()))
        else :
            number_of_edges.setText("Nombre des arretes : "+str(graphe.getNombreArrete()))  
        if graphe.isEulerian(): 
            is_eulerian.setText("Le graphe est Eulerien : Oui")
        else :
            is_eulerian.setText("Le graphe est Eulerien : Non")
        if graphe.isPlanaire():
            is_planaire.setText("Le graphe est planaire : Oui")
        else:
            is_planaire.setText("Le graphe est planaire : Non")
        if graphe.isConnexe():
            if graphe.isDirected():
                is_connexe.setText("Le graphe est fortement connexe : Oui")
            else : 
                is_connexe.setText("Le graphe est connexe : Oui")
        else :
            if graphe.isDirected():
                is_connexe.setText("Le graphe est fortement connexe : Non")
            else : 
                is_connexe.setText("Le graphe est connexe : Non")
        liste_nodes.setText("V={"+str(graphe.getListeSommet())[1:-1]+"}") 
        liste_edges.setText("E={"+str(graphe.getListeArrete())[1:-1]+"}")   
        density.setText("Densite :{:.2f}".format(graphe.getDensite()))
    else :
        if graphe.isDirected() :
            is_directed.setText("Graphe oriénter : Oui") 
        else : 
            is_directed.setText("Graphe oriénter : Non")
        if graphe.isPondere() :
            is_weighted.setText("Graphe pondére : Oui") 
        else : 
            is_weighted.setText("Graphe pondére : Non")
        number_of_nodes.setText(f'Nombre des sommet : '+str(graphe.getNombreSommet()))
        if graphe.isDirected()==False:
            number_of_edges.setText("Nombre des arretes : "+str(graphe.getNombreArrete()))   
        else :
            number_of_edges.setText("Nombre des arcs : "+str(graphe.getNombreArrete()))
        is_eulerian.setText("Le graphe est Eulerien :")
        is_planaire.setText("Le graphe est planaire :")
        if graphe.isDirected():
            is_connexe.setText("Le graphe est fortement connexe :")
        else : 
            is_connexe.setText("Le graphe est connexe :")
        liste_nodes.setText("V={}") 
        liste_edges.setText("E={}") 
        density.setText("Densite : ")
    degre_nodes.setColumnCount(graphe.getNombreSommet())
    degre_nodes.setVerticalHeaderLabels("Degree,..".split(","))
    degre_nodes.setHorizontalHeaderLabels(str(graphe.getListeSommet())[1:-1].split(","))
    degre_nodes.setStyleSheet("font-size:12px;")
    k=0
    for i in list(graphe.getDegreeSommets().values()):
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        item.setText(str(i))
        degre_nodes.setItem(0, k, item)
        k+=1
    if graphe.isDirected() :
        liste_edges.setToolTip("Ensemble des arcs")
    else:
        liste_edges.setToolTip("Ensemble des arretes")
    liste_nodes.setToolTip("Ensemble des sommet")

    show_frame(frame_info)
def update_info_graphe()->None:
    """
    Met à jour les informations du graphe dans le cadre d'informations s'il est visible,
    et met à jour les cadres de parcours BFS et DFS s'ils sont visibles.
    """
    if frame_info.isVisible():
        show_info_graph()
    if frame_bfs.isVisible():
        btn_bfs_event()
    if frame_dfs.isVisible():
         btn_dfs_event()
    #   Le probleme si comment update un frame bfs et un frame dfs apres l'ajoute ou la supression d'un sommet de graphe
def show_data_historique():
    """
    Affiche les données de l'historique du graphe dans le tableau 'table_historique_graphe'.
    Si la table est vide, affiche un message de notification en vert.
    """
    db = DBG("graphe")
    if db.nbrData()!= -1 :
        try :
            table_historique_graphe.setRowCount(db.nbrData())
            results = db.selectAll()
            for i in range(0,db.nbrData()):
                result = results[i]
                for j in range(0,6):
                    table_historique_graphe.setItem(i,j, QTableWidgetItem(result[j]))
        except Exception as e:
            print(e)
    else :
        note_table_db.setStyleSheet("font-size:15px;background-color:green;color:white;")
        note_table_db.setText("Table vide !!!")
#DRY
def patron_db(func,arg:bool):
    """
    Affiche un message d'erreur si le champ d'ID est vide ou si aucun graphe ne correspond à l'ID spécifié.
    Exécute la fonction passée en paramètre en fonction de la valeur booléenne `arg`.
    
    Args:
    - func : fonction à exécuter.
    - arg : valeur booléenne qui indique si la fonction `func` prend un argument ou non.
    
    Returns:
    None
    """
    audio_btn()
    db = DBG("graphe")
    if input_id.text()=="":
        note_table_db.setStyleSheet("font-size:15px;background-color:red;color:white;")
        note_table_db.setText("Champ vide !!!")
    else :
        try :
            if int(input_id.text())>db.nbrData() or int(input_id.text())==0:
                note_table_db.setStyleSheet("font-size:15px;background-color:red;color:white;")
                note_table_db.setText(f"Aucun graphe avec cette id={input_id.text()}")
            else :
                if arg==True :
                    func(db)
                else:
                    func()
        except :
            note_table_db.setStyleSheet("font-size:15px;background-color:red;color:white;")
            note_table_db.setText(f"{input_id.text()} n'est pas un nombre !!!")
def btn_recherche_event():
    """
    Met en évidence la ligne correspondant à l'ID de graphe entré dans le champ de recherche en changeant sa couleur de 
    police en rouge tandis que toutes les autres lignes ont leur couleur de police en noir. Réinitialise également le 
    champ de note_table_db.

    Args:
        None

    Returns:
        None
    """
    for j in range(table_historique_graphe.rowCount()):
        for i in range(table_historique_graphe.columnCount()):
            table_historique_graphe.item(j, i).setForeground(QColor(0,0,0))        
    for i in range(table_historique_graphe.columnCount()):
                table_historique_graphe.item(int(input_id.text())-1, i).setForeground(QColor(255,0,0))
    note_table_db.setStyleSheet("font-size:15px;background-color:none;color:white;")
    note_table_db.setText("")
    
def btn_utiliser_event(db:DBG):
        """
        Fonction qui permet d'utiliser le graphe correspondant à l'identifiant entré dans l'interface.
        
        Args:
            
            db (DBG): une instance de la classe DBG qui permet d'effectuer des requêtes sur la base de données.
        
        Returns:
            
            None
        
        Cette fonction réalise les actions suivantes :
            
            récupère les informations du graphe correspondant à l'identifiant entré dans la base de données.
            
            modifie le graphe de l'application en fonction des caractéristiques du graphe récupéré.
            
            affiche le nouveau graphe dans l'interface.
            
            active ou désactive les champs liés aux poids des arêtes en fonction du type de graphe.
            
            met à jour les notes de l'interface pour donner un feedback à l'utilisateur.
        """
        results = db.selectAll()
        result=results[int(input_id.text())-1]
        if result[2]=="Oui" and result[3]=="Oui" :
            graphe.toDirectedPondere()
        elif result[2]=="Non" and result[3]=="Oui" :
            graphe.toUnDirectedPondere()
        elif result[2]=="Non" and result[3]=="Non" :
            graphe.toUnDirected()
        elif result[2]=="Oui" and result[3]=="Non" :
            graphe.toDirected()
        resu=eval("["+result[5]+"]")
        if result[3]=="Oui":
            for i in resu :
                graphe.add_edge_value(i[0],i[1],float(i[2]))
        else :
            for i in resu :
                graphe.add_edge(i[0],i[1])
        note_table_db.setStyleSheet("font-size:15px;background-color:green;color:white;")
        note_table_db.setText(f"Le graphe de id={input_id.text()} est utiliser")
        note_ajouter_edge.setStyleSheet("font-size:15px;background-color:none;color:white;")
        note_ajouter_edge.setText(f"")
        graphe_rep()
        show_info_graph()
        if graphe.isPondere():
            input_poids_arrete.setEnabled(True)
            poids_arrete.setEnabled(True)
        else :
            input_poids_arrete.setEnabled(False)
            poids_arrete.setEnabled(False)
def btn_delete_event(db:DBG):
    """
    Supprime un graphe de la base de données.

    Args:
        db (DBG): Objet DBG contenant les informations de la base de données.

    Returns:
        None
    """
    db.delete(int(input_id.text()))
    show_data_historique()
btn_utiliser.clicked.connect(partial(patron_db,btn_utiliser_event,True))
btn_delete.clicked.connect(partial(patron_db,btn_delete_event,True))
btn_recherche.clicked.connect(partial(patron_db,btn_recherche_event,False))   
def show_frame(frame:QFrame)->None:
    """
    Cette fonction permet d'afficher un frame spécifique en cachant les autres frames qui sont déjà affichés.

    Args:
        frame (QFrame): Le frame à afficher.

    Returns:
        None
    """
    if frame_bellman_ford.isVisible():
        frame_bellman_ford.close()
    if frame_pdf.isVisible():
        frame_pdf.close()
    if frame_bfs.isVisible():
        frame_bfs.close()
    if frame_dfs.isVisible():
        frame_dfs.close()
    if frame_info.isVisible():
        frame_info.close()
    if frame_dijkstra.isVisible():
        frame_dijkstra.close()
    if frame_prim.isVisible():
        frame_prim.close()
    if frame_kruskal.isVisible():
        frame_kruskal.close()
    if frame_tableau_bd.isVisible():
        frame_tableau_bd.close()
    if frame_matrix.isVisible():
        frame_matrix.close()
    if frame_warshall.isVisible():
        frame_warshall.close()
    if frame_graphe_manipulation.isVisible():
        frame_graphe_manipulation.close()
    if frame==frame_tableau_bd:##############################
        frame_graphe_rep.close()
        show_data_historique()
    elif frame==frame_graphe_rep:
        frame_info.show()
    else:
        frame_graphe_rep.show()
    frame.show()
    
def btn_info_graphe_bare_event()->None:
    """
    Affiche les informations générales du graphe dans la fenêtre d'information.
    
    Args: 
        Aucun
        
    Returns:
        None
    """
    audio_btn()
    show_info_graph()
    
def show_frame_sound(frame:QFrame)->None:
    """
    Affiche le frame donné et joue un son de bouton.

    Args:
        frame (QFrame): le frame à afficher.

    Returns:
        None
    """
    audio_btn()
    show_frame(frame)
def btn_matrix_bare_event():
    """
    Affiche le frame pour la matrice du graphe et remplit les tableaux de la matrice 
    adjacente et incidence avec les valeurs correspondantes.
    """
    show_frame_sound(frame_matrix)
    if graphe.getNombreSommet()!=0:
        table_matrix_adj.setRowCount(graphe.getNombreSommet())
        table_matrix_adj.setColumnCount(graphe.getNombreSommet())
        table_matrix_adj.setHorizontalHeaderLabels(list(graphe.getListeSommet()))
        table_matrix_adj.setVerticalHeaderLabels(list(graphe.getListeSommet()))
        table_matrix_inc.setRowCount(graphe.getNombreSommet())
        table_matrix_inc.setColumnCount(graphe.getNombreArrete())
        listArrete=""
        for i in graphe.getListeArrete():
            if listArrete!="":
                listArrete+=":"+str(i)
            else :
                listArrete=str(i)
        table_matrix_inc.setHorizontalHeaderLabels(listArrete.split(":"))
        table_matrix_inc.setVerticalHeaderLabels(list(graphe.getListeSommet()))
        matrix_adj=graphe.getMatriceAdjacent()
        matrix_inc=graphe.getMatriceIncidence()
        for i in range(graphe.getNombreSommet()):
            for j in range(graphe.getNombreSommet()):
                table_matrix_adj.setItem(i,j, QTableWidgetItem(str(matrix_adj[i][j])))
        for i in range(graphe.getNombreSommet()):
            for j in range(graphe.getNombreArrete()):
                table_matrix_inc.setItem(i,j, QTableWidgetItem(str(matrix_inc[i][j])))

def btn_warshall_bare_event():
    """
    Affiche le cadre de l'algorithme de Warshall et exécute l'événement de l'algorithme de Warshall.

    Returns:
        None
    """
    show_frame(frame_warshall)
    btn_warshall_event()
def btn_home_bare_event():
    """
    Affiche le cadre de la représentation graphique et exécute l'événement de la représentation graphique.

    Returns:
        None
    """
    show_frame_sound(frame_graphe_rep)
    graphe_rep()
btn_info_graphe_bare.clicked.connect(btn_info_graphe_bare_event)
btn_bfs_bare.clicked.connect(partial(show_frame_sound,frame_bfs))
btn_dfs_bare.clicked.connect(partial(show_frame_sound,frame_dfs))
btn_dijkstra_bare.clicked.connect(partial(show_frame_sound,frame_dijkstra))
btn_prim_bare.clicked.connect(partial(show_frame_sound,frame_prim))
btn_kruskal_bare.clicked.connect(partial(show_frame_sound,frame_kruskal))
btn_historique_bare.clicked.connect(partial(show_frame_sound,frame_tableau_bd))
btn_genere_pdf_bare.clicked.connect(btn_genere_pdf_bare_event)
btn_home_bare.clicked.connect(btn_home_bare_event)
btn_graphe_manipulation_bare.clicked.connect(partial(show_frame_sound,frame_graphe_manipulation))
btn_matrix_bare.clicked.connect(btn_matrix_bare_event)
btn_warshall_bare.clicked.connect(btn_warshall_bare_event)
btn_bellman_ford_bare.clicked.connect(partial(show_frame_sound,frame_bellman_ford))
def ajouter_edge()->None:
    """
    Ajoute un sommet ou une arête dans le graphe en fonction des champs remplis dans l'interface graphique.

    Args:
        Aucun.

    Returns:
        None.
    """
    audio_btn()
    if graphe.isPondere():
        if input_sommet_arriver.text()!='' and input_sommet_depart.text()!='' and input_poids_arrete.text()!='':
            try :
                graphe.add_edge_value(input_sommet_depart.text(),input_sommet_arriver.text(),float(input_poids_arrete.text()))
                note_ajouter_edge.setStyleSheet('background-color:green;color:white;')
                if graphe.isDirected():
                    note_ajouter_edge.setText(f"L'arc : {input_sommet_depart.text()}---({input_poids_arrete.text()})--->{input_sommet_arriver.text()} est ajouter")
                else:
                    note_ajouter_edge.setText(f"L'arrete : {input_sommet_depart.text()}---({input_poids_arrete.text()})---{input_sommet_arriver.text()} est ajouter")
                viderInputChamps()
            except :
                note_ajouter_edge.setStyleSheet('background-color:red;color:white;')
                note_ajouter_edge.setText("Le poids entree n'est pas un reel")
        elif input_sommet_arriver.text()=='' and input_sommet_depart.text()!='' and input_poids_arrete.text()=='':
            graphe.add_vertex(input_sommet_depart.text())
            note_ajouter_edge.setStyleSheet('background-color:green;color:white;')
            note_ajouter_edge.setText(f"Le sommet : {input_sommet_depart.text()} est ajouter")
            viderInputChamps()
        elif input_sommet_arriver.text()!='' and input_sommet_depart.text()=='' and input_poids_arrete.text()=='':
            graphe.add_vertex(input_sommet_arriver.text())
            note_ajouter_edge.setStyleSheet('background-color:green;color:white;')
            note_ajouter_edge.setText(f"Le sommet : {input_sommet_arriver.text()} est ajouter")
            viderInputChamps()
        elif input_sommet_arriver.text()!='' and input_sommet_depart.text()=='' and input_poids_arrete.text()!='':
            note_ajouter_edge.setStyleSheet('background-color:red;color:white;')
            note_ajouter_edge.setText(f"Le champ de sommet de depart est vide")
        elif input_sommet_arriver.text()=='' and input_sommet_depart.text()!='' and input_poids_arrete.text()!='':
            note_ajouter_edge.setStyleSheet('background-color:red;')
            note_ajouter_edge.setText(f"Le champ de sommet d'arriver est vide")
        elif input_sommet_arriver.text()!='' and input_sommet_depart.text()!='' and input_poids_arrete.text()=='':
            note_ajouter_edge.setStyleSheet('background-color:red;color:white;')
            note_ajouter_edge.setText(f"Le champ de poids est vide")
    else:
        if input_sommet_arriver.text()!='' and input_sommet_depart.text()!='':
            graphe.add_edge(input_sommet_depart.text(),input_sommet_arriver.text())
            note_ajouter_edge.setStyleSheet('background-color:green;color:white;')
            if graphe.isDirected():
                note_ajouter_edge.setText(f"L'arrete : {input_sommet_depart.text()}------>{input_sommet_arriver.text()} est ajouter")
            else:
                note_ajouter_edge.setText(f"L'arrete : {input_sommet_depart.text()}------{input_sommet_arriver.text()} est ajouter")
            viderInputChamps()
        elif input_sommet_arriver.text()!='' and input_sommet_depart.text()=='':
            graphe.add_vertex(input_sommet_arriver.text())
            note_ajouter_edge.setStyleSheet('background-color:green;color:white;')
            note_ajouter_edge.setText(f"Le sommet : {input_sommet_arriver.text()} est ajouter")
            viderInputChamps()
        elif input_sommet_arriver.text()=='' and input_sommet_depart.text()!='':
            graphe.add_vertex(input_sommet_depart.text())
            note_ajouter_edge.setStyleSheet('background-color:green;color:white;')
            note_ajouter_edge.setText(f"Le sommet : {input_sommet_depart.text()} est ajouter")
            viderInputChamps()
        elif input_sommet_arriver.text()=='' and input_sommet_depart.text()=='':
            note_ajouter_edge.setStyleSheet('background-color:red;color:white;')
            note_ajouter_edge.setText(f"Les champs vide !!!")
    graphe_rep()
    update_info_graphe()

def supprimer_edge()->None:
    """Supprime un sommet ou une arête du graphe en fonction des valeurs entrées dans les champs de texte.

    Si les champs de texte sont vides, affiche un message d'erreur.
    Si seul le champ de texte "Sommet de départ" est rempli, supprime ce sommet du graphe.
    Si seul le champ de texte "Sommet d'arrivée" est rempli, supprime ce sommet du graphe.
    Si les deux champs de texte sont remplis, supprime l'arête entre les deux sommets du graphe.

    Affiche un message de confirmation si l'opération s'est bien déroulée et met à jour la représentation graphique
    du graphe ainsi que les informations affichées dans l'interface utilisateur.
    """
    audio_btn()
    global graphe_representation
    if input_sommet_arriver.text()!='' and input_sommet_depart.text()!='':
        if input_sommet_arriver.text() in graphe.getVertex() and input_sommet_depart.text() in graphe.getVertex():
            if input_sommet_arriver.text() in graphe.get_neighbors(input_sommet_depart.text()):
                graphe.remove_edge(input_sommet_depart.text(),input_sommet_arriver.text())
                note_ajouter_edge.setStyleSheet('background-color:green;color:white;')
                if graphe.isDirected():
                    note_ajouter_edge.setText(f"L'arc {input_sommet_depart.text()} -------> {input_sommet_arriver.text()} est supprimer")
                else:
                    note_ajouter_edge.setText(f"L'arrete {input_sommet_depart.text()} ------- {input_sommet_arriver.text()} est supprimer")
                viderInputChamps()
            else :
                note_ajouter_edge.setStyleSheet('background-color:red;color:white;')
                if graphe.isDirected():
                    note_ajouter_edge.setText(f"L'arc {input_sommet_depart.text()} -------> {input_sommet_arriver.text()} n'existe pas dans ce graphe")
                else:
                    note_ajouter_edge.setText(f"L'arrete {input_sommet_depart.text()} ------- {input_sommet_arriver.text()} n'existe pas dans ce graphe")
        else:
            note_ajouter_edge.setStyleSheet('background-color:red;color:white;')
            note_ajouter_edge.setText(f"{input_sommet_depart.text()} ou {input_sommet_arriver.text()} n'est pas un sommet de ce graphe")
    elif input_sommet_arriver.text()=='' and input_sommet_depart.text()!='':
        if input_sommet_depart.text() in graphe.getVertex():
            graphe.remove_vertex(input_sommet_depart.text())
            note_ajouter_edge.setStyleSheet('background-color:green;color:white;')
            note_ajouter_edge.setText(f"Le sommet : {input_sommet_depart.text()} est supprimer")
            viderInputChamps()
        else :
            note_ajouter_edge.setStyleSheet('background-color:red;color:white;')
            note_ajouter_edge.setText(f"Le sommet : {input_sommet_depart.text()} n'et pas un element de graphe !!")
    elif input_sommet_arriver.text()!='' and input_sommet_depart.text()=='':
        if input_sommet_arriver.text() in graphe.getVertex():
            graphe.remove_vertex(input_sommet_arriver.text())
            note_ajouter_edge.setStyleSheet('background-color:green;color:white;')
            note_ajouter_edge.setText(f"Le sommet : {input_sommet_arriver.text()} est supprimer")
            viderInputChamps()
        else :
            note_ajouter_edge.setStyleSheet('background-color:red;')
            note_ajouter_edge.setText(f"Le sommet : {input_sommet_arriver.text()} n'et pas un element de graphe !!")
    elif input_sommet_arriver.text()=='' and input_sommet_depart.text()=='':
        note_ajouter_edge.setStyleSheet('background-color:red;color:white;')
        note_ajouter_edge.setText(f"Les champ sont vide !!!")
    graphe_rep()
    update_info_graphe()
ajouter_arrete.clicked.connect(ajouter_edge)
supprimer_arrete.clicked.connect(supprimer_edge)
def type_graphe_activited()->None:
        """
        Change le type du graphe en fonction de l'option sélectionnée dans le menu déroulant type_graphe.
        Si l'option "Orientés" est sélectionnée, le graphe est transformé en un graphe orienté.
        Si l'option "Non-orientés" est sélectionnée, le graphe est transformé en un graphe non orienté.
        Si l'option "Non-orientés pondérés" est sélectionnée, le graphe est transformé en un graphe non orienté pondéré.
        Si l'option "Orientés pondérés" est sélectionnée, le graphe est transformé en un graphe orienté pondéré.
        La fonction met également à jour l'affichage du graphe ainsi que les informations sur le graphe.

        Args:
            Aucun.

        Returns:
            None.
        """
        audio_btn()
        global graphe
        func=type_graphe.currentText()
        if(func=="Orientés"):
            graphe.toDirected()
            poids_arrete.setEnabled(False)
            input_poids_arrete.setEnabled(False)
            note_ajouter_edge.setStyleSheet('background-color:green;color:white;')
            note_ajouter_edge.setText(f"Le graphe est change comme un graphe oriente")
        elif(func=="Non-orientés"):
            graphe.toUnDirected()
            poids_arrete.setEnabled(False)
            input_poids_arrete.setEnabled(False)
            note_ajouter_edge.setStyleSheet('background-color:green;color:white;')
            note_ajouter_edge.setText(f"Le graphe est change comme un graphe non oriente")
        elif(func=="Non-orientés pondérés"):
            graphe.toUnDirectedPondere()
            poids_arrete.setEnabled(True)
            input_poids_arrete.setEnabled(True)
            note_ajouter_edge.setStyleSheet('background-color:green;font-size:10px;color:white;')
            note_ajouter_edge.setText(f"Le graphe est change comme un graphe non oriente et pondere")
        elif(func=="Orientés pondérés"):
            graphe.toDirectedPondere()
            poids_arrete.setEnabled(True)
            input_poids_arrete.setEnabled(True)
            note_ajouter_edge.setStyleSheet('background-color:green;font-size:10px;color:white;')
            note_ajouter_edge.setText(f"Le graphe est change comme un graphe oriente pondere")
        graphe_rep()
        update_info_graphe()



def initialiser()->None:
    """
    Initialise le graphe en appelant la méthode init() de l'objet graphe.
    Affiche un message pour confirmer que l'initialisation est terminée et met à jour la représentation du graphe ainsi que les informations associées.

    Args:
        None

    Returns:
        None
    """
    audio_btn()
    graphe.init()
    note_ajouter_edge.setStyleSheet('background-color:green;')
    note_ajouter_edge.setText(f"Le graphe est initialiser")
    graphe_rep()
    update_info_graphe()
initialiser_graphe.clicked.connect(initialiser)
type_graphe.activated.connect(type_graphe_activited)

frame_dfs.close()
frame_bfs.close()
frame_info.close()
frame_dijkstra.close()
frame_prim.close()
frame_kruskal.close()
frame_tableau_bd.close()
frame_matrix.close()
frame_warshall.close()
frame_graphe_manipulation.close()
frame_pdf.close()
frame_bellman_ford.close()
show_info_graph()
graphe_rep()
generale_container.show()
#in generate docs comment  sys.exit(theorie_graphe_app.exec_())
sys.exit(theorie_graphe_app.exec_())
