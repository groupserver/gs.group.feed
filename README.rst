=================
``gs.group.feed``
=================

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2013-10-21
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

Introduction
============

This product displays a list of feed in the secondary area of the
group page [#home]_. The list of feeds that is displayed is
stored as a JSON_ blob in the group.

JSON
====

The JSON for the feeds is a list of feed objects, stored as a
string in the ``webfeeds`` property of the group folder. Each
feed object consists of the following.

:``name``: The name of the Web feed.
:``name_url``: The page that the name links to.
:``url``: The web-feed URL

For example::

  [
    {
      "name": "Issue tracker", 
      "feed_url": "https://redmine.iopen.net/projects/groupserver/activity.atom", 
      "name_url": "https://redmine.iopen.net/projects/groupserver/activity"
    }
  ]

Resources
=========

- Code repository: https://github.com/groupserver/gs.group.feed
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

.. [#home] See the ``gs.group.home`` product
           <https://github.com/groupserver/gs.group.feed>

..  LocalWords:  NotifyNewMember loggedInUser txt msg html groupInfo JSON
..  LocalWords:  joiningUser IGSJoiningUser NotifyAdmin
