$(function () {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json',
	  (data, status) => {
	      for (let movie of data.results) {
		  let title = $('<li></li>').text(movie['title']);
		  $('UL#list_movies').append(title);
	      }
	  });
});
