'''
Created on Jun 22, 2015

@author: dgraja
'''
import locale
import sys
import os


def is_enabled_lang(lang):
    return lang is not None


def fetch_locale():
    '''prepare l10n'''

    loc = None
    lang = None
    if sys.platform == 'darwin':
        from CoreFoundation import *
        import objc
        try:
            langs = objc.lookUpClass("NSLocale").preferredLanguages()
            lang = str(langs.objectAtIndex_(0))
            lang = str(lang).replace('-', '_')
            if not is_enabled_lang(lang):
                lang ='en'
            locale.setlocale(locale.LC_ALL, locale.normalize(lang))
        except Exception, e:
            locale.setlocale(locale.LC_ALL, '')
        # Only first part of locale id is required (example: es if es-ES)
        if lang.find('_')>=0:
            lang = lang.split('_')[0]
    else:
        default_loc = locale.getdefaultlocale()
        loc = 'en_US'
        if default_loc and len(default_loc) > 0 and is_enabled_lang(default_loc[0]):
            loc = default_loc[0]
        lang = str(loc).split('_')[0]
    return loc, lang


def main():
    loc, lang = fetch_locale()
    print loc
    print lang

if __name__ == '__main__':
    main()
    pass
