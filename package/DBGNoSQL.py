from pymongo import MongoClient
class DBG(MongoClient):
    """
    Connexion à une base de données MongoDB.

    Cette classe hérite de la classe `pymongo.MongoClient` et ajoute des méthodes pour insérer, sélectionner et supprimer des enregistrements dans une collection spécifique de la base de données.

    Args:
        database (str): Le nom de la base de données.

    Attributes:
        _db (pymongo.database.Database): L'objet de base de données MongoDB.

    Methods:
        __init__(self, database: str) -> None:
            Initialise une nouvelle connexion à la base de données spécifiée.

        insert(self, date: str, heur: str, orienter: str, pondere: str, sommet: str, arc: str) -> bool:
            Insère un nouveau document dans la collection "graphe".

        selectAll(self) -> list|bool:
            Sélectionne tous les documents de la collection "graphe".

        nbrData(self) -> int:
            Récupère le nombre total de documents dans la collection "graphe".

        delete(self, id: int) -> bool:
            Supprime un document spécifié de la collection "graphe".

        deleteAll(self) -> bool:
            Supprime tous les documents de la collection "graphe".
    """
    def __init__(self, database: str) -> None:
        """
        Initialise une nouvelle connexion à la base de données spécifiée.

        Args:
            database (str): Le nom de la base de données.

        Returns:
            None
        """
        super().__init__()
        self._db = self[database]
        self._collection = self._db["graphe"]

    def insert(self, date: str, heur: str, orienter: str, pondere: str, sommet: str, arc: str) -> bool:
        """
        Insère un nouveau document dans la collection "graphe".

        Args:
            date (str): La date du document.
            heur (str): L'heure du document.
            orienter (str): La direction du "graphe".
            pondere (str): La pondération du "graphe".
            sommet (str): Liste des sommets du "graphe".
            arc (str): Liste des arêtes(arcs) du "graphe".

        Returns:
            bool: True si le document a été inséré avec succès, False sinon.
        """
        try:
            self._collection.insert_one({
                "date": date,
                "heur": heur,
                "orienter": orienter,
                "pondere": pondere,
                "sommet": sommet,
                "arc": arc
            })
            return True
        except Exception as e:
            return False

    def selectAll(self) -> list|bool:
        """
        Sélectionne tous les documents de la collection "graphe".

        Returns:
            list: Une liste contenant toutes les valeurs des documents de la collection.
            bool: False si une erreur s'est produite lors de l'exécution de la requête.
        """
        try:
            documents = self._collection.find()
            return list(documents.values())
        except Exception as e:
            return False


    def nbrData(self) -> int:
        """
        Récupère le nombre total de documents dans la collection "graphe".

        Returns:
            int: Le nombre total de documents dans la collection.
            int: -1 si une erreur s'est produite lors de l'exécution de la requête.
        """
        try:
            return self._collection.count_documents({})
        except Exception as e:
            return -1

    def delete(self, id: int) -> bool:
        """
        Supprime le document correspondant à l'ID spécifié de la collection "graphe".

        Args:
            id (int): L'ID du document à supprimer.

        Returns:
            bool: True si le document a été supprimé avec succès, False sinon.
        """
        if id > self.nbrData() or id < 1:
            return False
        else:
            try:
                self._collection.delete_one({"_id": id})
                return True
            except Exception as e:
                return False

    def deleteAll(self) -> bool:
        """
        Supprime tous les documents de la collection "graphe".

        Returns:
            bool: True si tous les documents ont été supprimés avec succès, False sinon.
        """
        try:
            self._collection.delete_many({})
            return True
        except Exception as e:
            return False