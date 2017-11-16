# Project Jarvis

Jarvis est un petit e-commerce écrit en python avec le framework Django.

* Produits
* Gestion du Panier
  * [X] Ajout
  * [X] Suppression
  * [X] Modification
  * [ ] Commander
* Gestion des utilisateurs
  * [X] Connexion
  * [X] Déconnexion
  * [X] Inscription
* Contact
* Administration
* Gestion des fournisseurs

## Requirements

* python 2.7.11
* django 1.11

* pillow 4.3                    // Pour les images
* django-cart 1.0               // Pour le panier
* django-bootstrap3             // Pour le design

* MySQL-python 1.2              // Pour la base de données Mysql
* mysqlclient 1.3               // Pour la base de données Mysql

## Recupérer les dépendances

pip install -r lib_jarvis.txt

## Fonctionnalités

### Fournisseurs

Gestion des fournisseurs dans l'administration :
  * Ajout
  * Suppression
  * Modification

### Produits

Gestion des produits :
  * page d'index des produits avec pagination
  * page de consultation d'un produit

Un produit possède :
  * un nom
  * une référence
  * une description courte (pour l'aperçu)
  * une description longue
  * le nombre en stock
  * une image
  * un prix
  * des commentaires

Ajout d'un nouveau produit dans l'administration.

Pour ajouter un commentaire, il faut être connecté.

### Panier

Permet la gestion du panier, possibilités :
 * d'ajouter un produit
 * de supprimer un produit
 * de modifier la quantité d'un produit
 * de vider le panier si des produits sont dedans

Pour valider le panier, il faut être connecté.

### Users

Gestion des utilisateurs :
 * Connexion
 * Déconnexion
 * Inscription

### Contact

Page de contact. Envoie d'un mail.

### Administration

Gestion des produits, fournisseurs, ...

### Page accueil

Contient un petit text descriptif du site.
Puis affiche les 3 derniers produits ajoutés.
Pour finir, un lien vers un flux RSS des derniers commentaires est présent.
