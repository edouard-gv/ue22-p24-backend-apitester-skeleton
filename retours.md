# Retours ApiTesteur ue24 groupe 3

## Lisez la doc
- Quand on dit une liste c'est une liste, pas un dict
- Quand on dit une liste d'id on ne renvoie que les id, pas des objet
- Quand on retourne un objet, on retourne un dict simple... pas le dictionnaire des colonnes
- On peut renvoyer plus, mais pas moins ni différent

```json
{
  "0": 1,
  "1": 2,
  "2": 3,
  "3": 4,
  "4": 5
}

{
  "message": "[1, 2, 3, 4, 5]"
}


{
  "association_id": {
    "0": 1
  },
  "date": {
    "0": "2024-04-15"
  },
  "description": {
    "0": "Un marathon de programmation de 48 heures."
  },
  "id": {
    "0": 101
  },
  "lieu": {
    "0": "Campus Informatique"
  },
  "nom": {
    "0": "Hackathon"
  }
}

{
  "date": {
    "1": "2024-05-20",
    "2": "2024-04-30"
  },
  "description": {
    "1": "Tournoi amical de basket entre étudiants.",
    "2": "Atelier de peinture pour découvrir différentes techniques."
  },
  "lieu": {
    "1": "Gymnase Central",
    "2": "Atelier Arts"
  },
  "nom": {
    "1": "Tournoi de Basket",
    "2": "Atelier Peinture"
  }
}

{
  "columns": [
    "id",
    "association_id",
    "nom",
    "date",
    "lieu",
    "description"
  ],
  "data": [
    [
      102,
      2,
      "Tournoi de Basket",
      "2024-05-20",
      "Gymnase Central",
      "Tournoi amical de basket entre étudiants."
    ],
    [
      103,
      2,
      "Atelier Peinture",
      "2024-04-30",
      "Atelier Arts",
      "Atelier de peinture pour découvrir différentes techniques."
    ]
  ],
  "index": [
    1,
    2
  ]
}
```

## Quelques optimisations / alternatives
- pas besoin de jsonifier les dict et les list
- on peut faire des ```if id in associations_df.id:``` plutôt que de faire la requête et de regarder si elle est vide
    - Mais on ne teste pas en dur ```if id>=1 and id<=4 :```
- pas besoin de préciser le code retour si 200
- et bien-sûr il y a des manière plus ou moins élégantes d'avoir les bonnes structures pandas

``` python
return evenements_df[evenements_df.association_id == id].to_dict(orient='records')

return list(evenements_df[evenements_df.association_id == id].transpose().to_dict().values())
```

- mais on peut quand même profiter des avantages des lib ;)

``` python
def details_association(id):
    for association in associations:
        if id == association["id"]:
            return jsonify(association), 200
    return jsonify({ "error": "Association not found" }), 404
```
## Note
- Détails aux pluriel, ce n'est pas juste la description, "Le Bureau Des Étudiants pour les passionnés d'informatique."
- Abusez du formatteur black

