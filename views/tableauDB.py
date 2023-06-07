from PyQt5.QtWidgets import  QTableWidget
def tableauBaseDonner(container):
    """
    Crée un tableau de base de données à partir d'un conteneur donné.

    Args:
        container: Le conteneur dans lequel le tableau sera créé.

    Returns:
        
        frame_tableau_bd: Le cadre du tableau de base de données.
        
        input_id: Le champ de saisie pour l'identifiant.
        
        btn_recherche: Le bouton de recherche.
        
        btn_delete: Le bouton de suppression.
        
        btn_utiliser: Le bouton d'utilisation.
        
        table_historique_graphe: Le tableau d'historique des graphes.
        
        note_table_db: L'étiquette de la table de base de données.
    """

    frame_tableau_bd=container.newFram(200,0,600,600,'','background-color:None;font-size:15px;')
    rechetrche_label=frame_tableau_bd.newLabel(0,20,90,50,'font-size:15px;','Identifiant',False)
    input_id=frame_tableau_bd.newInput(90,35,130,20,'','',True,None)
    btn_recherche=frame_tableau_bd.newButton(230,35,100,20,'background-color:black;color:white;font-size:15px','background-color:white;color:black','Rechercehe',None,None)
    btn_delete=frame_tableau_bd.newButton(340,35,100,20,'background-color:black;color:white;font-size:15px','background-color:white;color:black','Supprimer',None,None)
    btn_utiliser=frame_tableau_bd.newButton(450,35,100,20,'background-color:black;color:white;font-size:15px','background-color:white;color:black','Utiliser',None,None)
    btn_utiliser.setToolTip("Utiliser comme graphe actuelle")
    note_table_db=frame_tableau_bd.newLabel(200,60,200,30,'font-size:15px;color:white;','',True)
    table_historique_graphe=QTableWidget(frame_tableau_bd)
    table_historique_graphe.setGeometry(10,100,580,495)
    table_historique_graphe.setColumnCount(6)
    table_historique_graphe.setHorizontalHeaderLabels(["Date","Hour","Oriénter","Pondére","V","E"])
    return frame_tableau_bd,input_id,btn_recherche,btn_delete,btn_utiliser,table_historique_graphe,note_table_db


