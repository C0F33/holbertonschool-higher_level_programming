fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json()) // Parse the JSON from the response
  .then(data => {
    const movies = data.results; // Get the list of movies from the data
    const listMovies = document.getElementById('list_movies'); // Get the UL element

    // Iterate over each movie and create a list item
    movies.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title; // Set the text content to the movie title
      listMovies.appendChild(listItem); // Append the list item to the UL
    });
  })
  .catch(error => {
    console.error('Error fetching movie data:', error); // Log any errors to the console
  });
