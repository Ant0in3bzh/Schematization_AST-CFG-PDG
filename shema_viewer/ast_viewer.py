import ast
import astor
from graphviz import Digraph


def ast_pdf_viewer(code: str):
    # Analyse du code source pour créer l'AST.
    tree = ast.parse(code)

    # Créer un objet Digraph
    dot = Digraph(comment='AST - Abstract Syntax Tree')


    # Fonction récursive pour ajouter les nœuds à l'AST
    def add_nodes(node):
        node_id = str(id(node))
        if isinstance(node, ast.Name):
            # Si le nœud est une variable (Name), inclure le nom
            dot.node(node_id, f"Name\nName: {node.id}")
        elif isinstance(node, ast.Constant):
            # Si le nœud est une constante (Constant), inclure la valeur
            dot.node(node_id, f"Constant\nValue: {node.value}")
        elif isinstance(node, ast.Assign):
            # Si le nœud est une affectation (Assign), inclure les cibles (les noms) de l'affectation
            targets = ", ".join(target.id for target in node.targets)
            dot.node(node_id, f"Assign\nTargets: {targets}")
        elif isinstance(node, ast.Attribute) and hasattr(node, 'attr'):
            # Si le nœud est un attribut avec un nom, inclure le nom de l'attribut
            dot.node(node_id, f"Attribute\nName: {node.attr}")
        elif isinstance(node, ast.Expr):
            # Si le nœud est une expression, inclure l'expression
            dot.node(node_id, f"Expr")
        elif isinstance(node, ast.Store):
            # Si le nœud est un magasin (Store), inclure l'information de stockage
            dot.node(node_id, f"Store")
        else:
            dot.node(node_id, node.__class__.__name__)

        for child in ast.iter_child_nodes(node):
            child_id = str(id(child))
            dot.edge(node_id, child_id)
            add_nodes(child)


    # Ajouter le nœud racine
    dot.node(str(id(tree)), tree.__class__.__name__)

    # Ajouter les autres nœuds
    add_nodes(tree)
    # Utilisez astor pour générer la représentation du code AST
    ast_code = astor.dump_tree(tree)

    # Affichez la représentation de l'AST
    print(ast_code)

    # Générer et afficher le schéma AST
    dot.render('AST - Abstract Syntax Tree', view=True)


if __name__ == '__main__':
    # Charger le code source à partir d'un fichier (ou vous pouvez le définir directement dans une chaîne).
    with open('../test_files/simple_lambda_file.py', 'r') as file:
        code = file.read()
    ast_pdf_viewer(code)

    with open('../test_files/medium_lambda_file.py', 'r') as file:
        code = file.read()
    ast_pdf_viewer(code)
