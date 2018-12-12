import hlt
import logging
import numpy as np 
import pandas as pd 
import random
import os

from collections import OrderedDict

VERSION = 1

HM_ENT_FEATURES = 5
PCT_CHANGE_CHANCE = 30
DESIRED_SHIP_COUNT = 20

game = hlt.Game('Mim{}'.format(VERSION))
logging.info('MimBot-{} Start'.format(VERSION))

ship_plans = {}

if os.path.exists('c{}_input.vec'.format(VERSION)):
	os.remove('c{}_input.vec'.format(VERSION))

if os.path.exists('c{}_output.vec'.format(VERSION)):
	os.remove('c{}_output.vec'.format(VERSION))
