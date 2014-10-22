# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import unicode_literals, absolute_import
from json import loads as json_load
from zope.cachedescriptors.property import Lazy
from gs.group.base import GroupViewlet


class FeedViewlet(GroupViewlet):
    '''The viewlet for displaying a list of feeds in a group'''

    @Lazy
    def feeds(self):
        retval = self.groupInfo.get_property('webfeeds', '')
        return retval

    @property
    def feedInfo(self):
        feeds = json_load(self.feeds)
        for feed in feeds:
            yield feed

    @Lazy
    def show(self):
        retval = bool(self.feeds)
        return retval
