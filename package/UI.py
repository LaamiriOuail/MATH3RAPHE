import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from functools import partial
import networkx as nx
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
# import Graphe
class Window(QWidget):
    """
    Classe représentant la fenêtre principale de l'application.
    
    Args:
        wwith (int): La largeur de la fenêtre.
        
        wheigth (int): La hauteur de la fenêtre.
        
        title (str): Le titre de la fenêtre.
        
        iconImage (str|None): Le chemin vers l'image à utiliser pour l'icône de la fenêtre. None si pas d'image.
        
        bakgroundImage (str|None): Le chemin vers l'image à utiliser pour l'arrière-plan de la fenêtre. None si pas d'image.
        
        styleCSS (str|None): Chaîne de style CSS ou None s'il n'y en a pas.
        
        fixedSize (bool|int): Si la fenêtre doit être de taille fixe. True ou 1 si oui, False ou 0 si non.
        
        opacity (float|None): L'opacité de la fenêtre. None si pas d'opacité.
    
    Methods:
        newFram: Crée une nouvelle instance de la classe Fram et la retourne.
        
        keyPressEvent: Méthode de gestionnaire d'événements qui est appelée lorsque l'utilisateur appuie sur la touche "Entrée".
        
        center: Centre la fenêtre sur l'écran.

    """
    def __init__(self,wwith:int,wheigth:int,title:str,iconImage:str|None,bakgroundImage:str|None,styleCSS:str|None,fixedSize:bool|int,opacity:float|None):
        """
        Initialise une nouvelle instance de la classe Window.

        Args:
            wwith (int): La largeur de la fenêtre.
            
            wheigth (int): La hauteur de la fenêtre.
            
            title (str): Le titre de la fenêtre.
            
            iconImage (str|None): Le chemin vers l'image à utiliser pour l'icône de la fenêtre. None si pas d'image.
            
            bakgroundImage (str|None): Le chemin vers l'image à utiliser pour l'arrière-plan de la fenêtre. None si pas d'image.
            
            styleCSS (str|None): Chaîne de style CSS ou None s'il n'y en a pas.
            
            fixedSize (bool|int): Si la fenêtre doit être de taille fixe. True ou 1 si oui, False ou 0 si non.
            
            opacity (float|None): L'opacité de la fenêtre. None si pas d'opacité.

        Returns:
            None
        """
        super().__init__()
        if fixedSize==True or fixedSize==1 : 
            self.setFixedSize(wwith,wheigth)
            #self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinMaxButtonsHint)
            self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint)
        else:
            self.resize(wwith,wheigth)
        if opacity!=None :
            self.setWindowOpacity(opacity)
        if styleCSS!=None:
            self.setStyleSheet(styleCSS)
        self.setWindowTitle(title)
        if iconImage!=None:
            self.setWindowIcon(QIcon(iconImage))
        if bakgroundImage!=None:
            label = QLabel(self)
            pixmap = QPixmap(bakgroundImage).scaled(wwith,wheigth)
            label.setPixmap(pixmap)
        self.center()
    def center(self):
        """
        Centre la fenêtre sur l'écran.
        
        Returns:
            None
        """
        screen_size = QDesktopWidget().screenGeometry(-1)
        center_x = (screen_size.width() - self.width()) / 2
        center_y = (screen_size.height() - self.height()) / 2
        self.move(int(center_x), int(center_y))
    def newFram(self,left:int,top:int,wwidth:int,wheigth:int,bakgroundImage:str|None,styleCSS:str|None):
        """
        Crée un nouveau cadre (Fram) dans la fenêtre.
        
        Args:
            left (int): La position horizontale du cadre en pixels.
            
            top (int): La position verticale du cadre en pixels.
            
            wwidth (int): La largeur du cadre en pixels.
            
            wheigth (int): La hauteur du cadre en pixels.
            
            bakgroundImage (str | None): Le chemin d'accès à l'image de fond du cadre.
            
            styleCSS (str | None): Chaîne de style CSS ou None s'il n'y en a pas.
            
        Returns:
            Fram: L'objet créé pour le cadre.

        """
        name=Fram(self,left,top,wwidth,wheigth,bakgroundImage,styleCSS)
        return name
    def keyPressEvent(self, event):
        """Gère l'événement de pression de touche du clavier.
        Cette méthode est appelée chaque fois qu'une touche du clavier est pressée alors que la 
        fenêtre a le focus.
        
        Args:
            event (QEvent): L'événement de pression de touche du clavier.
            
        Returns:
            Aucune valeur de retour.
        """
        # Si la touche Entrée est pressée, passer au champ QLineEdit suivant
        if event.key() == 16777220:  # 16777220 correspond à la touche "Entrée"
            focus = self.focusWidget()
            if focus is not None and isinstance(focus, QLineEdit):
                self.focusNextChild()
