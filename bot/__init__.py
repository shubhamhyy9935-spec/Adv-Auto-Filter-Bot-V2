#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID =39690918
API_HASH ="4f1ab2b4a61d2dae7ac34db4cf7ab2f5"
BOT_TOKEN ="8550404877:AAFblNn_wy0lllKuiFtFj8t3xgrHYXXlkIs"
DB_URI = "mongodb+srv://Tonicveil:bhaimerajay98@cluster0.vmckaf5.mongodb.net/?retryWrites=true&w=majority"
USER_SESSION = None


VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)



