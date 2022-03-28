from .import views
from .models import Movie
from django.shortcuts import render

# HINT: Create a view to provide movie recommendations list for the HTML template

def movie_recommendation_view(request):
    if request.method == "GET":
      # The context/data to be presented in the HTML template
      context = generate_movies_context()
      # Render a HTML page with specified template and context
      return render(request, 'movierecommender/movie_list.html', context)

def generate_movies_context():
  context = {}
  # SHow only Movies In Recommendation List
  # Sorted by vote_average in desc
  # Get Recommended Movie counts

  recommended_counts = Movie.objects.filter (
    recommended=True
  ).count ()

  # if there are no recommended movies
  if recommended_counts == 0:
    # just return the top voted and unwatched movies as popular ones

    movies = Movie.objects.filter (
      watched=False
    ) .order_by('-vote_count')[:30]
    else:
      # Get the top voted, unwatched and recommended movies
      movies = Movie.objects.filter (
        watched=False
      ) .filter (
        recommended=True
      ) .order_by('-vote_count')[:30]
      context ['movie_list'] = movies

      return context

