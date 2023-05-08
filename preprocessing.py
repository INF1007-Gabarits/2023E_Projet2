from consts import *
import pandas as pd
from typing import List, NoReturn, Tuple


def lireDonnees(cheminHauts: str, cheminBas: str, cheminChaussures: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    # TODO: Lire les fichiers csv comme des dataframes

    return hautsDf, basDf, chaussuresDf


def filtrerColonnes(dataframe: pd.DataFrame, colonnesAGarder: List[str])  -> pd.DataFrame:
    #TODO Filter le dataframe pour juste garder les colonnes spécifiées dans colonnesAGarder

    return dataframeFiltre


def renommerColonne(dataframe: pd.DataFrame, vieuxNom: str, nouveauNom: str) -> pd.DataFrame:
    #TODO renommer la colonne nommée vieuxNom en nouveauNom

    return dataframeRenomme


def enleverDoublons(dataframe: pd.DataFrame) -> pd.DataFrame:
    #TODO Enlever les lignes doublées du dataframe

    return dataframeSansDoublons


def ajouterColonneType(dataframe: pd.DataFrame, colType: str) -> pd.DataFrame:
    # TODO Ajouter une colonne nommée "Type" avec la valeur par défaut colType

    return dataframeAvecType


def ajouterColonneBalance(dataframe: pd.DataFrame) -> pd.DataFrame:
    # TODO Calculer la colonne balance à partir des colonnes Prix_Achat et Prix_Vente
    # Balance = Prix_Vente - Prix_Achat

    return dataframeAvecProfit


def pretraiterDataframe(dataframe: pd.DataFrame, objType: str) -> pd.DataFrame:
    # TODO Exécuter les fonctions pour prétraiter le dataframe
    # TODO 1 - Filtrer le dataframe pour juste garder les colonnes COLONNES_IMPORTANTES

    # TODO 2 - renommer colonne "Buy" à "Buy_Price"

    # TODO 3 - renommer colonne "Sell" à "Sell_Price"

    # TODO 4 - Enlever les doublons dans le dataframe

    # TODO 5 -Ajouter une colonne type avec la valeur par defaut typeObj

    # TODO 6 - Ajouter la colonne profit


    return dataframe


def mergerDataframes(listeDataframes: List[pd.DataFrame]) -> pd.DataFrame:
    # TODO Merger tous les dataframe dans la liste listeDataframes en un seul, sans les indices

    return dataframeMerge


def sauvegarderDataframe(dataframe: pd.DataFrame, nomFichier: str) -> NoReturn:
    # TODO Sauvegarder le dataframe dans le fichier nomFichier
    pass


if __name__ == "__main__":
    # Lecture des données
    hautsDf, basDf, chaussuresDf = lireDonnees(CHEMIN_DF_HAUTS, CHEMIN_DF_BAS, CHEMIN_DF_CHAUSSURES)

    # Prétraitement des dataframes
    hautsDf      = pretraiterDataframe(hautsDf, NOM_TYPE_HAUT)
    basDf        = pretraiterDataframe(basDf, NOM_TYPE_BAS)
    chaussuresDf = pretraiterDataframe(chaussuresDf, NOM_TYPE_CHAUSSURES)

    # Création du dataframe complet
    dataframeComplet = mergerDataframes([hautsDf, basDf, chaussuresDf])

    # Sauvegarde du dataframe
    sauvegarderDataframe(dataframeComplet, CHEMIN_DF_COMPLET)