#!/usr/bin/env python
# -*- coding: utf8 -*-

import logging
import os

from spotify import Link
from spotify.manager import SpotifySessionManager, SpotifyContainerManager


class Starrify(SpotifySessionManager, SpotifyContainerManager):

    appkey_file = os.path.join(os.path.dirname(__file__), 'spotify_appkey.key')

    def __init__(self, track_uri, username=None, password=None, remember_me=False,
                 login_blob='', proxy=None, proxy_username=None,
                 proxy_password=None):
        SpotifySessionManager.__init__(self, username=username, password=password,
                                       remember_me=remember_me, login_blob=login_blob,
                                       proxy=proxy, proxy_username=proxy_username,
                                       proxy_password=proxy_password)
        self.track_uri = track_uri
        self.ctr = None
        # self.container_manager = JukeboxContainerManager()
        print "Logging in, please wait..."

    def star(self, track_uri, session):
        link = Link.from_string(track_uri)
        if not link.type() == Link.LINK_TRACK:
            return

        print "Starring", track_uri

        track = link.as_track()
        track.starred(session, True)
        return track.starred(session)

    def container_loaded(self, c, u):
        print "Container loaded"
        self.disconnect()

    def logged_in(self, session, error):
        if error:
            print error
            return

        print "Logged in!"
        print self.star(self.track_uri, session)

        self.ctr = session.playlist_container()
        self.watch(self.ctr)

    def logged_out(self, session):
        print "Logged out!"


if __name__ == '__main__':
    import optparse
    op = optparse.OptionParser(version="%prog 0.1")
    op.add_option("-t", "--track", help="Spotify track URI")
    op.add_option("-u", "--username", help="Spotify username")
    op.add_option("-p", "--password", help="Spotify password")
    op.add_option("-v", "--verbose", help="Show debug information",
        dest="verbose", action="store_true")
    (options, args) = op.parse_args()
    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    session_m = Starrify(options.track, options.username, options.password, True)
    session_m.connect()
