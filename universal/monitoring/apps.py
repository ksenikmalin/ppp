from django.apps import AppConfig


class MonitoringConfig(AppConfig):
    name = 'monitoring'

class StatisticsConfig(AppConfig):
    name = 'statistics'

class DiagnosticConfig(AppConfig):
    name = 'diagnostic'

class CustomizationConfig(AppConfig):
    name = 'customization'

class HelpConfig(AppConfig):
    name = 'help'

class ReferenceConfig(AppConfig):
    name = 'reference'

class ContractConfig(AppConfig):
    name = 'contract'

class ProfileConfig(AppConfig):
    name = 'profile'

class ErrorsConfig(AppConfig):
    name = 'errors'

class IndexConfig(AppConfig):
    name = 'index'