
from PyQt5.QtWidgets import  QFileDialog

def pdfComponent(container)->tuple:
    frame_pdf=container.newFram(200,300,600,300,'','background-color:None;font-size:7px;')
    frame_pdf.newLabel(10,50,300,30,'font-size:15px;','Sommet de depart "Dijkstra/Ford" :',False)
    frame_pdf.newLabel(440,50,160,30,'font-size:15px;','<b>Title :</b> ',True)
    title_pdf=frame_pdf.newInput(440,80,150,20,'font-size:15px;','',True,None)
    frame_pdf.newLabel(440,110,160,30,'font-size:15px;','<b>Nom complete :</b> ',True)
    nom_complete_pdf=frame_pdf.newInput(440,140,150,20,'font-size:15px;','',True,None)
    input_source_dijkstra_pdf=frame_pdf.newInput(280,50,150,20,'font-size:15px;','',True,None)
    frame_pdf.newLabel(10,80,300,30,'font-size:15px;','Sommet d\'arriver "Dijkstra/Ford" :',False)
    input_pointFinal_dijkstra_pdf=frame_pdf.newInput(280,80,150,20,'font-size:15px;','',True,None)
    frame_pdf.newLabel(10,110,300,30,'font-size:15px;','Sommet de BFS :',False)
    input_source_bfs_pdf=frame_pdf.newInput(280,110,150,20,'font-size:15px;','',True,None)
    frame_pdf.newLabel(10,140,300,30,'font-size:15px;','Sommet de DFS :',False)
    input_source_dfs_pdf=frame_pdf.newInput(280,140,150,20,'font-size:15px;','',True,None)
    frame_pdf.newLabel(10,170,300,30,'font-size:15px;','Sommet de "Prim/Kruskal"',False)
    input_source_prim_pdf=frame_pdf.newInput(280,170,150,20,'font-size:15px;','',True,None)
    frame_pdf.newLabel(0,0,600,30,'font-size:15px;color:blue;','Generation d\'un pdf :',True)
    frame_pdf.newLabel(10,210,300,30,'font-size:15px;','Choisir un dossier :',False)
    btn_choisir_dossier_pdf=frame_pdf.newButton(220,213,150,20,'font-size:15px;','','Choisir un dossier',None,None)
    btn_pdf=frame_pdf.newButton(450,213,110,20,'background-color:white;color:black;font-size:15px;','background-color:black;color:white','enregistre pdf',None,None)
    note_pdf=frame_pdf.newLabel(50,250,500,30,'','',True)
    return frame_pdf,input_pointFinal_dijkstra_pdf,input_source_bfs_pdf,input_source_dfs_pdf,input_source_dijkstra_pdf,input_source_prim_pdf,btn_pdf,note_pdf,btn_choisir_dossier_pdf,title_pdf,nom_complete_pdf
