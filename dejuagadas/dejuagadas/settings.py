# Scrapy settings for dejuagadas project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'dejuagadas'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['dejuagadas.spiders']
NEWSPIDER_MODULE = 'dejuagadas.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
FEED_URI = '/home/pablo/desarrollo/juegos_de_azar/datos/%(name)s/%(time)s_sin_proc.csv'
FEED_FORMAT= 'csv'

