

def infoComponent(container):
    """
    Crée et retourne un conteneur d'informations sur un graphe ainsi que des labels pour afficher les informations.

    Args:
        container (QWidget): Le conteneur dans lequel les informations doivent être créées.

    Returns:
        tuple: Un tuple contenant le conteneur créé et les labels pour afficher les informations sur le graphe.

    """
    right_buttom=container.newFram(200,300,600,300,'','background-color:None;font-size:7px;')
    graphe_info_label=right_buttom.newLabel(0,0,600,30,'font-size:15px;color:blue;','Information sur le graphe',True)
    degre_nodes=right_buttom.newTable(200,30,395,70,"font-size:20px;",1,None)
    is_directed=right_buttom.newLabel(5,0,150,30,'font-size:15px;','',False)
    is_weighted=right_buttom.newLabel(5,30,150,30,'font-size:15px;','',False)
    number_of_nodes=right_buttom.newLabel(5,60,300,30,'font-size:15px;','',False)
    liste_nodes =right_buttom.newLabel(5,120,600,30,'font-size:15px;','',False)
    number_of_edges=right_buttom.newLabel(5,90,300,30,'font-size:15px;','',False)
    liste_edges=right_buttom.newLabel(5,150,600,30,'font-size:15px;','',False)
    density=right_buttom.newLabel(5,180,200,30,'font-size:15px;','',False)
    is_eulerian=right_buttom.newLabel(200,180,400,30,'font-size:15px;','',False)
    is_planaire=right_buttom.newLabel(0,210,300,30,'font-size:15px;','',False)
    is_connexe=right_buttom.newLabel(300,210,300,30,'font-size:15px;','',False)
    return right_buttom,is_directed,is_weighted,number_of_nodes,liste_nodes,number_of_edges,liste_edges,density,degre_nodes,is_eulerian,is_planaire,is_connexe
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# import networkx as nx

# # créer un graphe non-dirigé
# G = nx.Graph()
# G.add_weighted_edges_from([(0, 1, 3.0), (1, 2, 7.5)])

# # obtenir les informations du graphe
# print("Nombre de nœuds :", nx.number_of_nodes(G))
# print("Nombre d'arêtes :", nx.number_of_edges(G))
# print("Densité :", nx.density(G))
# print("Est-ce que le graphe est dirigé :", nx.is_directed(G))
# print("Degré du nœud 1 :", nx.degree(G, 1))
# print("Degré de tous les nœuds :", dict(nx.degree(G)))
# print("Longueur moyenne des chemins les plus courts :", nx.average_shortest_path_length(G))
# print("Diamètre :", nx.diameter(G))
# print("Excentricités de tous les nœuds :", nx.eccentricity(G))
# adj_matrix = nx.adjacency_matrix(G) # matrice d'adjacence
# print(adj_matrix)
# print(adj_matrix[0,0])
# degree_distribution = nx.degree_histogram(G) # distribution de degré
# print(degree_distribution)

# import sys
# from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

# class Matrix(QTableWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("Matrice")
#         self.setRowCount(4)
#         self.setColumnCount(3)

#         for i in range(4):
#             for j in range(3):
#                 item = QTableWidgetItem()
#                 item.setText("({},{})".format(i, j))
#                 self.setItem(i, j, item)

#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     matrix = Matrix()
#     sys.exit(app.exec_())


