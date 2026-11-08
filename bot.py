"""Logique du chatbot : des règles simples basées sur des mots-clés.

Chaque règle associe une liste de mots-clés à une réponse.
Le bot cherche le premier mot-clé présent dans la question de l'utilisateur.
"""

import unicodedata

# Liste des règles : (mots-clés, réponse)
REGLES = [
    (["bonjour", "salut", "hello", "coucou"],
     "Bonjour ! Je suis FAQ Bot. Pose-moi une question sur Git, GitHub, Docker ou le CI/CD."),
    (["github"],
     "GitHub est une plateforme en ligne qui héberge des dépôts Git et permet de collaborer (pull requests, issues, GitHub Actions)."),
    (["git"],
     "Git est un outil de gestion de versions : il garde l'historique de ton code grâce aux commits."),
    (["commit"],
     "Un commit est une sauvegarde de tes modifications, accompagnée d'un message qui explique ce qui a changé."),
    (["branche", "branch"],
     "Une branche permet de travailler sur une fonctionnalité sans toucher au code principal (main)."),
    (["docker", "conteneur", "container"],
     "Docker emballe une application et ses dépendances dans un conteneur qui fonctionne partout de la même façon."),
    (["kubernetes", "k8s"],
     "Kubernetes orchestre des conteneurs : il les déploie, les redémarre et les met à l'échelle automatiquement."),
    (["ci/cd", "pipeline", "ci", "cd"],
     "Le CI/CD automatise les tests (CI) et le déploiement (CD) à chaque modification du code."),
    (["linux"],
     "Linux est un système d'exploitation open source, très utilisé sur les serveurs et dans le cloud."),
    (["terraform"],
     "Terraform est un outil d'Infrastructure as Code : on décrit l'infrastructure dans des fichiers, et Terraform la crée automatiquement."),
    (["aws", "amazon"],
     "AWS (Amazon Web Services) est la plateforme cloud d'Amazon : serveurs (EC2), stockage (S3), bases de données…"), 
    (["merci", "thanks"],
     "Avec plaisir ! 😊"),
    (["au revoir", "bye", "a bientot"],
     "Au revoir et bon courage !"),
]

REPONSE_PAR_DEFAUT = (
    "Désolé, je n'ai pas compris. Essaie avec un mot-clé comme : git, github, commit, "
    "branche, docker, kubernetes, linux, terraform, aws ou pipeline."
)


def normaliser(texte: str) -> str:
    """Met le texte en minuscules et retire les accents (é -> e)."""
    texte = texte.lower().strip()
    texte = unicodedata.normalize("NFD", texte)
    return "".join(c for c in texte if unicodedata.category(c) != "Mn")


def repondre(question: str) -> str:
    """Renvoie la réponse du bot pour une question donnée."""
    question = normaliser(question)
    if not question:
        return "Écris une question pour commencer 🙂"

    # On découpe la question en mots pour éviter que "ci" soit trouvé dans "merci"
    mots = question.replace("?", " ").replace("!", " ").replace(",", " ").split()

    for mots_cles, reponse in REGLES:
        for mot_cle in mots_cles:
            if " " in mot_cle:
                # Expression de plusieurs mots : on cherche dans la phrase entière
                if mot_cle in question:
                    return reponse
            elif mot_cle in mots:
                return reponse
    return REPONSE_PAR_DEFAUT
