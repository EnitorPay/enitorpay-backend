from agents.config import get_logger
import datetime
import os

log = get_logger('docbuilder_agent')

def generate_readme(metadata: dict):
    log.info('Generating README.md content...')
    name = metadata.get('project_name', 'EnitorPay')
    version = metadata.get('version', '0.0.1')
    timestamp = datetime.datetime.utcnow().isoformat()

    readme_content = f"""# {name}

**Version:** {version}

Generated automatically by DocBuilder Agent.

_Last updated: {timestamp} UTC_
"""
    os.makedirs('docs', exist_ok=True)
    with open('docs/README.md', 'w') as f:
        f.write(readme_content)

    log.info(f'Readme.md updated for {name}.')
    return readme_content

def lambda_handler(event=None, context=None):
    return {'status': 'success', 'content': generate_readme(event or {})}

if __name__ == '__main__':
    log.info('DocBuilder Agent initiated locally.')
    generate_readme({'project_name': 'EnitorPay', 'version': '0.2.5-safe'})
