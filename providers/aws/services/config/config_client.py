from providers.aws.lib.audit_info.audit_info import current_audit_info
from providers.aws.services.config.config_service import Config

config_client = Config(current_audit_info)
