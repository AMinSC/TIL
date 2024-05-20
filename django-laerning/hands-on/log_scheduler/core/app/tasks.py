from core.celery import app

import logging

logger = logging.getLogger('request')

@app.task()
def write_log():
    logger.info('Scheduled Log')
    logger.error('Scheduled Log')
