# PlanetsAPI

A public GraphQL API for information about planets and exoplanets.

## Writing Queries

```
query{
  planet(code:"jupiter"){
    massKg
    radiusKm
    orbitDays
    semimajorAu
    discoveryMethod
  }
}
```

The above query will produce the following result:

```
{
  "data": {
    "planet": {
      "massKg": "1.898e+27",
      "radiusKm": "43441",
      "orbitDays": "4300",
      "semimajorAu": "0.52028",
      "discoveryMethod": "telescope"
    }
  }
}
```

## Examples

[Python](https://github.com/ZaneTurner/PlanetsAPI/blob/master/Examples/AccessPlanetByID.py)
