pyyts
=====

YTS (http://yts.re) API Client

Install
=======

``pip install pyyts``

Sample Usage
============
::

    import pyyts

    test_client = pyyts.YTSClient("YOUR_APPLICATION_KEY_HERE")
    print test_client.movies.list_movies()