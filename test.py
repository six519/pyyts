#!/usr/bin/env python

import pyyts

test_client = pyyts.YTSClient()
#print test_client.movies.list_movies()
#print test_client.movies.movie_details()
#print test_client.movies.movie_suggestions(movie_id=10)
#print test_client.movies.movie_comments()
print test_client.movies.movie_reviews(movie_id=20)