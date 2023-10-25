import ast
import networkx as nx
import matplotlib.pyplot as plt


def pdg_pdf_viewer(code: str):
    # Analyser le code source pour créer l'AST
    tree = ast.parse(code)

    # Créer un graphe dirigé (DiGraph) pour représenter les dépendances
    graph = nx.DiGraph()

    # Parcourir l'AST et identifier les dépendances
    # Exemple : si une fonction utilise une autre fonction, ajoutez une arête entre elles
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            for item in ast.walk(node):
                if isinstance(item, ast.Name) and item.id != function_name:
                    graph.add_edge(function_name, item.id)

    # Visualisez le graphe
    pos = nx.spring_layout(graph)
    plt.title("PDG - Program Dependence Graph")

    nx.draw(graph, pos, with_labels=True, node_size=500)

    plt.savefig("..\PDG -Program Dependence Graph.pdf", format="pdf")

    plt.show()



if __name__ == '__main__':
    # Lire le code source Python
    with open('../test_files/simple_lambda_file.py', 'r') as file:
        code = file.read()
    pdg_pdf_viewer(code)