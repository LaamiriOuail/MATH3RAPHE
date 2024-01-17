from fpdf import FPDF
import datetime
import os
import sys
from pathlib import Path


parent_dir = os.path.abspath(os.path.join(os.getcwd(), '.'))
sys.path.append(parent_dir)
def dateTime()->list:
    return [str(datetime.date.today()),datetime.datetime.now().strftime('%H:%M:%S')]
def generate_pdf(title:str,nom:str,path:str,graphe,note_pdf):
    try:
        # Création d'un document PDF vierge
        pdf = FPDF()
        pdf.add_page()
        # Définition de la police et de la taille du texte
        pdf.set_font("Arial", size=12)
        #NOM complete
        pdf.set_xy(10, 10)
        pdf.cell(10, 10, nom)
        #Title
        pdf.set_font("Arial", size=17)
        pdf.set_xy(80, 10)
        pdf.cell(10, 10, title)
        #Date
        pdf.set_font("Arial", size=12)
        pdf.set_xy(180, 10)
        pdf.cell(10, 10, dateTime()[0])
        # Set line color to black
        pdf.set_draw_color(0, 0, 0)
        # Draw a line
        pdf.line(10, 20, 203, 20)
        # ORIENTER
        pdf.set_xy(5, 20)
        if graphe.isDirected():
            pdf.cell(0, 10, "Graphe oriénter : Oui")
        else:
            pdf.cell(0, 10, "Graphe oriénter : Non")
        # PONDERE
        pdf.set_xy(70, 20)
        if graphe.isPondere():
            pdf.cell(300, 10, "Graphe pondére : Oui")
        else:
            pdf.cell(300, 10, "Graphe pondére : Non")
        # PLANAIRE
        pdf.set_xy(5, 25)
        if graphe.isPlanaire():
            pdf.cell(0, 10, "Graphe planaire : Oui")
        else :
            pdf.cell(0, 10, "Graphe planaire : Non")
        # Connexe
        pdf.set_xy(70, 25)
        if graphe.isConnexe():
            if graphe.isDirected():
                pdf.cell(300, 10, "Graphe fortement connexe : Oui")
            else :
                pdf.cell(300, 10, "Graphe connexe : Oui")
        else :
            if graphe.isDirected():
                pdf.cell(300, 10, "Graphe fortement connexe : Non")
            else :
                pdf.cell(300, 10, "Graphe connexe : Non")
        # Euleriene
        pdf.set_xy(140, 20)
        if graphe.isEulerian():
            pdf.cell(0, 10, "Graphe eulerien : Oui")
        else:
            pdf.cell(0, 10, "Graphe eulerien : Non")
        # Densite
        pdf.set_xy(140, 25)
        pdf.cell(30, 10, "Densite : %.2f" % graphe.getDensite())
        # Ensemble des sommet
        pdf.set_xy(5, 30)
        pdf.cell(0, 10, "Les sommet :"+str(graphe.getListeSommet())[1:-1])
        # Ensemble des arretes
        pdf.set_xy(5, 35)
        pdf.cell(0, 13, "Les arretes :"+str(graphe.getListeArrete())[1:-1])
        #Tableau des degree
        pdf.set_text_color(255, 0, 0) # Rouge
        pdf.set_xy(5, 45)
        pdf.cell(0, 13, "Tableaux des degree :")
        pdf.set_text_color(0, 0, 0) # Rouge
        pdf.set_xy(0, 45)
        pdf.ln()
        matrix = [["Sommet"]+graphe.getListeSommet(), ["Degree"]+list(graphe.getDegreeSommets().values())]
        for row in matrix:
            i=0
            for item in row:
                if(i==0):
                    pdf.cell(20, 10, str(item), border=1)
                    i+=1
                else :
                    pdf.cell(7, 10, str(item), border=1)
            pdf.ln()
        #Matrix adjacente
        pdf.set_text_color(255, 0, 0) # Rouge
        pdf.set_xy(5, 160)
        pdf.cell(0, 13, "Matrice d'adjacent :")
        pdf.set_xy(0, 162)
        pdf.ln()
        pdf.set_text_color(0, 0, 0) 
        matrix = graphe.getMatriceAdjacent()
        for row in matrix:
            i=0
            for item in row:
                pdf.cell(10, 10, str(item), border=1)
            pdf.ln()
        #Matrix Incidente
        pdf.set_text_color(255, 0, 0) # Rouge
        pdf.set_xy(5, 80)
        pdf.cell(0, 13, "Matrice d'incidence :")
        pdf.ln()
        pdf.set_text_color(0, 0, 0) # Rouge
        matrix = graphe.getMatriceIncidence()
        for row in matrix:
            i=0
            for item in row:
                pdf.cell(10, 10, str(item), border=1)
            pdf.ln()
        pdf.add_page()

        #image de dfs
        pdf.image(Path('./public/image/graph-dfs.png'), x=0, y=130, w=100)
        # image dfs label
        pdf.set_font("Arial", size=10)
        pdf.set_xy(22, 140)
        pdf.cell(10, 130, "figure3 : Representation de DFS")

        #image de graphe
        pdf.image(Path('./public/image/graph.png'), x=0, y=30, w=100)
        # image graphe label
        pdf.set_font("Arial", size=10)
        pdf.set_xy(22, 40)
        pdf.cell(10, 130, "figure1 : Representation de graphe")
        if graphe.isDirected():
            #image de prime/kruskal(non-orienter pondere connexe) or warshall(orienter)
            pdf.image(Path('./public/image/graph-warshall.png'), x=110, y=130, w=100)
            # image prime/kruskal or warshall label
            pdf.set_font("Arial", size=10)
            pdf.set_xy(132, 140)
            pdf.cell(10, 130, "figure4 : Representation de Warshall")
        elif graphe.isConnexe() and graphe.isPondere():
            #image de prime/kruskal(non-orienter pondere connexe) 
            pdf.image(Path('./public/image/graph-prim.png'), x=110, y=130, w=100)
            # image prime/kruskal
            pdf.set_font("Arial", size=10)
            pdf.set_xy(132, 140)
            pdf.cell(10, 130, "figure4 : Representation de Prime/Kruskal")

        #image de bfs
        pdf.image(Path('./public/image/graph-bfs.png'), x=110, y=30, w=100)
        # image bfs label
        pdf.set_font("Arial", size=10)
        pdf.set_xy(132, 40)
        pdf.cell(10, 130, "figure2 : Representation de BFS")

        pdf.set_font("Arial", size=12)
        #NOM complete
        pdf.set_xy(10, 10)
        pdf.cell(10, 10, nom)
        #Title
        pdf.set_font("Arial", size=17)
        pdf.set_xy(80, 10)
        pdf.cell(10, 10, title)
        #Date
        pdf.set_font("Arial", size=12)
        pdf.set_xy(180, 10)
        pdf.cell(10, 10, dateTime()[0])
        # Set line color to black
        pdf.set_draw_color(0, 0, 0)
        # Draw a line
        pdf.line(10, 20, 203, 20)

        if graphe.isPondere():
            pdf.add_page()
            #image de dijkstra/ford
            pdf.image(Path('./public/image/graph-bellman-ford.png'), x=0, y=30, w=100)
            # image dijkstra/ford label
            pdf.set_font("Arial", size=10)
            pdf.set_xy(22, 40)
            pdf.cell(10, 130, "figure5 : Representation de Dijikstra/Ford")

            pdf.set_font("Arial", size=12)
            #NOM complete
            pdf.set_xy(10, 10)
            pdf.cell(10, 10, nom)
            #Title
            pdf.set_font("Arial", size=17)
            pdf.set_xy(80, 10)
            pdf.cell(10, 10, title)
            #Date
            pdf.set_font("Arial", size=12)
            pdf.set_xy(180, 10)
            pdf.cell(10, 10, dateTime()[0])
            # Set line color to black
            pdf.set_draw_color(0, 0, 0)
            # Draw a line
            pdf.line(10, 20, 203, 20)

        pdf.output(Path(f"{path}\\{title}.pdf"))
        note_pdf.setText(f"Pdf enregistrer en : {path}\\{title}.pdf")
        note_pdf.setStyleSheet("background-color: green ; color : white;font-size:15px;")
    except:
        print("in pdf generator methode")