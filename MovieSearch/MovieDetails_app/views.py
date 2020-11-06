
import requests
from .serializers import MovieSerializer
from .models import Movie
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MoviesView(APIView):

    def get(self, request):
        if request.data.get("order"):
            if request.data["order"] == "dsc":
                print("working dsc")
                movies = Movie.objects.all().order_by("id").reverse()
            else:
                return Response(data={"Error": "You can only sort id with order equal to dsc (for descending)"}, status=status.HTTP_400_BAD_REQUEST)

        else:
            movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):

        if request.data.get("title"):
            title = request.data["title"]
        else:
            return Response(data={"Error": "You must provide title in POST request with key named title"}, status=status.HTTP_400_BAD_REQUEST)

        my_api_key = 'f961e895'
        url = f'http://www.omdbapi.com/?t={title}&type=movie&apikey={my_api_key}'
        response = requests.get(url)
        if response.status_code == requests.codes.ok and response.json()['Response'] == 'True':
            if not Movie.objects.filter(Title=response.json()['Title']).exists():
                serializer = MovieSerializer(data=response.json())
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(data={"Error": "Problem with serializing data from external API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                movie_from_database = Movie.objects.get(Title=response.json()['Title'])
                movie_from_database_serialized = MovieSerializer(movie_from_database)
                return Response(movie_from_database_serialized.data)
        else:
            return Response(data={"Error": "No movie with that title"}, status=status.HTTP_204_NO_CONTENT)