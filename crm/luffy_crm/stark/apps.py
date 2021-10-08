from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class StarkConfig(AppConfig):
    name = 'stark'

    def ready(self):
        autodiscover_modules('stark')  # 从已经注册的app中找到stark插件并启动
