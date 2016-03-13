# -*- coding: utf-8 -*-

import re
PLUGIN_PREFIX = "/music/Cantelou"
PLUGIN_ID = "com.plexapp.plugins.Cantelou"
PLUGIN_REVISION = 0.2
PLUGIN_UPDATES_ENABLED = False

ICON = "icon-default.png"
ART = "art-default.jpg"
CACHE_INTERVAL = 3600 * 2
NAME = "Cantelou"

URL = "http://www.europe1.fr/podcasts/revue-de-presque.xml"

##########################################################################


def Start():
    Plugin.AddPrefixHandler(PLUGIN_PREFIX, MainMenu, NAME, R(ICON), R(ART))
    Plugin.AddViewGroup("Details", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("ShowList", viewMode="List", mediaType="items")
    MediaContainer.title1 = 'Revue de presques'
    MediaContainer.content = 'Items'
    MediaContainer.art = R('bg-default.jpg')
    HTTP.SetCacheTime(CACHE_INTERVAL)

##########################################################################


def MainMenu():
    dir = MediaContainer(
        title1="Revue de Presque",
        content='Items',
        art=R('art-default.jpg'),
     mediaType='music')
    dir.viewGroup = 'Details'
    data = XML.ElementFromURL(URL, encoding=None)
    for item in data.xpath('//item'):
        summary = item.xpath(
            't:summary', namespaces={
                't': 'http://www.itunes.com/dtds/podcast-1.0.dtd'})[0].text
        keyword = item.xpath(
            't:keywords', namespaces={
                't': 'http://www.itunes.com/dtds/podcast-1.0.dtd'})[0].text
        pubDate = item.xpath('pubDate')[0].text
        url = item.xpath('enclosure')[0].get('url')
        title = item.xpath('title')[0].text.strip()
        image = "http://cdn-europe1.new2.ladmedia.fr/var/europe1/storage/images/media/podcasts/la-revue-de-presque-de-nicolas-canteloup/511584-4-fre-FR/La-revue-de-presque-de-Nicolas-Canteloup.jpg"
        summary = "[%s]\n\n%s\n%s\n" % (title, summary.strip(), pubDate)
        title = title.strip()
        dir.Append(
            TrackItem(
                url,
                title,
                "info",
                "Rubrique",
                summary=summary,
                thumb=R('icon-default.png')))
    return dir

#<Element {http://www.itunes.com/dtds/podcast-1.0.dtd}summary at 0x95bce64>

#	item=0
#	for item in data.xpath('//item'):
#		title	= item.xpath('title')[0].text
#		pubDate	= item.xpath('pubdate')[0].text
#		summ = XML.StringFromElement(item)
#		Log(summ)
#		summary = "blank"
#		url = item.xpath('enclosure')[0].get('url')
#		dir.Append(TrackItem(url,title.strip(),"info","Rubrique",summary=summary+pubDate+"("+summ+")",art=R(ICON)))


##########################################################################
def utf8decode(s):
    s = s.encode("iso-8859-1")
    return s.decode("utf-8")
