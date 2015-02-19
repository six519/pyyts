#!/usr/bin/env python

import pyyts

test_client = pyyts.YTSClient("test")
print test_client.movies.add_movie_bookmark()
#print test_client.users.user_profile()