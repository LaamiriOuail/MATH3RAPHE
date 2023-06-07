import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy
class Graph:
    """
    Classe singleton qui représente un graphe orienté ou non orienté avec ou sans pondération.
    
    Attributes:
        directed (bool): True si le graphe est orienté, False sinon.
        
        pondere (bool): True si le graphe est pondéré, False sinon.
        
        instance (Graph): Instance unique de la classe Graph.
        
        graphe (nx.Graph|nx.DiGraph): Graphe du réseau créé avec la bibliothèque NetworkX.

    Methods:
        get_instance(cls, directed: bool, pondere: bool) -> nx.Graph|nx.DiGraph:
            Crée une instance de la classe Graph s'il n'en existe pas déjà une et la retourne.
        init(self) -> None:
            Réinitialise le graphe.
        add_vertex(self, vertex) -> None:
            Ajoute un sommet au graphe.
        add_edge(self, vertex1: str, vertex2: str) -> None:
            Ajoute une arête non pondérée entre deux sommets au graphe.
        add_edge_value(self, vertex1: str, vertex2: str, value: float) -> None:
            Ajoute une arête pondérée entre deux sommets au graphe.
        get_neighbors(self, vertex: str) -> list:
            Retourne une liste des voisins du sommet donné en argument.
        remove_vertex(self, vertex: str) -> None:
            Retire un sommet du graphe.
        remove_edge(self, vertex1: str, vertex2: str) -> None:
            Retire une arête entre deux sommets du graphe.
        getVertex(self) -> list:
            Retourne une liste des sommets du graphe.
        bfs(self, start: str) -> list:
            Parcours en largeur du graphe à partir du sommet de départ donné en argument.
        dfs(self, start: str) -> list:
            Parcours en profondeur du graphe à partir du sommet de départ donné en argument.
        isDirected(self) -> bool:
            Retourne True si le graphe est orienté, False sinon.
        isPondere(self) -> bool:
            Retourne True si le graphe est pondéré, False sinon.
        isEulerian(self) -> bool:
            Retourne True si le graphe est eulérien, False sinon.
        isPlanaire(self) -> bool:
            Retourne True si le graphe est planaire, False sinon.
        isConnexe(self) -> bool:
            Retourne True si le graphe est connexe, False sinon.
        toDirectedPondere(self) -> None:
            Transforme le graphe en graphe orienté pondéré.
        toUnDirectedPondere(self) -> None:
            Transforme le graphe en graphe non orienté pondéré.
        toDirected(self) -> None:
            Transforme le graphe en graphe orienté non pondéré.
        toUnDirected(self) -> None:
            Transforme le graphe en graphe non orienté non pondéré.
        isVide(self) -> bool:
            Retourne True si le graphe est vide, False sinon

    Raises :
        Exception : Si une deuxième instance de la classe Graph est créée.

    """
    __instance = None
    def __init__(self,directed:bool,pondere:bool)->None:
        """
        Constructeur de la classe Graph.
        
        Args :
        - directed (bool) : True si le graphe est orienté, False sinon.
        - pondere (bool) : True si le graphe est pondéré, False sinon.
        """
        if Graph.__instance is None :
            self.__directed=directed
            self.__pondere=pondere
            if self.__directed:
                self.__graphe = nx.DiGraph()
            else: 
                self.__graphe = nx.Graph() 
            Graph.__instance = self
        else:
            #print("Singleton class can't have more than one instance")
            raise Exception("Singleton class can't have more than one instance,please use get_instance() method")

    @classmethod   
    def get_instance(cls,directed:bool,pondere:bool)->nx.Graph|nx.DiGraph:
        """
        Renvoie l'instance unique de la classe Graph ou crée une nouvelle instance si elle n'existe pas encore.

        Args:
            directed (bool) : True si le graphe est orienté, False sinon.
        
            pondere (bool) : True si le graphe est pondéré, False sinon.

        Returns:
            Graph.__instance : L'instance unique de la classe Graph.
        """
        if Graph.__instance is None :
            Graph(directed,pondere)
        return Graph.__instance 
    def init(self)->None:
        """
            Réinitialise le graphe.
        """
        if self.__directed==True:
            self.__graphe = nx.DiGraph()
        else: 
            self.__graphe = nx.Graph()
    def add_vertex(self, vertex)->None:
        """
            Ajoute un sommet au graphe.
            
            Args:
                vertex (str): Nom du sommet à ajouter.
        """
        self.__graphe.add_node(vertex) 
    def add_edge(self, vertex1:str, vertex2:str)->None:
        """
            Ajoute une arête non pondérée entre deux sommets au graphe.
            
            Args:
                vertex1 (str): Nom du premier sommet.
                
                vertex2 (str): Nom du deuxième sommet.
        """
        self.__graphe.add_edge(vertex1,vertex2)
    def add_edge_value(self, vertex1:str, vertex2:str, value:float)->None:
        """
            Ajoute une arête pondérée entre deux sommets au graphe.
            
            Args:
                vertex1 (str): Nom du premier sommet.
                
                vertex2 (str): Nom du deuxième sommet.
                
                value (float): Poids de l'arête à ajouter.
                
        """
        self.__graphe.add_edge(vertex1,vertex2,weight=float(value)) 
    def add_edge_from(self,edge):
        self.__graphe.add_edges_from(edge)
    def get_neighbors(self, vertex:str)->list:
        """
            Retourne une liste des voisins du sommet donné en argument.
            
            Args:
                vertex (str): Nom du sommet dont on veut connaître les voisins.
            
            Returns:
                list: Liste des noms des voisins du sommet donné en argument.
        """
        return list(self.__graphe.neighbors(vertex))
    def remove_vertex(self, vertex:str):
        """
            Retire un sommet du graphe.
            
            Args:
                vertex (str): Nom du sommet à retirer.
        """
        self.__graphe.remove_node(vertex)
    def remove_edge(self, vertex1:str, vertex2:str):
        """
            Retire une arête entre deux sommets du graphe.
            
            Args:
                vertex1 (str): Nom du premier sommet.
                
                vertex2 (str): Nom du deuxième sommet.
            """
        self.__graphe.remove_edge(vertex1, vertex2)
    def getVertex(self)->list:
        """
            Retourne une liste des sommets du graphe.
            
            Returns:
                list: Liste des noms des sommets du graphe.
        """
        return list(self.__graphe.nodes())
    def bfs(self, start:str):
        """
            Parcours en largeur du graphe à partir du sommet de départ donné en argument.
            
            Args:
                start (str): Nom du sommet de départ.
            
            Returns:
                list: Liste des noms des sommets visités lors du parcours en largeur.
        """
        queue = []
        queue.append(start)
        visited = set()
        visited.add(start)
        bfs_order = []
        while queue:
            node = queue.pop(0)
            bfs_order.append(node)
            for neighbor in self.__graphe.neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return bfs_order
    def dfs(self, start:str):
        """
        Effectue une recherche en profondeur (DFS) à partir du nœud start.

        Args:
            start (str): Le nœud de départ de la recherche en profondeur.

        Returns:
            Une liste de nœuds dans l'ordre où ils ont été visités par la recherche en profondeur.
        """
        stack = []
        stack.append(start)
        visited = set()
        dfs_order = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                dfs_order.append(node)
                for neighbor in self.__graphe.neighbors(node):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return dfs_order

    def isDirected(self)->bool:
        """
        Renvoie True si le graphe est orienté, False sinon.
        """
        return self.__directed
    def isPondere(self)->bool:
        """
        Renvoie True si le graphe est pondéré, False sinon.
        """
        return self.__pondere
    def isEulerian(self)->bool:
        """
        Vérifie si le graphe est eulérien.

        Returns:
            True si le graphe est eulérien, False sinon.
        """
        return nx.is_eulerian(self.__graphe)
    def isPlanaire(self)->bool:
        """
        Vérifie si le graphe est planaire.

        Returns:
            True si le graphe est planaire, False sinon.
        """
        is_planar, embedding = nx.check_planarity(self.__graphe)
        return is_planar
    def isConnexe(self)->bool:
        """
        Vérifie si le graphe est connexe.

        Returns:
            True si le graphe est connexe, False sinon.
        """
        if self.isVide():
            return False
        elif self.__directed:
            return nx.is_strongly_connected(self.__graphe)
            #print("Le graphe est fortement connexe")
        else :
            return nx.is_connected(self.__graphe)
    def toDirectedPondere(self)->None:
        """
        Cette méthode permet de transformer un graphe non orienté et pondéré en graphe orienté et pondéré.
        """
        self.__directed=True
        self.__pondere=True
        self.__graphe = nx.DiGraph()
        Graph.__instance=self
    def toUnDirectedPondere(self)->None:
        """
        Cette méthode permet de transformer un graphe orienté et pondéré en graphe non orienté et pondéré.
        """
        self.__directed=False
        self.__pondere=True
        self.__graphe = nx.Graph()
        Graph.__instance=self
    def toDirected(self)->None:
        """
        Cette méthode permet de transformer un graphe non orienté et non pondéré en graphe orienté et non pondéré.
        """
        self.__directed=True
        self.__pondere=False
        self.__graphe = nx.DiGraph()
        Graph.__instance=self
    def toUnDirected(self)->None:
        """
        Cette méthode permet de transformer un graphe orienté et non pondéré en graphe non orienté et non pondéré.
        """
        self.__directed=False
        self.__pondere=False
        self.__graphe = nx.Graph()
        Graph.__instance=self
    def isVide(self)->bool:
        """
        Cette méthode vérifie si le graphe est vide.

        Returns:
            bool : True si le graphe est vide, False sinon.
        """
        if list(self.__graphe.nodes())==[]:
            return True
        else :
            return False
    def getNetworkxGraph(self)->nx.Graph|nx.DiGraph:
        """
        Cette méthode retourne le graphe sous forme d'un objet Networkx Graph ou DiGraph.

        Returns:
            nx.Graph|nx.DiGraph : le graphe sous forme d'un objet Networkx Graph ou DiGraph.
        """
        return self.__graphe
    def getNombreSommet(self)->int:
        """
        Cette méthode retourne le nombre de sommets dans le graphe.

        Returns:
            int : le nombre de sommets dans le graphe.
        """
        return self.__graphe.number_of_nodes()
    def getNombreArrete(self)->int:
        """
        Retourne le nombre d'arêtes dans le graphe.

        Returns:
            int: Le nombre d'arêtes dans le graphe.
        """
        return self.__graphe.number_of_edges()
    def getDensite(self)->float:
        """
        Calcule la densité du graphe.

        Returns:
            float : La densité du graphe.
        """
        if self.getNombreSommet() == 1 or self.getNombreSommet() == 0:
            d=0.0
        elif self.__directed :
            d=(self.getNombreArrete())/(self.getNombreSommet()*(self.getNombreSommet()-1))
        else :
            d=(2*self.getNombreArrete())/(self.getNombreSommet()*(self.getNombreSommet()-1))
        return d
    def getDegreeSommets(self)->dict:
        """
        Retourne un dictionnaire contenant les degrés de chaque sommet du graphe.

        Returns:
            dict: Dictionnaire contenant les degrés des sommets.
        """
        return dict(self.__graphe.degree())

    def getMatriceAdjacent(self)->list:
        """
        Retourne une liste représentant la matrice d'adjacence du graphe.

        Returns:
            list: Liste représentant la matrice d'adjacence du graphe.
        """
        return nx.to_numpy_array(self.__graphe).tolist()
    def getMatriceIncidence(self)->list:
        """
        Retourne une liste représentant la matrice d'incidence du graphe.

        Returns:
            list: Liste représentant la matrice d'incidence du graphe.
        """
        return nx.incidence_matrix(self.__graphe,oriented=self.__directed).toarray().tolist()
    def getListeSommet(self)->list:
        """
        Retourne une liste contenant tous les sommets du graphe.

        Returns:
            list: Liste contenant tous les sommets du graphe.
        """
        return list(self.__graphe.nodes())
    def getListeArrete(self)->dict:
        """
        Retourne un dictionnaire contenant les arêtes du graphe.

        Returns:
            dict: Dictionnaire contenant les arêtes du graphe.
        """
        if self.__pondere:
            return self.__graphe.edges.data("weight")
        else :
            return self.__graphe.edges()
    def getBfsGraphe(self,source:str)->nx.DiGraph:
        """
        Retourne l'arbre de parcours en largeur (BFS) à partir du sommet source.

        Args:
            source (str): Le sommet source pour le parcours en largeur.

        Returns:
            nx.DiGraph: L'arbre de parcours en largeur à partir du sommet source.
        """
        return nx.bfs_tree(self.__graphe, source=source)
    def getDfsGraphe(self,source:str)->nx.DiGraph:
        """
        Retourne l'arbre de parcours en profondeur (DFS) à partir du sommet source.

        Args:
            source (str): Le sommet source pour le parcours en profondeur.

        Returns:
            nx.DiGraph: L'arbre de parcours en profondeur à partir du sommet source.
        """
        return nx.dfs_tree(self.__graphe, source=source)
    # def updateGraphePDF(self,source:str|None):
    #     def updatePhotoGraphe(G,flag,path):
    #         fig = plt.Figure()
    #         ax = fig.add_subplot(111)
    #         pos = nx.spring_layout(G)
    #         if flag=='graphe':
    #             nx.draw_networkx_nodes(G, pos,node_color="yellow")
    #         else :
    #             node_colors =["green"]
    #             for i in range(G.number_of_nodes()-1):
    #                 node_colors+=["yellow"]
    #             nx.draw_networkx_nodes(G, pos,node_color=node_colors)
    #         edge_labels = nx.get_edge_attributes(G, 'weight')
    #         nx.draw_networkx_edges(G, pos)
    #         nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    #         nx.draw_networkx_labels(G, pos)
    #         canvas = FigureCanvas(fig)
    #         layout = QVBoxLayout()
    #         layout.addWidget(canvas)
    #         canvas.print_figure(path)
    #     updatePhotoGraphe(self.getNetworkxGraph(),'graphe',"./graphe-pdf/graph.png")
    #     if source !=None :
    #         updatePhotoGraphe(self.getBfsGraphe(source),'bfs',"./graphe-pdf/bfs-graph.png")
    #         updatePhotoGraphe(self.getDfsGraphe(source),'dfs',"./graphe-pdf/dfs-graph.png")
    def getPrimGraphe(self,source:str):
        """
        Retourne l'arbre de poids minimum (MST) du sous-graphe connexe de self.__graphe contenant le nœud source.

        Args:
            source (str) : Le nom du nœud de départ.

        Returns:
            mst (nx.Graph) : L'arbre de poids minimum (MST) du sous-graphe connexe de self.__graphe contenant le nœud source.
        """
        start_node = source
        subgraph = self.__graphe.subgraph(nx.node_connected_component(self.__graphe, start_node))
        mst = nx.minimum_spanning_tree(subgraph)
        return mst
    def getKruskalGraphe(self,source:str):
        """
        Retourne l'arbre de poids minimum (MST) du sous-graphe connexe de self.__graphe contenant le nœud source, calculé en utilisant l'algorithme de Kruskal.

        Args:
            source (str) : Le nom du nœud de départ.

        Returns:
            mst (nx.Graph) : L'arbre de poids minimum (MST) du sous-graphe connexe de self.__graphe contenant le nœud source, calculé en utilisant l'algorithme de Kruskal.
        """
        start_node = source
        subgraph = self.__graphe.subgraph(nx.node_connected_component(self.__graphe, start_node))
        mst = nx.minimum_spanning_tree(subgraph,algorithm='kruskal')
        return mst
    # def getFloydWarshall(self):
    #     """
    #     Retourne un dictionnaire contenant la matrice des distances de Floyd-Warshall pour self.__graphe.

    #     Returns:
    #         distances (dict) : Un dictionnaire contenant la matrice des distances de Floyd-Warshall pour self.__graphe.
    #     """
    #     distances = nx.floyd_warshall(self.__graphe)
    #     return distances
    def getVideGraphe(self)->nx.Graph:
        """
        Retourne un graphe vide.

        Returns:
            nx.Graph : Un graphe vide.
        """
        return nx.Graph()
    def getListeDijkstra(self,source:str,pointFinal:str)->list:
        """
        Retourne une liste contenant le chemin le plus court entre la source et le point final
        en utilisant l'algorithme de Dijkstra.

        Args:
            source (str) : Le nœud source du chemin.
        
            pointFinal (str) : Le nœud final du chemin.

        Returns:
            list : La liste contenant le chemin le plus court.
        """
        return list(nx.dijkstra_path(self.__graphe,source, pointFinal))
    def getListeBellmanFord(self,source:str,pointFinal:str)->list:
        return list(nx.bellman_ford_path(self.__graphe, source, pointFinal))
    def getWarshallGraphe(self)->nx.DiGraph:
        return nx.transitive_closure(self.__graphe)
    def isAllPositive(self)->bool:
        if self.__pondere :
            all_positive=True
            for u, v, weight in self.__graphe.edges(data='weight'):
                if weight < 0:
                    all_positive = False
                    break
            return all_positive
        else :
            return False
    def afficher_graphe(self,graphe,flag="graphe",listDijikstra=None,grapheHelper=None):
        plt.close()
        G=graphe
        H=grapheHelper
        pos = nx.spring_layout(G)
        if flag=='graphe' :
            nx.draw_networkx_nodes(G, pos,node_color="yellow")
            nx.draw_networkx_edges(G, pos)
        elif flag == 'warshall':
            edge_colors=[]
            for i in G.edges():
                if i in H.edges():
                    edge_colors+=["#08052f"]
                else :
                    edge_colors+=["#fd6510"]
            nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
            nx.draw_networkx_nodes(G, pos, node_color="#37a1f0")
        elif flag=='prim':
            nx.draw_networkx_nodes(G, pos,node_color="#03C988")
            nx.draw_networkx_edges(G, pos)
        elif flag=="kruskal":
            nx.draw_networkx_nodes(G, pos,node_color="#CCD5AE")
            nx.draw_networkx_edges(G, pos)
        elif flag=='dijkstra':
            path_edges = [(listDijikstra[i], listDijikstra[i+1]) for i in range(len(listDijikstra)-1)]
            path_subgraph = graphe.edge_subgraph(path_edges)
            node_colors=[]
            for i in G.nodes():
                if i in listDijikstra:
                    node_colors+=["#9DF1DF"]
                else :
                    node_colors+=["#FFEA20"]
            nx.draw_networkx_nodes(G, pos,node_color=node_colors)
            nx.draw_networkx_edges(G, pos)
            nx.draw_networkx_edges(path_subgraph, pos, edge_color="#9DF1DF")
        elif flag=="bellman_ford":
            path_edges = [(listDijikstra[i], listDijikstra[i+1]) for i in range(len(listDijikstra)-1)]
            path_subgraph = graphe.edge_subgraph(path_edges)
            node_colors=[]
            for i in G.nodes():
                if i in listDijikstra:
                    node_colors+=["#e8dc78"]
                else :
                    node_colors+=["#FFEA20"]
            nx.draw_networkx_nodes(G, pos,node_color=node_colors)
            nx.draw_networkx_edges(G, pos)
            nx.draw_networkx_edges(path_subgraph, pos, edge_color="#e8dc78")
        else :
            node_colors =["#FCC2FC"]
            for i in range(G.number_of_nodes()-1):
                node_colors+=["#C9F4AA"]
            nx.draw_networkx_nodes(G, pos,node_color=node_colors)
            nx.draw_networkx_edges(G, pos)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        nx.draw_networkx_labels(G, pos)
        plt.show()
    def getGraphe(self):
        return self.__graphe



        

