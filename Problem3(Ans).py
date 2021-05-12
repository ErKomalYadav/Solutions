import logging

a = 50
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')
