# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html



import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin


# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEO = {'LIVE TV': [{'name': 'ABP News',
                       'thumb': 'http://www.media247.co.uk/bizasia/wp-content/uploads/2017/01/abpnewsnew001.jpg',
                       'video': 'http://hindiabp-lh.akamaihd.net/i/hindiabp1new_1@192103/master.m3u8',
                       'genre': 'Animals'},
                      {'name': 'ABP Ananda',
                       'thumb': 'https://pbs.twimg.com/profile_images/2265469431/mhfdk1dfs640hd35tox6_400x400.jpeg',
                       'video': 'http://bengaliabp-lh.akamaihd.net/i/abpbanglanew_1@192108/master.m3u8',
                       'genre': 'Animals'},
                      {'name': 'ETV Bangla',
                       'thumb': 'http://sim03.in.com/62/2e7599512bb9b51fce54dd72e1f02f9e_m.jpg',
                       'video': 'http://etvbanglalive-lh.akamaihd.net/i/etv_bangla_news_live_1@2289/index_3_av-p.m3u8?sd=10&play-only=primary&rebase=on&hdntl=exp=1479008971~acl=%2f*~data=hdntl~hmac=151ed96eca9cf183c67429750ada6122e1c1108f74716596b6703eed81a0c701',
                       'genre': 'Animals'},
					   {'name': 'NDTV 24x7',
                       'thumb': 'http://www.indiantelevision.com/sites/drupal7.indiantelevision.co.in/files/images/tv-images/2014/05/08/ndtv.jpg',
                       'video': 'http://ndtvstream-lh.akamaihd.net/i/ndtv_24x7_1@300633/index_352_av-p.m3u8',
                       'genre': 'Animals'},
					   {'name': 'NDTV INDIA HINDI',
                       'thumb': 'https://yt3.ggpht.com/-H95jY2ux2YQ/AAAAAAAAAAI/AAAAAAAAAAA/ZWe_3_BJ5sY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg',
                       'video': 'http://bglive-a.bitgravity.com/ndtv/indlo/live/native',
                       'genre': 'Animals'},
					   {'name': 'INDIA TV',
                       'thumb': 'http://1.bp.blogspot.com/-AMQZ-kBgxA4/T5DVOkqDO6I/AAAAAAAA2XU/yVqULj-ctv0/s1600/India-TV-Logo.jpg',
                       'video': 'http://indiatvnews-lh.akamaihd.net/i/ITV_1@199237/index_3_av-p.m3u8',
                       'genre': 'Animals'},
					   {'name': 'IBN 7',
                       'thumb': 'http://www.india-forums.com/tellybuzz/images/uploads/671_IBN-7-TV-Channel-India-Logo.jpg',
                       'video': 'http://ibn7_hls-lh.akamaihd.net/i/ibn7_hls_n_1@174951/index_3_av-p.m3u8',
                       'genre': 'Animals'},
					   {'name': 'NEWS 24',
                       'thumb': 'http://tvimages.burrp.com/images/channels2/news/news24.png',
                       'video': 'http://d20vhs4gtao945.cloudfront.net/bagnetworks/ngrp:news24_all/chunklist_b634000.m3u8',
                       'genre': 'Animals'},
					   {'name': 'INDIA NEWS',
                       'thumb': 'https://upload.wikimedia.org/wikipedia/en/4/49/India-news-logo.gif',
                       'video': 'http://indiatvnews-lh.akamaihd.net/i/ITV_1@199237/index_3_av-b.m3u8?sd=10&rebase=on',
                       'genre': 'Animals'},
					   {'name': 'NEWS X HD',
                       'thumb': 'http://images.mytm.in/u1341/3251071.jpg',
                       'video': 'http://newsx.live-s.cdn.bitgravity.com/cdn-live/_definst_/newsx/live/newsxnew.smil/chunklist_w218860994_b512000.m3u8',
                       'genre': 'Animals'},					   
					   {'name': 'TV100 NEWS',
                       'thumb': 'http://livetvstream247.tk/wp-content/uploads/2016/03/tv100-news-logo.jpg',
                       'video': 'rtmp://capcobroadcaststream.in/guj//tv100.sdp_aac',
                       'genre': 'Animals'},					   
					   {'name': 'NEWS NATION',
                       'thumb': 'http://extradesimovies.com/wp-content/uploads/2016/10/news-nation-Live-logo.png',
                       'video': 'rtmp://54.255.176.172/live/newsnation_720p',
                       'genre': 'Animals'},
					   {'name': 'NEWS STATE',
                       'thumb': 'https://newsnation1.s3.amazonaws.com/images/2014/02/19/740527207-UP.jpg',
                       'video': 'rtmp://54.255.176.172/trans/nnstate_720p',
                       'genre': 'Animals'},
					   {'name': 'JOO MUSIC',
                       'thumb': 'https://lh4.ggpht.com/Gmztx1CSvrLf3GsE8N67w5_THsaI8mVqPVFUW7l4Hor_71PTBnobOlBnCniWMmXxJDI=w300',
                       'video': 'http://wowzacontrol.com:1935/8038/8038/chunklist_w1610289693.m3u8',
                       'genre': 'Animals'},
					   {'name': 'E24',
                       'thumb': 'http://www.fetchlogos.com/wp-content/uploads/2015/10/E-24-Logo.jpg',
                       'video': 'http://d3ibnxavurfby0.cloudfront.net/bagnetworks/ngrp:e24_all/playlist.m3u8',
                       'genre': 'Animals'},					   
					   {'name': 'KISS TV',
                       'thumb': 'http://www.webtvstreams.com/wp-content/uploads/2014/04/Kiss-Tv.jpg',
                       'video': 'http://fms113.mediadirect.ro:1937/live3/_definst_/kiss_low/playlist.m3u8?publisher=83&token=c31533f4f4f1f6154428aa3cfbcbecbf41719aa5baadd852',
                       'genre': 'Animals'},					   
					   {'name': 'DD NEWS',
                       'thumb': 'https://upload.wikimedia.org/wikipedia/commons/7/77/DD_News_Logo_2015.jpg',
                       'video': 'http://nicls1-lh.akamaihd.net/i/ddnews_1@409133/master.m3u8',
                       'genre': 'Animals'},	
					   {'name': 'NDTV PRIME',
                       'thumb': 'http://www.exchange4media.com/storyimages/fs_57129.jpg',
                       'video': 'http://bglive-a.bitgravity.com/ndtv/prolo/live/native',
                       'genre': 'Animals'},
					   {'name': 'ET NOW',
                       'thumb': 'http://vignette1.wikia.nocookie.net/logopedia/images/b/bf/ET_Now.png/revision/latest?cb=20110930231639',
                       'video': 'http://etnowweblive-lh.akamaihd.net/i/ETNowweb_1@348070/master.m3u8',
                       'genre': 'Animals'},
					   {'name': 'NEWS WORLD INDIA',
                       'thumb': 'https://upload.wikimedia.org/wikipedia/en/8/83/News_World_India_Second_Logo_File.jpg',
                       'video': 'http://newsworldcloud.purplestream.in/newsworld/newsworld3-live.smil/playlist.m3u8',
                       'genre': 'Animals'}
					   
                      ],
			'MHDTVLIVE': [{'name': 'Sony ESPN HD1',
                      'thumb': 'http://www.vidsplay.com/vids/us_postal.jpg',
                      'video': 'http://www.vidsplay.com/vids/us_postal.mp4',
                      'genre': 'Cars'},
                     {'name': 'Traffic',
                      'thumb': 'http://www.vidsplay.com/vids/traffic1.jpg',
                      'video': 'http://www.vidsplay.com/vids/traffic1.avi',
                      'genre': 'Cars'},
                     {'name': 'Traffic Arrows',
                      'thumb': 'http://www.vidsplay.com/vids/traffic_arrows.jpg',
                      'video': 'http://www.vidsplay.com/vids/traffic_arrows.mp4',
                      'genre': 'Cars'}
                     ],
            'MOVIES': [{'name': 'Postal Truck',
                      'thumb': 'http://www.vidsplay.com/vids/us_postal.jpg',
                      'video': 'http://www.vidsplay.com/vids/us_postal.mp4',
                      'genre': 'Cars'},
                     {'name': 'Traffic',
                      'thumb': 'http://www.vidsplay.com/vids/traffic1.jpg',
                      'video': 'http://www.vidsplay.com/vids/traffic1.avi',
                      'genre': 'Cars'},
                     {'name': 'Traffic Arrows',
                      'thumb': 'http://www.vidsplay.com/vids/traffic_arrows.jpg',
                      'video': 'http://www.vidsplay.com/vids/traffic_arrows.mp4',
                      'genre': 'Cars'}
                     ],
            'TV SHOWS': [{'name': 'Chicken',
                      'thumb': 'http://www.vidsplay.com/vids/chicken.jpg',
                      'video': 'http://www.vidsplay.com/vids/bbqchicken.mp4',
                      'genre': 'Food'},
                     {'name': 'Hamburger',
                      'thumb': 'http://www.vidsplay.com/vids/hamburger.jpg',
                      'video': 'http://www.vidsplay.com/vids/hamburger.mp4',
                      'genre': 'Food'},
                     
                     ]}


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: list
    
	
	
    return VIDEOS.iterkeys() """
	
	url1 = getURL()
    VIDEOS = {'LIVE TV': [{'name': 'ABP News',
                       'thumb': 'http://www.media247.co.uk/bizasia/wp-content/uploads/2017/01/abpnewsnew001.jpg',
                       'video': 'http://hindiabp-lh.akamaihd.net/i/hindiabp1new_1@192103/master.m3u8',
                       'genre': 'Animals'},
                      {'name': 'ABP Ananda',
                       'thumb': 'https://pbs.twimg.com/profile_images/2265469431/mhfdk1dfs640hd35tox6_400x400.jpeg',
                       'video': 'http://bengaliabp-lh.akamaihd.net/i/abpbanglanew_1@192108/master.m3u8',
                       'genre': 'Animals'},
                      {'name': 'ETV Bangla',
                       'thumb': 'http://sim03.in.com/62/2e7599512bb9b51fce54dd72e1f02f9e_m.jpg',
                       'video': 'http://etvbanglalive-lh.akamaihd.net/i/etv_bangla_news_live_1@2289/index_3_av-p.m3u8?sd=10&play-only=primary&rebase=on&hdntl=exp=1479008971~acl=%2f*~data=hdntl~hmac=151ed96eca9cf183c67429750ada6122e1c1108f74716596b6703eed81a0c701',
                       'genre': 'Animals'},
					   {'name': 'NDTV 24x7',
                       'thumb': 'http://www.indiantelevision.com/sites/drupal7.indiantelevision.co.in/files/images/tv-images/2014/05/08/ndtv.jpg',
                       'video': 'http://ndtvstream-lh.akamaihd.net/i/ndtv_24x7_1@300633/index_352_av-p.m3u8',
                       'genre': 'Animals'},
					   {'name': 'NDTV INDIA HINDI',
                       'thumb': 'https://yt3.ggpht.com/-H95jY2ux2YQ/AAAAAAAAAAI/AAAAAAAAAAA/ZWe_3_BJ5sY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg',
                       'video': 'http://bglive-a.bitgravity.com/ndtv/indlo/live/native',
                       'genre': 'Animals'},
					   {'name': 'INDIA TV',
                       'thumb': 'http://1.bp.blogspot.com/-AMQZ-kBgxA4/T5DVOkqDO6I/AAAAAAAA2XU/yVqULj-ctv0/s1600/India-TV-Logo.jpg',
                       'video': 'http://indiatvnews-lh.akamaihd.net/i/ITV_1@199237/index_3_av-p.m3u8',
                       'genre': 'Animals'},
					   {'name': 'IBN 7',
                       'thumb': 'http://www.india-forums.com/tellybuzz/images/uploads/671_IBN-7-TV-Channel-India-Logo.jpg',
                       'video': 'http://ibn7_hls-lh.akamaihd.net/i/ibn7_hls_n_1@174951/index_3_av-p.m3u8',
                       'genre': 'Animals'},
					   {'name': 'NEWS 24',
                       'thumb': 'http://tvimages.burrp.com/images/channels2/news/news24.png',
                       'video': 'http://d20vhs4gtao945.cloudfront.net/bagnetworks/ngrp:news24_all/chunklist_b634000.m3u8',
                       'genre': 'Animals'},
					   {'name': 'INDIA NEWS',
                       'thumb': 'https://upload.wikimedia.org/wikipedia/en/4/49/India-news-logo.gif',
                       'video': 'http://indiatvnews-lh.akamaihd.net/i/ITV_1@199237/index_3_av-b.m3u8?sd=10&rebase=on',
                       'genre': 'Animals'},
					   {'name': 'NEWS X HD',
                       'thumb': 'http://images.mytm.in/u1341/3251071.jpg',
                       'video': 'http://newsx.live-s.cdn.bitgravity.com/cdn-live/_definst_/newsx/live/newsxnew.smil/chunklist_w218860994_b512000.m3u8',
                       'genre': 'Animals'},					   
					   {'name': 'TV100 NEWS',
                       'thumb': 'http://livetvstream247.tk/wp-content/uploads/2016/03/tv100-news-logo.jpg',
                       'video': 'rtmp://capcobroadcaststream.in/guj//tv100.sdp_aac',
                       'genre': 'Animals'},					   
					   {'name': 'NEWS NATION',
                       'thumb': 'http://extradesimovies.com/wp-content/uploads/2016/10/news-nation-Live-logo.png',
                       'video': 'rtmp://54.255.176.172/live/newsnation_720p',
                       'genre': 'Animals'},
					   {'name': 'NEWS STATE',
                       'thumb': 'https://newsnation1.s3.amazonaws.com/images/2014/02/19/740527207-UP.jpg',
                       'video': 'rtmp://54.255.176.172/trans/nnstate_720p',
                       'genre': 'Animals'},
					   {'name': 'JOO MUSIC',
                       'thumb': 'https://lh4.ggpht.com/Gmztx1CSvrLf3GsE8N67w5_THsaI8mVqPVFUW7l4Hor_71PTBnobOlBnCniWMmXxJDI=w300',
                       'video': 'http://wowzacontrol.com:1935/8038/8038/chunklist_w1610289693.m3u8',
                       'genre': 'Animals'},
					   {'name': 'E24',
                       'thumb': 'http://www.fetchlogos.com/wp-content/uploads/2015/10/E-24-Logo.jpg',
                       'video': 'http://d3ibnxavurfby0.cloudfront.net/bagnetworks/ngrp:e24_all/playlist.m3u8',
                       'genre': 'Animals'},					   
					   {'name': 'KISS TV',
                       'thumb': 'http://www.webtvstreams.com/wp-content/uploads/2014/04/Kiss-Tv.jpg',
                       'video': 'http://fms113.mediadirect.ro:1937/live3/_definst_/kiss_low/playlist.m3u8?publisher=83&token=c31533f4f4f1f6154428aa3cfbcbecbf41719aa5baadd852',
                       'genre': 'Animals'},					   
					   {'name': 'DD NEWS',
                       'thumb': 'https://upload.wikimedia.org/wikipedia/commons/7/77/DD_News_Logo_2015.jpg',
                       'video': 'http://nicls1-lh.akamaihd.net/i/ddnews_1@409133/master.m3u8',
                       'genre': 'Animals'},	
					   {'name': 'NDTV PRIME',
                       'thumb': 'http://www.exchange4media.com/storyimages/fs_57129.jpg',
                       'video': 'http://bglive-a.bitgravity.com/ndtv/prolo/live/native',
                       'genre': 'Animals'},
					   {'name': 'ET NOW',
                       'thumb': 'http://vignette1.wikia.nocookie.net/logopedia/images/b/bf/ET_Now.png/revision/latest?cb=20110930231639',
                       'video': 'http://etnowweblive-lh.akamaihd.net/i/ETNowweb_1@348070/master.m3u8',
                       'genre': 'Animals'},
					   {'name': 'NEWS WORLD INDIA',
                       'thumb': 'https://upload.wikimedia.org/wikipedia/en/8/83/News_World_India_Second_Logo_File.jpg',
                       'video': 'http://newsworldcloud.purplestream.in/newsworld/newsworld3-live.smil/playlist.m3u8',
                       'genre': 'Animals'}
					   
                      ],
			'MHDTVLIVE': [{'name': 'Sony ESPN HD1',
                      'thumb': 'http://www.vidsplay.com/vids/us_postal.jpg',
                      'video': 'http://www.vidsplay.com/vids/us_postal.mp4',
                      'genre': 'Cars'},
                     {'name': 'Traffic',
                      'thumb': 'http://www.vidsplay.com/vids/traffic1.jpg',
                      'video': 'http://www.vidsplay.com/vids/traffic1.avi',
                      'genre': 'Cars'},
                     {'name': 'Traffic Arrows',
                      'thumb': 'http://www.vidsplay.com/vids/traffic_arrows.jpg',
                      'video': 'http://www.vidsplay.com/vids/traffic_arrows.mp4',
                      'genre': 'Cars'}
                     ],
            'MOVIES': [{'name': 'Postal Truck',
                      'thumb': 'http://www.vidsplay.com/vids/us_postal.jpg',
                      'video': 'http://www.vidsplay.com/vids/us_postal.mp4',
                      'genre': 'Cars'},
                     {'name': 'Traffic',
                      'thumb': 'http://www.vidsplay.com/vids/traffic1.jpg',
                      'video': 'http://www.vidsplay.com/vids/traffic1.avi',
                      'genre': 'Cars'},
                     {'name': 'Traffic Arrows',
                      'thumb': 'http://www.vidsplay.com/vids/traffic_arrows.jpg',
                      'video': 'http://www.vidsplay.com/vids/traffic_arrows.mp4',
                      'genre': 'Cars'}
                     ],
            'TV SHOWS': [{'name': 'Chicken',
                      'thumb': 'http://www.vidsplay.com/vids/chicken.jpg',
                      'video': 'http://www.vidsplay.com/vids/bbqchicken.mp4',
                      'genre': 'Food'},
                     {'name': 'Hamburger',
                      'thumb': 'http://www.vidsplay.com/vids/hamburger.jpg',
                      'video': 'http://www.vidsplay.com/vids/hamburger.mp4',
                      'genre': 'Food'},
                     
                     ]}
    return VIDEOS.iterkeys()
	
def getURL()
    return 'http://hindiabp-lh.akamaihd.net/i/hindiabp1new_1@192103/master.m3u8'
def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEO[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEO[category][0]['thumb'],
                          'icon': VIDEO[category][0]['thumb'],
                          'fanart': VIDEO[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # http://mirrors.xbmc.org/docs/python-docs/15.x-isengard/xbmcgui.html#ListItem-setInfo
        list_item.setInfo('video', {'title': category, 'genre': category})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        list_item.setInfo('video', {'title': video['name'], 'genre': video['genre']})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/vids/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
