from packages.graph import Graph 
import click
from colorama import init, Fore, Style
import os
import ast         

file_path="graphe.txt"          
def getGraphe():
    if os.path.exists(file_path):
        with open(file_path, "r") as fichier:
            data = fichier.read().strip().split(":")
        if len(data)!=4:
            return None
        else:
            #orientation:ponderation:listArrete:listVertex
            if data[3]!="[]":
                directed=True if data[0]=="True" else False
                pondere=True if data[1]=="True" else False
                graphe=Graph(directed,pondere)
                for i in ast.literal_eval(data[3]):
                    graphe.add_vertex(i)
                for i in ast.literal_eval(data[2]):
                    graphe.add_edge_value(i[0],i[1],i[2]) if graphe.isPondere() else graphe.add_edge(i[0],i[1])
                return graphe
            return Graph(data[0],data[1])
    else:
        return None     
def setGraphe(graphe:Graph):
       with open(file_path, "w") as fichier:
            pondere="True" if graphe.isPondere() else ""
            orienter="True" if graphe.isDirected() else ""
            fichier.write(f"{orienter}:{pondere}:{graphe.getListeArrete()}:{graphe.getListeSommet()}")
            
# click.echo(Fore.GREEN + "Hello, World!" + Style.RESET_ALL)
# click.echo(Fore.RED + "This is an error message." + Style.RESET_ALL)
def message(err,port=1):
    if err=="null":
        click.echo(f"{Fore.RED}Le graphe est null {Style.RESET_ALL} \n{Fore.GREEN}pour plus d'informations lancer la commande  : {Fore.YELLOW}graphe help{Style.RESET_ALL} ")
    elif port==0:
        click.echo(f"{Fore.RED}{err}{Style.RESET_ALL}")
    elif port==1:
        click.echo(f"{Fore.GREEN}{err}{Style.RESET_ALL}")
    elif port==2:
        click.echo(f"{Fore.YELLOW}{err}{Style.RESET_ALL}")
def commande_description(commande:str,description:str)->None:
    click.echo(f"\t{Fore.YELLOW}{commande} {Style.RESET_ALL}: {description}")
@click.group
def cli():
    pass    
@cli.command()
def cls():
    os.system('cls')
@cli.command()
def i():
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else :
        graphe.init()
        setGraphe(graphe)
        message("Le graphe est initialiser")
@cli.command()
def op():
    graphe=getGraphe()
    if graphe==None: 
        graphe=Graph(True,True)
    else:
        graphe.toDirectedPondere()
    setGraphe(graphe)
    message("Le graphe est orienter pondere")
@cli.command()
def o():
    graphe=getGraphe()
    if graphe==None: 
        graphe=Graph(True,False)
    else:
        graphe.toDirected()
    setGraphe(graphe)
    message("Le graphe est orienter")
@cli.command()
def p():
    graphe=getGraphe()
    if graphe==None: 
        graphe=Graph(False,True)
    else:
        graphe.toUnDirectedPondere()
    setGraphe(graphe)
    message("Le graphe est pondere")
@cli.command()
def s():
    graphe=getGraphe()
    if graphe==None: 
        graphe=Graph(False,False)
    else:
        graphe.toUnDirected()
    setGraphe(graphe)
    message("Le graphe est simple")

@cli.command()
@click.argument('vertex',type=str)
def av(vertex):
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else :
        graphe.add_vertex(vertex)
        setGraphe(graphe)
        message(f"La sommet {vertex} est ajouter")

@cli.command()
@click.argument('vertex',type=str)
def dv(vertex):
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else:
        if vertex in graphe.getListeSommet():
            graphe.remove_vertex(vertex)
            setGraphe(graphe)
            message(f"La sommet {vertex} est supprimer")
        else:
            message(f"La sommet {vertex} n'appartient pas au graphe",0)    

