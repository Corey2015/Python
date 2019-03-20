# -*- coding: utf-8 -*-
import  logging
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                   # ilename='parser_result.log',
                    #filemode='w'
                   )
logger  = logging.getLogger(__name__)

def main():
    logger.warning("warning 1")


if __name__ == "__main__":
    main()