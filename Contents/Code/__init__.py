# -*- coding: utf-8 -*-

PLUGIN_PREFIX           = "/music/Cantelou"
PLUGIN_ID               = "com.plexapp.plugins.Cantelou"
PLUGIN_REVISION         = 0.1
PLUGIN_UPDATES_ENABLED  = True

ICON="icon-default.png"
ART="art-default.jpg"
CACHE_INTERVAL = 3600 * 2
NAME="Cantelou"

URL="http://www.europe1.fr/podcasts/revue-de-presque.xml"

####################################################################################################
def Start():
  Plugin.AddPrefixHandler(PLUGIN_PREFIX, MainMenu, NAME, R(ICON),R(ART))
  Plugin.AddViewGroup("Details", viewMode="InfoList", mediaType="items")
  Plugin.AddViewGroup("ShowList", viewMode="List", mediaType="items")
  MediaContainer.title1 = 'Cplus'
  MediaContainer.content = 'Items'
  MediaContainer.art = R('bg-default.jpg')
  HTTP.SetCacheTime(CACHE_INTERVAL)

####################################################################################################
def MainMenu():
	dir = MediaContainer(title1="Canal Plus", content = 'Items', art = R('art-default.jpg'), mediaType='music')
	dir.viewGroup = 'Details'
	data=HTML.ElementFromURL(URL,encoding="utf-8")
	item=0
	for item in data.xpath('//item'):
		title	= item.xpath('title')[0].text
		pubDate	= item.xpath('pubdate')[0].text
		summary = ''.join(item.xpath('./summary/text()'))
		#Log(summary)
		url = item.xpath('enclosure')[0].get('url')
		dir.Append(TrackItem(url,title.strip(),"info","Rubrique",summary=summary+pubDate,art=R(ICON)))
	return dir


###################################################################################################
def utf8decode(s):
	s = s.encode("iso-8859-1")
	return s.decode("utf-8")
