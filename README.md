# PlanetsAPI

A public GraphQL API for information about planets and exoplanets. Currently the API is down, will be fixed by Feburary 21st.

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

## Implementation

This GraphQl API was implemented using Python/Django and is hosted on Google Cloud. It uses a MySQL database to store the information about the planets. 

## Acknowledgements/source

This API makes use of data from the first public release of the WASP data (Butters et al. 2010) as provided by the WASP consortium and services at the NASA Exoplanet Archive, which is operated by the California Institute of Technology, under contract with the National Aeronautics and Space Administration under the Exoplanet Exploration Program.

## License

[MIT] (https://github.com/ZaneTurner/PlanetsAPI/blob/master/LICENSE)

