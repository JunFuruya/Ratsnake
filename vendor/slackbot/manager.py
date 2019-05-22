# -*- coding: utf-8 -*-

import os
from glob import glob
from six import PY2
from importlib import import_module

import g
# 20180515 change include path from "slackbot" to "vendor.slackbot"
from vendor.slackbot import settings
from vendor.slackbot.utils import to_utf8


class PluginsManager(object):
    def __init__(self):
        pass

    commands = {
        'respond_to': {},
        'listen_to': {},
        'default_reply': {}
    }

    def init_plugins(self):
        if hasattr(settings, 'PLUGINS'):
            plugins = settings.PLUGINS
        else:
            # 20180515 change include path from "slackbot" to "vendor.slackbot"
            plugins = 'vendor.slackbot.plugins'

        for plugin in plugins:
            self._load_plugins(plugin)

    def _load_plugins(self, plugin):
        path_name = None

        if PY2:
            import imp

            for mod in plugin.split('.'):
                if path_name is not None:
                    path_name = [path_name]
                _, path_name, _ = imp.find_module(mod, path_name)
        else:
            from importlib.util import find_spec as importlib_find

            # 2019/05/16 パスを強制的に指定（指定しないとsite-packageを読みに行くため）
            #path_name = importlib_find(plugin)
            # TODO configからPLUGINSを読み込む必要がなくなった
            path_name = os.path.dirname(os.path.abspath(__file__))+'\plugins'
            #try:
                #path_name = path_name.submodule_search_locations[0]
            #except TypeError:
                #path_name = path_name.origin

        module_list = [plugin]
        if not path_name.endswith('.py'):
            module_list = glob('{}/[!_]*.py'.format(path_name))
            module_list = ['.'.join((plugin, os.path.split(f)[-1][:-3])) for f
                           in module_list]
        for module in module_list:
            try:
                import_module(module)
            except:
                g.log.error('Failed to import {}'.format(module))

    def get_plugins(self, category, text):
        has_matching_plugin = False
        if text is None:
            text = ''
        for matcher in self.commands[category]:
            m = matcher.search(text)
            if m:
                has_matching_plugin = True
                yield self.commands[category][matcher], to_utf8(m.groups())

        if not has_matching_plugin:
            yield None, None
