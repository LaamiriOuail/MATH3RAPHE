
def bareChoix(container):
    """
    Cette fonction crée un conteneur avec des boutons pour choisir parmi différentes fonctions.
    
    Args:
        container: Le conteneur parent dans lequel placer le conteneur de cette component.

    Returns:
        Une liste de boutons, chacun avec une fonctionnalité différente.
    """
    bare_left_algorithm=container.newFram(0,0,200,600,'','background-color:black;')
    btn_home=bare_left_algorithm.newButton(0,0,200,40,"background-color:white;color:black;font-size:15px","background-color:black;color:white","Home","",None)
    btn_historique=bare_left_algorithm.newButton(0,40,200,40,"background-color:white;color:black;font-size:15px","background-color:black;color:white","Historique","",None)
    btn_genere_pdf=bare_left_algorithm.newButton(0,80,200,40,"background-color:white;color:black;font-size:15px","background-color:black;color:white","PDF associe","",None)    
    btn_graphe_manipulation=bare_left_algorithm.newButton(0,120,200,40,"background-color:white;color:black;font-size:15px","background-color:black;color:white","Operation sur graphe","",None)
    btn_info_graphe=bare_left_algorithm.newButton(0,160,200,40,"background-color:white;color:black;font-size:15px","background-color:black;color:white","Information du graphe","",None)
    btn_matrix=bare_left_algorithm.newButton(0,200,200,40,"background-color:white;color:black;font-size:15px","background-color:black;color:white","Matrice associé","",None)
    btn_bfs=bare_left_algorithm.newButton(0,240,200,40,"background-color:white;color:black;font-size:15px","background-color:black;color:white","parcours en largeur(BFS)","",None)
    btn_dfs=bare_left_algorithm.newButton(0,280,200,40,"background-color:white;color:black;font-size:15px","background-color:black;color:white","parcours en profondeur(DFS)","",None)
    btn_prime=bare_left_algorithm.newButton(0,320,200,40,"background-color:white;color:black;font-size:15px","background-color:black;color:white","Prime","",None)
    btn_kruskal=bare_left_algorithm.newButton(0,360,200,40,"background-color:white;color:black;font-size:15px","background-color:black;color:white","kruskal","",None)
    btn_dijkstra=bare_left_algorithm.newButton(0,400,200,40,"background-color:white;color:black;font-size:15px","background-color:black;color:white","Dijkstra","",None)
    btn_bellman_ford=bare_left_algorithm.newButton(0,440,200,40,"background-color:white;color:black;font-size:15px","background-color:black;color:white","Bellman-Ford-Moore","",None)
    btn_warshall=bare_left_algorithm.newButton(0,480,200,40,"background-color:white;color:black;font-size:15px","background-color:black;color:white","Floyd-Warshall","",None)
    btn_ford_fulkeson=bare_left_algorithm.newButton(0,520,200,40,"background-color:white;color:black;font-size:15px","background-color:black;color:white","Ford-Fulkeson","",None)
    btn_welch_powell=bare_left_algorithm.newButton(0,560,200,40,"background-color:white;color:black;font-size:15px","background-color:black;color:white","Welch-Powell","",None)
    return btn_home,btn_historique,btn_info_graphe,btn_bfs,btn_dfs,btn_dijkstra,btn_prime,btn_kruskal,btn_matrix,btn_warshall,btn_graphe_manipulation,btn_genere_pdf,btn_bellman_ford
    
    
    