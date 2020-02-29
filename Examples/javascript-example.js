const { createApolloFetch } = require('apollo-fetch');

const fetch = createApolloFetch({
  uri: 'https://pristine-gadget-267405.appspot.com/graphql/',
});

// You can also easily pass variables for dynamic arguments
fetch({
  query: `query{
    planet(code:"neptune"){
      name
      massKg
      radiusKm
      orbitDays
      semimajorAu
      discoveryMethod
    }
  }`,
}).then(res => {
  console.log(res.data);
});
