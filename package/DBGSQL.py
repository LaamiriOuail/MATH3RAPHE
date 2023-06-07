import sqlite3
from pymongo import MongoClient
class DBG(sqlite3.Connection):
    """
    Connexion à une base de données SQLite.

    Cette classe hérite de la classe `sqlite3.Connection` et ajoute des méthodes pour insérer, sélectionner et supprimer des enregistrements dans une table spécifique de la base de données.

    Args:
        database (str): Le nom de la base de données.

    Attributes:
        _dataBase (str): Le chemin vers la base de données.

    Methods:
        __init__(self, database: str) -> None:
            Initialise une nouvelle connexion à la base de données spécifiée.

        insert(self, date: str, heur: str, orienter: str, pondere: str, sommet: str, arc: str) -> bool:
            Insère un nouveau enregistrement dans la table "graphe".

        selectAll(self) -> list|bool:
            Sélectionne tous les enregistrements de la table "graphe".

        nbrData(self) -> int:
            Récupère le nombre total d'enregistrements dans la table "graphe".

        delete(self, id: int) -> bool:
            Supprime un enregistrement spécifié de la table "graphe".

        deleteAll(self) -> bool:
            Supprime tous les enregistrements de la table "graphe".

       
    """
    def __init__(self, database:str)->None:
        """
        Initialise une nouvelle connexion à la base de données spécifiée.

        Args:
            database (str): Le nom de la base de données.

        Returns:
        None
        """
        dataBase =f".\\models\\{database}.db"
        self._dataBase=dataBase
        super().__init__(dataBase)
        self.execute(f'CREATE TABLE IF NOT EXISTS {database} (id INTEGER PRIMARY KEY AUTOINCREMENT , date TEXT , heur TEXT,orienter TEXT,pondere TEXT,Sommet Text,arc TEXT)')
    def insert(self, date:str,heur:str,orienter:str,pondere:str,sommet:str,arc:str)->bool:
        """
        Insère un nouveau enregistrement dans la table "graphe".

        Args:
            date (str): La date de l'enregistrement.
            
            heur (str): L'heure de l'enregistrement.
            
            orienter (str): La direction de "graphe".
            
            pondere (str): La pondération de "graphe".
            
            sommet (str): Liste des sommets de "graphe".
            
            arc (str): Liste des arretes(arcs) de "graphe".

        Returns:
            bool: True si l'enregistrement a été inséré avec succès, False sinon.
        """
        try:
            self.execute(f'INSERT INTO graphe(date,heur,orienter,pondere,sommet,arc) VALUES (?,?,?,?,?,?)', (date,heur,orienter,pondere,sommet,arc))
            self.commit()
            return True
        except Exception as e :
            return False
    def selectAll(self)->list|bool:
        """
        Sélectionne tous les enregistrements de la table "graphe".

        Returns:
            list: Une liste contenant tous les enregistrements de la table.
            
            bool: False si une erreur s'est produite lors de l'exécution de la requête.
        """
        try:
            cursor = self.execute(f'SELECT date,heur,orienter,pondere,sommet,arc FROM graphe')
            return cursor.fetchall()
        except Exception as e :
            return False
    def nbrData(self)->int:
        """
        Récupère le nombre total d'enregistrements dans la table "graphe".

        Returns:
            int: Le nombre total d'enregistrements dans la table.
            
            int: -1 si une erreur s'est produite lors de l'exécution de la requête.
        """
        try:
            cursor = self.execute(f'SELECT COUNT(*) FROM graphe')
            result = cursor.fetchone()
            num_rows = result[0]
            return num_rows
        except Exception as e:
            return -1
    def delete(self, id:int)->bool:
        """
        Supprime l'enregistrement correspondant à l'ID spécifié de la table "graphe".
        
        Args:
            id (int): L'ID de l'enregistrement à supprimer.

        Returns:
            bool: True si l'enregistrement a été supprimé avec succès, False sinon.
        """
        if id>self.nbrData() or id<1:
            return False
        else:
            try:
                self.execute(f'DELETE FROM graphe WHERE id = ?', (id,))
                self.execute(f'UPDATE graphe SET id = id - 1 WHERE id > ?', (id,))
                self.commit()
                return True
            except Exception as e :
                return False
    def deleteAll(self)->bool:
        """
        Supprime tous les enregistrements de la table "graphe".

        Returns:
            bool: True si tous les enregistrements ont été supprimés avec succès, False sinon.
        """
        try:
            self.execute(f'DELETE FROM graphe')
            self.execute(f'UPDATE sqlite_sequence SET seq = 0 WHERE name = "graphe"')
            self.commit()
            return True
        except Exception as e:
            return False
    




