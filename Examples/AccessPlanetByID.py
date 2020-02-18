import requests, json

URL = "https://pristine-gadget-267405.appspot.com/graphql/"

query = """
{
  planet(code:"earth"){
    name
    massKg
    radiusKm
    orbitDays
    semimajorAu
    discoveryMethod
  }
}
"""


def get_planet_data(arguments):
    arguments = dict(query=arguments)  # wrap query in dictionary

    graph_ql_request = requests.post(url=URL,
                                     data=json.dumps(arguments),
                                     headers={"Content-type": "application/json",
                                              "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'})
    country_data = graph_ql_request.json()
    return country_data


print(get_planet_data(query))