@cli.command()
@click.argument('debut',type=str)
@click.argument('fin',type=str)
@click.argument('poids',type=int, default='0')
def ae(debut,fin,poids):
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else :
        if graphe.isPondere():
            if poids!=0:
                graphe.add_edge_value(debut,fin,poids)
                setGraphe(graphe)
                message(f"L'arrete ({debut},{fin},{poids}) est ajouter",1)
            else:
                message(f"Le poids est different de 0",0)
        else:
            graphe.add_edge(debut,fin)
            setGraphe(graphe)
            message(f"L'arrete ({debut},{fin}) est ajouter",1)

@cli.command()
@click.argument('depart',type=str)
@click.argument('fin',type=str)
def de(depart,fin):
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else :
        if depart in graphe.getListeSommet() and fin in graphe.getListeSommet():
            if depart in graphe.get_neighbors(fin):
                graphe.remove_edge(depart,fin)
                setGraphe(graphe)
                message(f"L'arrete ({depart},{fin}) est supprimer",1)
            else:
                message(f"La sommet {depart} et {fin} n'est pas des voisin",2)
        else:
            message("La sommet {depart} ou {fin} n'est pas en graphe",0)
@cli.command()
def v():
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else :
        message(f"L'ensemble des sommet : {graphe.getListeSommet()}",1)
@cli.command()
def e():
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else :
        if graphe.isDirected():
            message(f"L'ensemble des arretes : {graphe.getListeArrete()}",1)
        else:
            message(f"L'ensemble des arcs : {graphe.getListeArrete()}",1)
@cli.command()
def type():
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else :
        if graphe.isPondere() and graphe.isDirected():
            message("Graphe orienter pondere",1)
        elif graphe.isPondere():
            message("Graphe orienter",1)
        elif graphe.isDirected():
            message("Graphe pondere",1)
        else:
            message("Graphe simple",1)
@cli.command()
def show():
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else:
        message("Le graphe est representer ...",1)
        graphe.afficher_graphe(graphe.getGraphe())
@cli.command()
@click.argument('start',type=str)
def bfs(start):
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else:
        if start in graphe.getListeSommet():
            click.echo(f"BFS : {Fore.GREEN}{graphe.bfs(start)}{Style.RESET_ALL}")
            graphe.afficher_graphe(graphe.getBfsGraphe(start),"dfs")
        else :
            click.echo(f"{Fore.RED}La sommet {start} n'appartient pas a le graphe !!{Style.RESET_ALL}")
@cli.command()
@click.argument('start',type=str)
def dfs(start):
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else:
        if start in graphe.getListeSommet():
            click.echo(f"DFS : {Fore.GREEN}{graphe.dfs(start)}{Style.RESET_ALL}")
            graphe.afficher_graphe(graphe.getDfsGraphe(start),"bfs")
        else :
            click.echo(f"{Fore.RED}La sommet {start} n'appartient pas a le graphe !!{Style.RESET_ALL}")
@cli.command()
@click.argument('start',type=str)
def prime(start:str):
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else:
        if graphe.isConnexe() and graphe.isPondere() and graphe.isDirected()!=True:
            if start in graphe.getListeSommet():
                click.echo(f"{Fore.GREEN}prime representer ...{Style.RESET_ALL}")
                graphe.afficher_graphe(graphe.getPrimGraphe(start),"prim")
            else:
                click.echo(f"{Fore.RED}La sommet {start} n'appartient pas au graphe{Style.RESET_ALL}")
        else:
            click.echo(f"{Fore.RED}Attention : L'algorithme de prime appliquer a un graphe connexe pondere et non orienter{Style.RESET_ALL}")
