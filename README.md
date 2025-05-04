# 📘 SmartECole  : Django School Management API - Backend

## 🎯 Contexte du projet

Ce projet s'inscrit dans le cadre du **Hackverse 2025**, une compétition d'innovation technologique organisée par le **Club GI (Génie Informatique)** de l'École Nationale Supérieure Polytechnique de Yaoundé (**ENSPY**). En réponse au défi n°2 de cette édition, notre équipe a conçu une **API de gestion intelligente des ressources matérielles et des acteurs d'un établissement scolaire**.

L'objectif est de **centraliser la gestion des salles, équipements (ordinateurs, vidéoprojecteurs), enseignants, étudiants et personnel administratif**, tout en fournissant une vue synthétique des données sous forme de **dashboard dynamique**.

---

## 🧩 Problématique abordée

De nombreux établissements scolaires font face à :

* une **gestion dispersée et manuelle** des ressources pédagogiques et administratives ;
* une **absence de suivi clair** de l'utilisation des ressources (réservations, disponibilité, etc.) ;
* une **difficulté à obtenir des statistiques précises** sur les activités ou les besoins ;
* une **communication inefficace** entre les différents corps (étudiants, enseignants, administration).

Notre solution propose donc :

* une **API REST** robuste et extensible ;
* une **gestion centralisée** des utilisateurs et ressources ;
* des **statistiques automatisées** via un endpoint de contexte (utile pour un tableau de bord) ;
* une **architecture modulaire**, adaptée à une intégration front-end web/mobile.

---

## 🚀 Fonctionnalités principales

### 👥 Utilisateurs

* Enregistrement & authentification via token pour :

  * Étudiants
  * Enseignants
  * Membres du personnel administratif

### 🏫 Gestion des ressources physiques

* CRUD pour :

  * Salles de classe
  * Ordinateurs
  * Vidéoprojecteurs
  * Départements
  * Services administratifs

### 📊 Statistiques & Dashboard

* Endpoint `/api/context/` qui retourne :

  * Nombre de requêtes envoyées / reçues
  * Nombre de réservations
  * Liste des départements et services disponibles

---

## ⚙️ Installation du projet (en local)

### 1. 📥 Cloner le dépôt

```bash
git clone https://github.com/Delmat237/Hackverse-A3Code-backend.git
cd Hackverse-A3Code-backend
```

### 2. 🐍 Créer un environnement virtuel Python

```bash
python3 -m venv env
source env/bin/activate  # Sous Windows : env\Scripts\activate
```

### 3. 📦 Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. 🧱 Appliquer les migrations et lancer le serveur

```bash
python manage.py migrate
python manage.py runserver
```

> 💡 Par défaut, la base de données utilisée est SQLite. Vous pouvez la remplacer par PostgreSQL dans `settings.py` si besoin.

---

## 🔗 Endpoints de l'API (extraits)

### 👥 Authentification & Enregistrement

* `POST /api/students/`
* `POST /api/teachers/`
* `POST /api/`
* `POST /api/login/`

### 📊 Dashboard

* `GET /api/dashboard/context/`

### 🔧 Ressources

#### Salles

* `GET /api/classrooms/`
* `POST /api/classrooms/`

#### Ordinateurs

* `GET /api/computers/`
* `POST /api/computers/`

#### Vidéoprojecteurs

* `GET /api/projectors/`
* `POST /api/projectors/`

#### Départements & Services

* `GET /api/departments/`
* `GET /api/services/`

> Pour chaque ressource, les routes `PUT` et `DELETE` sont également disponibles avec `/id/`.

---

## 🧪 Technologies utilisées

* Python 3.10+
* Django 5.2
* Django REST Framework (DRF)
* SQLite / PostgreSQL (au choix)

---

## 📁 Architecture du projet

```
backend/
├── core/                  # Configuration générale
├── classroom/             # Salles de classe
├── users/                 # Étudiants, enseignants, staff
├── dashboard/             # Statistiques
├── manage.py
└── requirements.txt
```

---

## 👨‍💻 Équipe projet

Développé dans le cadre du Hackverse 2025, défi n°2 :

* **Azangue Delmat Leonel**
* **Bala Andegue François**


Club Génie Informatique - ENSPY

---

> 🙏 Merci d'utiliser ce projet. Toute contribution, remarque ou amélioration est la bienvenue !
