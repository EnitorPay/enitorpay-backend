from agents.config import get_logger
import subprocess

log = get_logger('infrawatch_agent')

def check_service_status(service_name: str):
    log.info(f'Checking status of service: {service_name}')
    try:
        result = subprocess.run(['sudo', 'systemctl', 'status', service_name, '--no-pager'], capture_output=True, text=True)
        if result.returncode == 0:
            log.info(f'Service {service_name} is active.')
            return {'service': service_name, 'status': 'active', 'details': result.stdout}
        else:
            log.warning(f'Service {service_name} is not active.')
            return {'service': service_name, 'status': 'inactive', 'details': result.stderr}
    except Exception as e:
        log.error(f'Failed to check service {service_name}: {e}')
        return {'service': service_name, 'error': str(e)}

def lambda_handler(event=None, context=None):
    service = event.get('service', 'enitorpay') if event else 'enitorpay'
    return check_service_status(service)

if __name__ == '__main__':
    log.info('InfraWatch Agent initiated locally.')
    result = check_service_status('enitorpay')
    log.info(f'Status Result: {result}')