@cli.command()
@click.argument('start',type=str)
def kruskal(start:str):
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else:
        if graphe.isConnexe() and graphe.isPondere() and graphe.isDirected()!=True: 
            if start in graphe.getListeSommet():
                click.echo(f"{Fore.GREEN}kruskal representer ...{Style.RESET_ALL}")
                graphe.afficher_graphe(graphe.getKruskalGraphe(start),"kruskal")
            else:
                click.echo(f"{Fore.RED}La sommet {start} n'appartient pas au graphe{Style.RESET_ALL}")
        else:
            click.echo(f"{Fore.RED}Attention : L'algorithme de kruskal appliquer a un graphe connexe pondere et non orienter{Style.RESET_ALL}")      
    
@cli.command()
def info():
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else:
        click.echo(f"\t\t\t\t{Fore.YELLOW} Les informations de graphe : {Style.RESET_ALL}")
        click.echo(f"\t\t\t\t{Fore.GREEN}------------------------------{Style.RESET_ALL}")
        click.echo(f"\t\tGraphe orienter : {Fore.GREEN}Oui{Style.RESET_ALL}") if graphe.isDirected() else click.echo(f"\t\tGraphe orienter : {Fore.RED}Non{Style.RESET_ALL}")
        click.echo(f"\t\tGraphe pondere : {Fore.GREEN}Oui{Style.RESET_ALL}") if graphe.isPondere() else click.echo(f"\t\tGraphe pondere : {Fore.RED}Non{Style.RESET_ALL}")
        click.echo(f"\t\tGraphe planaire : {Fore.GREEN}Oui{Style.RESET_ALL}") if graphe.isPlanaire() else click.echo(f"\t\tGraphe planaire : {Fore.RED}Non{Style.RESET_ALL}")
        if graphe.isVide()!=True:
            click.echo(f"\t\tGraphe eulerian : {Fore.GREEN}Oui{Style.RESET_ALL}") if graphe.isEulerian() else click.echo(f"\t\tGraphe eulerian : {Fore.RED}Non{Style.RESET_ALL}")
        if graphe.isDirected():
            click.echo(f"\t\tGraphe fortement connexe : {Fore.GREEN}Oui{Style.RESET_ALL}") if graphe.isConnexe() else click.echo(f"\t\tGraphe fortement connexe : {Fore.RED}Non{Style.RESET_ALL}")
            click.echo(f"\t\tL'ensemble des arretes : {Fore.GREEN}{graphe.getListeArrete()}{Style.RESET_ALL}")
        else :
            click.echo(f"\t\tGraphe connexe : {Fore.GREEN}Oui{Style.RESET_ALL}") if graphe.isConnexe() else click.echo(f"\t\tGraphe connexe : {Fore.RED}Non{Style.RESET_ALL}")
            click.echo(f"\t\tL'ensemble des arcs : {Fore.GREEN}{graphe.getListeArrete()}{Style.RESET_ALL}")
        click.echo(f"\t\tL'ensemble des sommet : {Fore.GREEN}{graphe.getListeSommet()}{Style.RESET_ALL}")
        click.echo(f"\t\tnombre des sommets : {Fore.GREEN}{len(graphe.getListeSommet())}{Style.RESET_ALL}")
        if graphe.isDirected():
            click.echo(f"\t\tnombre des arcs : {Fore.GREEN}{len(graphe.getListeArrete())}{Style.RESET_ALL}")
        else:
            click.echo(f"\t\tnombre des arcs : {Fore.GREEN}{len(graphe.getListeArrete())}{Style.RESET_ALL}")
        click.echo(f"\t\tdensite : {Fore.GREEN}{graphe.getDensite()}{Style.RESET_ALL}")
@cli.command()
@click.argument("start",type=str)
@click.argument("end",type=str)
def dijkstra(start:str,end:str):
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else:
        if graphe.isPondere() and graphe.isAllPositive(): 
            if start in graphe.getListeSommet() and end in graphe.getListeSommet():
                click.echo(f"{Fore.GREEN}Dijkstra representer ...{Style.RESET_ALL}")
                graphe.afficher_graphe(graphe.getGraphe(),"dijkstra",graphe.getListeDijkstra(start,end))
            else:
                click.echo(f"{Fore.RED}La sommet {start} ou {end} n'appartient pas au graphe{Style.RESET_ALL}")
        else:
            click.echo(f"{Fore.RED}Attention : L'algorithme de dijkstra appliquer a un graphe pondre avec des poids positives{Style.RESET_ALL}")      