class Fram(QFrame):
    """
    Classe Frame personnalisée basée sur QFrame qui peut contenir des widgets et qui prend en charge la personnalisation 
    de la feuille de style CSS, la création de boutons, de libellés et d'entrées de texte avec des propriétés spécifiques.

    Args:
        window (Union[Window, QWidget]): Une référence à la fenêtre parente.
        
        left (int): La position horizontale du cadre par rapport à la fenêtre parente.
        
        top (int): La position verticale du cadre par rapport à la fenêtre parente.
        
        width (int): La largeur du cadre.
        
        height (int): La hauteur du cadre.
        
        background_image (str|None): Le chemin d'accès de l'image d'arrière-plan du cadre. None par défaut.
         
        style_css (str|None): Les styles CSS à appliquer au cadre. None par défaut.
        

    Methods:
        __init__(self, window: Union[Window, QWidget], left: int, top: int, width: int, height: int, background_image: Optional[str] = None, style_css: Optional[str] = None) -> None:
            Initialise une instance de la classe Frame.

        newButton(self, left: int, top: int, width: int, height: int, styleCSS: str, hoverStyleCss: str, title: str, icon: str, event: Optional[Callable[..., Any]] = None) -> QPushButton:
            Crée et retourne un bouton avec des styles CSS et des actions personnalisées.

        newLabel(self, left: int, top: int, width: int, height: int, styleCSS: str, titleHTML: str, textCenter: Union[bool, int]) -> QLabel:
            Créer et retourne un QLabel avec des propriétés spécifiques.

        newInput(self, left: int, top: int, width: int, height: int, style: str, placeholder: str, textCenter: Union[bool, int], passwordInput: Union[bool, int]) -> QLineEdit:
            Créer et retourne un QLineEdit avec des propriétés spécifiques.
            
        newComboBox(self, left: int, top: int, iwith: int, iheight: int, firstItem: str, styleCSS: str, hoverStyleCss: str) -> QComboBox:
            Crée et retourne un nouveau QComboBox.
        
        newFram(self, left: int, top: int, wwith: int, wheigth: int, backgroundImage: str, styleCSS: str) -> QFrame:
            Crée un nouveau QFrame avec les propriétés spécifiées.
            
        newLogo(self, left: int, top: int, wwith: int, wheigth: int, icon: str) -> QLabel:
            Crée et retourne un nouveau QLabel avec une icône spécifiée.
            
        closeFrame(self) -> bool:
            Ferme la fenêtre Frame.

        showFrame(self) -> None:
            Affiche la fenêtre Frame.

        newTable(self, left:int, top:int, lwith:int, lheigth:int, styleCSS:str, row:int|None, col:int|None) -> QTableWidget:
            Crée une nouvelle instance de QTableWidget.
    """
    def __init__(self,window:Window|QWidget,left:int,top:int,wwith:int,wheigth:int,bakgroundImage:str|None,styleCSS:str|None):
        """
        Initialise une instance de la classe Fram.
        
        Args:
            window (Union[Window, QWidget]): Une référence à la fenêtre parente.
            left (int): La position horizontale du cadre par rapport à la fenêtre parente.
            top (int): La position verticale du cadre par rapport à la fenêtre parente.
            width (int): La largeur du cadre.
            height (int): La hauteur du cadre.
            background_image (str|None): Le chemin d'accès de l'image d'arrière-plan du cadre. None par défaut. 
            style_css (str|None): Les styles CSS à appliquer au cadre. None par défaut.
        """
        super().__init__(window)
        self.setGeometry(left,top,wwith,wheigth)
        if bakgroundImage!=None:
            label = QLabel(self)
            pixmap = QPixmap(bakgroundImage).scaled(wwith,wheigth)
            label.setPixmap(pixmap)
        if styleCSS!=None:
            self.setStyleSheet(styleCSS)
    def newButton(self,left:int,top:int,lwith:int,lheigth:int,styleCSS:str,hoverStyleCss:str,title:str,icon:str,event)->QPushButton:
        """
        Crée et retourne un bouton avec des styles CSS et des actions personnalisées.
        
        Args:
            left (int): Position horizontale du bouton.
            
            top (int): Position verticale du bouton.
            
            lwith (int): Largeur du bouton.
            
            lheigth (int): Hauteur du bouton.
            
            styleCSS (str): Feuille de style CSS pour le bouton.
            
            hoverStyleCss (str): Feuille de style CSS pour le survol du bouton.
            
            title (str): Titre du bouton.
            
            icon (str): Chemin d'accès à l'icône du bouton.
            
            event (Optional[Callable[..., Any]], optional): Fonction de rappel pour l'action personnalisée du bouton. Defaults to None.
            
        Returns:
            QPushButton: Instance du bouton créé.
        """
        name =QPushButton(title,self)
        name.setStyleSheet(
                          "QPushButton"
                          "{"
                          f'{styleCSS}'
                          "}"
                          "QPushButton::hover"
                          "{"
                          f'{hoverStyleCss}'
                          "}")   
        name.setGeometry(left,top,lwith,lheigth)
        name.setIcon(QIcon(icon))
        if  event!=None and event!=False:
            name.clicked.connect(event) 
        """
        in function with Parameter :
        from functools import partial
        event=partial(nameFunction,parametre1=...,parametre2=...,...) 
        or event=partial(nameFunction,value1,value2,...) avec parametre1=value1,parametre2=value2,...
        """
        return name
    def newLabel(self,left:int,top:int,lwith:int,lheight:int,styleCSS:str,titleHTML:str,textCenter:bool|int)->QLabel:
        """
        Créer et retourne un QLabel avec des propriétés spécifiques.
        
        Args:
            left (int): la position horizontale du coin supérieur gauche du QLabel.
            
            top (int): la position verticale du coin supérieur gauche du QLabel.
            
            lwith (int): la largeur du QLabel.
            
            lheight (int): la hauteur du QLabel.
            
            styleCSS (str): les propriétés CSS à appliquer au QLabel.
            
            titleHTML (str): le texte HTML à afficher dans le QLabel.
            
            textCenter (bool|int): si True ou 1, le texte est centré dans le QLabel.
            
        Returns:
            QLabel: le QLabel créé.
        """
        name =QLabel(titleHTML,self)
        name.setGeometry(left,top,lwith,lheight)
        name.setStyleSheet(styleCSS)
        if textCenter==True or textCenter==1 :
           name.setAlignment(Qt.AlignCenter) 
        return name
    def newInput(self,left:int,top:int,iwith:int,iheight:int,style:str,placeholder:str,textCenter:bool|int,passwordInput:bool|int)->QLineEdit:
        """
        Créer et retourne un QLineEdit avec des propriétés spécifiques.
        
        Args:
            left (int): la position horizontale du coin supérieur gauche du QLineEdit.
            
            top (int): la position verticale du coin supérieur gauche du QLineEdit.
            
            iwith (int): la largeur du QLineEdit.
            
            iheight (int): la hauteur du QLineEdit.
            
            style (str): les propriétés CSS à appliquer au QLineEdit.
            
            placeholder (str): le texte à afficher dans le QLineEdit tant que l'utilisateur n'a pas entré de valeur.
            
            textCenter (bool|int): si True ou 1, le texte est centré dans le QLineEdit.
            
            passwordInput (bool|int): si True ou 1, le QLineEdit est affiché comme champ de saisie de mot de passe.
            
        Returns:
            QLineEdit: le QLineEdit créé.

        """
        name = QLineEdit(self)
        name.setPlaceholderText(placeholder)
        name.setStyleSheet(style)
        name.setGeometry(left,top,iwith,iheight)
        if textCenter==True or textCenter==1 :
           name.setAlignment(Qt.AlignCenter)
        if passwordInput==True or passwordInput==1:
            name.setEchoMode(QLineEdit.Password)
        return name
    def newComboBox(self,left:int,top:int,iwith:int,iheight:int,firstItem:str,styleCSS:str,hoverStyleCss:str)->QComboBox:
        """
        Crée et retourne un nouveau QComboBox.
        
        Args:
            left (int): La position X du coin supérieur gauche de la liste déroulante.
            
            top (int): La position Y du coin supérieur gauche de la liste déroulante.
            
            iwith (int): La largeur de la liste déroulante.
            
            iheight (int): La hauteur de la liste déroulante.
            
            firstItem (str): Le premier élément de la liste déroulante.
            
            styleCSS (str): La feuille de style CSS appliquée à la liste déroulante.
            
            hoverStyleCss (str): La feuille de style CSS appliquée à la liste déroulante lorsqu'elle est survolée.
            
        Returns:
            QComboBox: Le nouveau QComboBox créé.
        """
        name=QComboBox(self)
        name.addItem(firstItem)
        name.setStyleSheet(
                          "QComboBox"
                          "{"
                          f'{styleCSS}'
                          "}"
                          "QComboBox::hover"
                          "{"
                          f'{hoverStyleCss}'
                          "}")  
        name.setGeometry(left,top,iwith,iheight)
        return name
    def newFram(self,left:int,top:int,wwith:int,wheigth:int,bakgroundImage:str,styleCSS:str)->QFrame:
        """
        Crée un nouveau QFrame avec les propriétés spécifiées.
        
        Args:
            left (int): La position horizontale du coin supérieur gauche du QFrame.
            
            top (int): La position verticale du coin supérieur gauche du QFrame.
            
            wwith (int): La largeur du QFrame.
            
            wheigth (int): La hauteur du QFrame.
            
            backgroundImage (str): Le chemin de l'image de fond à utiliser pour le QFrame.
            
            styleCSS (str): La feuille de style CSS à utiliser pour le QFrame.
            
        Returns:
            QFrame: Un nouveau QFrame avec les propriétés spécifiées.
        """
        name=Fram(self,left,top,wwith,wheigth,bakgroundImage,styleCSS)
        return name
    def newLogo(self,left,top,wwith,wheigth,icon)->QLabel:
        """ 
        Crée et retourne un nouveau QLabel avec une icône spécifiée.
        
        Args:
        
            left (int): La position horizontale du coin supérieur gauche du QLabel.
            
            top (int): La position verticale du coin supérieur gauche du QLabel.
            
            wwith (int): La largeur du QLabel.
            
            wheigth (int): La hauteur du QLabel.
            
            icon (str): Le chemin de l'image de fond à utiliser pour le QLabel.
                        
        Returns:
        
            QLabel: Un nouveau QLabel avec les propriétés spécifiées.
        """
        name = QLabel(self)
        name.move(left,top)
        pixmap = QPixmap(icon).scaled(wwith,wheigth)
        name.setPixmap(pixmap)
        return name
    def closeFrame(self)->bool:
        """Ferme la fenêtre Frame.
        
        Returns:
            bool: True si la fenêtre est fermée, False sinon.
        """
        self.close()
    def showFrame(self)->None:
        """Affiche la fenêtre Frame."""
        self.show()
    def newTable(self,left:int,top:int,lwith:int,lheigth:int,styleCSS:str,row:int|None,col:int|None)->QTableWidget:
        """Crée une nouvelle instance de QTableWidget.

        Args:
            left (int): Coordonnée horizontale de la table.
            
            top (int): Coordonnée verticale de la table.
            
            lwith (int): Largeur de la table.
            
            lheigth (int): Hauteur de la table.
            
            styleCSS (str): Chaîne de style CSS à appliquer à la table.
            
            row (int|None): Nombre de lignes de la table. Par défaut None.
            
            col (int|None): Nombre de colonnes de la table. Par défaut None.

        Returns:
            QTableWidget: Nouvelle instance de QTableWidget.
        """
        table=QTableWidget(self)
        table.setGeometry(left,top,lwith,lheigth)
        if row!=None :
            table.setRowCount(row)
        if col!=None :
            table.setColumnCount(col)
        table.setStyleSheet(
                          "QTableWidget"
                          "{"
                          f'{styleCSS}'
                          "}"
                          "QTableWidget::item"
                          "{"
                          'padding-left:5px;padding-right:5px;text-align:center;'
                          "}")
        return table
    def newFrameGraphe(self,left:int,top:int,width:int,height:int,graphe:nx.Graph|nx.DiGraph,flag:str,listDijikstra:list|None,grapheHelper:nx.Graph|nx.DiGraph|None=None) -> QFrame:
        """Crée et retourne un nouveau cadre qui contient un graphe dessiné à l'aide de la bibliothèque NetworkX.
        Args:
            left (int): La position en pixels à partir de la gauche de la fenêtre parente où le cadre sera dessiné.
            
            top (int): La position en pixels à partir du haut de la fenêtre parente où le cadre sera dessiné.
            
            width (int): La largeur en pixels du cadre.
            
            height (int): La hauteur en pixels du cadre.
            
            graphe (nx.Graph | nx.DiGraph): Le graphe NetworkX à dessiner. Peut être soit un graphe non-dirigé, soit un graphe dirigé.
            
            flag (str): Un indicateur qui spécifie quelle méthode a été utilisée pour dessiner le graphe. Les valeurs possibles sont : 'graphe', 'prim', 'kruskal', 'dijkstra', 'default'.
            
            listDijikstra (list | None): Une liste optionnelle de nœuds qui seront colorés en vert si la méthode de dessin est 'dijkstra'. Sinon, doit être None.

        Returns:
            QFrame: Un nouveau cadre qui contient le graphe dessiné.

        """
        name=QFrame(self)
        name.setGeometry(left,top,width,height)
        fig = plt.Figure()
        ax = fig.add_subplot(111)
        G=graphe
        H=grapheHelper
        pos = nx.spring_layout(G)
        if flag=='graphe' :
            nx.draw_networkx_nodes(G, pos, ax=ax,node_color="yellow")
            nx.draw_networkx_edges(G, pos, ax=ax)
        elif flag == 'warshall':
            edge_colors=[]
            for i in G.edges():
                if i in H.edges():
                    edge_colors+=["#08052f"]
                else :
                    edge_colors+=["#fd6510"]
            nx.draw_networkx_edges(G, pos,ax=ax, edge_color=edge_colors)
            nx.draw_networkx_nodes(G, pos, ax=ax, node_color="#37a1f0")
        elif flag=='prim':
            nx.draw_networkx_nodes(G, pos, ax=ax,node_color="#03C988")
            nx.draw_networkx_edges(G, pos, ax=ax)
        elif flag=="kruskal":
            nx.draw_networkx_nodes(G, pos, ax=ax,node_color="#CCD5AE")
            nx.draw_networkx_edges(G, pos, ax=ax)
        elif flag=='dijkstra':
            path_edges = [(listDijikstra[i], listDijikstra[i+1]) for i in range(len(listDijikstra)-1)]
            path_subgraph = graphe.edge_subgraph(path_edges)
            node_colors=[]
            for i in G.nodes():
                if i in listDijikstra:
                    node_colors+=["#9DF1DF"]
                else :
                    node_colors+=["#FFEA20"]
            nx.draw_networkx_nodes(G, pos, ax=ax,node_color=node_colors)
            nx.draw_networkx_edges(G, pos, ax=ax)
            nx.draw_networkx_edges(path_subgraph, pos,ax=ax, edge_color="#9DF1DF")
        elif flag=="bellman_ford":
            path_edges = [(listDijikstra[i], listDijikstra[i+1]) for i in range(len(listDijikstra)-1)]
            path_subgraph = graphe.edge_subgraph(path_edges)
            node_colors=[]
            for i in G.nodes():
                if i in listDijikstra:
                    node_colors+=["#e8dc78"]
                else :
                    node_colors+=["#FFEA20"]
            nx.draw_networkx_nodes(G, pos, ax=ax,node_color=node_colors)
            nx.draw_networkx_edges(G, pos, ax=ax)
            nx.draw_networkx_edges(path_subgraph, pos,ax=ax, edge_color="#e8dc78")
        else :
            node_colors =["#FCC2FC"]
            for i in range(G.number_of_nodes()-1):
                node_colors+=["#C9F4AA"]
            nx.draw_networkx_nodes(G, pos, ax=ax,node_color=node_colors)
            nx.draw_networkx_edges(G, pos, ax=ax)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
        nx.draw_networkx_labels(G, pos, ax=ax)
        canvas = FigureCanvas(fig)
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        name.setLayout(layout)
        if flag=='graphe':
            canvas.print_figure('./public/image/graph.png')
        elif flag=='bfs':
            canvas.print_figure('./public/image/graph-bfs.png')
        elif flag=='dfs':
            canvas.print_figure('./public/image/graph-dfs.png')
        elif flag=='dijkstra':
            canvas.print_figure('./public/image/graph-dijkstra.png')
        elif flag=="prim":
            canvas.print_figure('./public/image/graph-prim.png')
        elif flag=="warshall":
            canvas.print_figure('./public/image/graph-warshall.png')
        elif flag=="kruskal":
            canvas.print_figure('./public/image/graph-kruskal.png')
        elif flag=="bellman_ford":
            canvas.print_figure('./public/image/graph-bellman-ford.png')
        return name
    
    


