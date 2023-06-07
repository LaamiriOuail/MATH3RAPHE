from PyQt5.QtWidgets import QLineEdit

def EdgeComponent(container):
    """
    Créer les composants pour ajouter ou supprimer une arête dans un graphe.

    Args:
        container: le conteneur où les composants seront ajoutés.

    Returns:
        
        Un tuple contenant :
        
        le cadre principal contenant tous les autres cadres et composants
        
        le cadre pour l'affichage du graphe (vide pour l'instant)
        
        le cadre pour l'ajout ou la suppression d'une arête
        
        la liste déroulante pour sélectionner le type de graphe
        
        le champ d'entrée pour le sommet de départ
        
        le champ d'entrée pour le sommet d'arrivée
        
        le libellé pour le poids de l'arête
        
        le champ d'entrée pour le poids de l'arête
        
        le bouton pour ajouter une arête
        
        le bouton pour supprimer une arête
        
        le bouton pour réinitialiser le graphe
        
        le bouton pour enregistrer le graphe
        
        le libellé pour afficher un message après l'ajout ou la suppression d'une arête.
    """
    frame_graphe_manipulation=container.newFram(200,300,600,300,'','background-color:none;')
    # frame_graphe_rep_nx=frame_graphe_manipulation.newFram(0,0,300,300,None,None)
    frame_add_del_edge=frame_graphe_manipulation.newFram(150,10,300,300,'','background-color:none;')
    input_sommet_depart=frame_add_del_edge.newInput(130,65,130,20,'','',True,None)
    sommet_depart=frame_add_del_edge.newLabel(0,50,130,50,'font-size:15px;','Sommet de depart',False)
    sommet_arriver=frame_add_del_edge.newLabel(0,75,130,50,'font-size:15px;','Sommet d\'arrive',False)
    input_sommet_arriver=frame_add_del_edge.newInput(130,93,130,20,'','',True,None)
    poids_arrete=frame_add_del_edge.newLabel(0,100,130,50,'font-size:15px;','Poids',False)
    poids_arrete.setEnabled(False)
    input_poids_arrete=frame_add_del_edge.newInput(130,118,130,20,'','',True,None)
    input_poids_arrete.setEnabled(False)
    ajouter_arrete=frame_add_del_edge.newButton(20,150,100,20,'background-color:white;color:black','background-color:black;color:white','Ajouter',None,None)
    supprimer_arrete=frame_add_del_edge.newButton(180,150,100,20,'background-color:black;color:white','background-color:white;color:black','Supprimer',None,None)
    initialiser_graphe=frame_add_del_edge.newButton(20,170,100,20,'background-color:black;color:white','background-color:white;color:black','Initialiser',None,None)
    enregistrer_graphe=frame_add_del_edge.newButton(180,170,100,20,'background-color:white;color:black','background-color:black;color:white','Enregistrer',None,None)
    note_ajouter_edge =frame_add_del_edge.newLabel(5,200,275,30,'color:white;font-size:12px;','',True)
    type_graphe=frame_add_del_edge.newComboBox(0,0,150,25,'Non-orientés','background-color:black;color:white;','')
    type_graphe.addItem('Orientés')
    type_graphe.addItem('Non-orientés pondérés')
    type_graphe.addItem('Orientés pondérés')
    return frame_graphe_manipulation,frame_add_del_edge,type_graphe,input_sommet_depart,input_sommet_arriver,poids_arrete,input_poids_arrete,ajouter_arrete,supprimer_arrete,initialiser_graphe,enregistrer_graphe,note_ajouter_edge