@cli.command()
@click.argument("start",type=str)
@click.argument("end",type=str)
def bellmanford(start:str,end:str):
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else:
        if graphe.isPondere(): 
            if start in graphe.getListeSommet() and end in graphe.getListeSommet():
                click.echo(f"{Fore.GREEN}Bellman Ford representer ...{Style.RESET_ALL}")
                graphe.afficher_graphe(graphe.getGraphe(),"bellman_ford",graphe.getListeBellmanFord(start,end))
            else:
                click.echo(f"{Fore.RED}La sommet {start} ou {end} n'appartient pas au graphe{Style.RESET_ALL}")
        else:
            click.echo(f"{Fore.RED}Attention : L'algorithme de bellman-ford appliquer a un graphe pondere{Style.RESET_ALL}")  
                      
@cli.command()
def warshall():
    graphe=getGraphe()
    if graphe==None:
        message("null")
    else:
        if graphe.isDirected(): 
            click.echo(f"{Fore.GREEN}Bellman Ford representer ...{Style.RESET_ALL}")
            graphe.afficher_graphe(graphe.getWarshallGraphe(),"warshall",None,graphe.getGraphe())
        else:
            click.echo(f"{Fore.RED}Attention : L'algorithme de warshall appliquer a un graphe orienter{Style.RESET_ALL}")  
            
            
            
            
            

@cli.command()
def help():
    click.echo("La liste des commande : ")
    commande_description("graphe help","Afficher la liste des commande")
    commande_description("graphe i","initialiser le graphe")
    commande_description("graphe o","Changer le type de graphe a graphe orienter")
    commande_description("graphe p","Changer le type de graphe a graphe pondere")
    commande_description("graphe op","Changer le type de graphe a graphe orienter pondere")
    commande_description("graphe s","Changer le type de graphe a graphe simple")
    commande_description("graphe v","Afficher la liste des sommets")
    commande_description("graphe e","Afficher la liste des arretes(arcs)")
    commande_description(f"graphe av {Fore.BLUE}vertex[arg]","Ajouter un sommet au graphe")
    commande_description(f"graphe ae {Fore.BLUE}vertex1[arg] vertex2[arg] weight[opt]","Ajouter un arrete(arc) au graphe")
    commande_description(f"graphe dv {Fore.BLUE}vertex[arg]","Supprimer un sommet de graphe")
    commande_description(f"graphe de {Fore.BLUE}vertex1[arg] vertex2[arg]","Supprimer un arrete(arc) de graphe")
    commande_description(f"graphe type","Afficher le type de graphe")
    commande_description(f"graphe info","Afficher le informations de graphe")
    commande_description(f"graphe bfs {Fore.BLUE}vertex[arg]","Afficher et representer l'algorithme de  bfs")
    commande_description(f"graphe dfs {Fore.BLUE}vertex[arg]","Afficher et representer l'algorithme de dfs")
    commande_description(f"graphe prime {Fore.BLUE}vertex[arg]","Afficher et representer l'algorithme de prime ")
    commande_description(f"graphe kruskal {Fore.BLUE}vertex[arg]","Afficher et representer l'algorithme de kruskal ")
    commande_description(f"graphe dijkstra {Fore.BLUE}vertex1[arg] vertex2[arg]","Representer l'algorithme de dijkstra")
    commande_description(f"graphe bellmanford {Fore.BLUE}vertex1[arg] vertex2[arg]","Representer l'algorithme de bellman ford")
    commande_description(f"graphe warshall","Representer l'lgorithme de warshall")
    commande_description(f"graphe cls","clear le terminale")
    
if __name__=="__main__":
    cli()
