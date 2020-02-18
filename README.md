# PlanetsAPI

A public GraphQL API for information about planets and exoplanets.

## Writing Queries

```
{
  planet(id:1) {
    name
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
'data': {
  'planet': {
      'name': 'Mercury',
      'massKg': '3.285e+23',
      'radiusKm': '2439.7',
      'orbitDays': '88',
      'semimajorAu': '0.387',
      'discoveryMethod': 'telescope'}
    }
}
```
