from agents.config import get_logger
import time

log = get_logger('research_agent')

def gather_research(topic: str):
    log.info(f'Starting research on topic: {topic}')
    time.sleep(1)
    findings = f'Preliminary insights about {topic}: requires deeper review.'
    log.info(f'Research completed for topic: {topic}')
    return findings

def lambda_handler(event=None, context=None):
    topic = event.get('topic', 'general inquiry') if event else 'general inquiry'
    result = gather_research(topic)
    return {'status': 'success', 'data': result}

if __name__ == '__main__':
    log.info('Research Agent initiated locally.')
    output = gather_research('AI-Ops automation design')
    log.info(f'Output: {output}')
