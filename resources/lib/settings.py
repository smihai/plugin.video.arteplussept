"""Add-on settings"""

import dataclasses

languages = ['fr', 'de', 'en', 'es', 'pl', 'it']
qualities = ['SQ', 'EQ', 'HQ']
loglevel = ['DEFAULT', 'API']


@dataclasses.dataclass
class Settings:
    """Add-on settings"""
    def __init__(self, plugin):
        # Language used to query arte api
        # defaults to fr
        self.language = plugin.get_setting(
            'lang', choices=languages) or languages[0]
        # Quality of the videos
        # defaults to SQ
        self.quality = plugin.get_setting(
            'quality', choices=qualities) or qualities[0]
        # Should the plugin display all available streams for videos?
        # defaults to False
        self.show_video_streams = plugin.get_setting(
            'show_video_streams', bool) or False
        # Arte TV user name
        # defaults to empty string to return false with if not str
        self.username = plugin.get_setting(
            'username') or ""
        # Enable additional logs managed by plugin : API messages
        self.loglevel = plugin.get_setting(
            'loglevel', choices=loglevel) or loglevel[0]
