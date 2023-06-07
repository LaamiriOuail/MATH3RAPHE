

def grapheRepresentationComponent(container,graphe):
    frame_graphe_rep=container.newFram(200,0,600,300,None,None)
    frame_graphe_rep_nx=frame_graphe_rep.newFrameGraphe(0,0,600,300,graphe.getNetworkxGraph(),"graphe",None)
    return frame_graphe_rep,frame_graphe_rep_nx