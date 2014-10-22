"use strict";
// Load the list of active group members using AJAX.
//
// Copyright © 2014 OnlineGroups.net and Contributors.
// All Rights Reserved.
//
// This software is subject to the provisions of the Zope Public License,
// Version 2.1 (ZPL). http://groupserver.org/downloads/license/
jQuery.noConflict();

function gs_group_feed_init () {
    jQuery('.gs-group-feed-content').each(gs_group_feed_add);
}

function gs_group_feed_add (i, e) {
    var feedDiv=null, feedUrl=null;
    feedDiv = jQuery('#gs-group-feed-content-'+i);
    feedUrl = feedDiv.data('feed-url');
    feedDiv.FeedEk({
        FeedUrl: feedUrl,
        MaxCount : 2,
        ShowDesc : false,
        ShowPubDate: true,
        DescCharacterLimit: 48,
    });
}

jQuery(window).load(function () {
    gsJsLoader.with_module('/++resource++FeedEk-2.0.js', gs_group_feed_init);
});