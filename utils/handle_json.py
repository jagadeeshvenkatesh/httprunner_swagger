#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 2019年9月29日
@author: qguan
@File: handle_json.py
"""

import json

import yaml

from utils.logger import log as logger


def get_json(path, field=''):
    """
    get json file datas
    :param path:
    :param field:
    :return:
    """
    with open(path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        if field:
            data = json_data.get(field)
            return data
        else:
            return json_data


def write_data(res, json_path):
    """
    handle params write data to json file
    :param res:
    :param json_path:
    :return:
    """
    if isinstance(res, dict) or isinstance(res, list):
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False, sort_keys=True, indent=4)
        logger.info('Interface Params Total：{} ,write to json file successfully!'.format(len(res)))
    else:
        logger.error('\n:{} Params is not dict.\n'.format(write_data.__name__))


def json_to_yaml(json_file):
    """
    supported json to yaml file
    """
    if json_file.endswith("json"):
        with open(json_file, "r") as pf:
            json_to_dict = json.loads(pf.read())
        yaml_file = json_file.replace(".json", ".yaml")
        with open(yaml_file, "w") as fp:
            yaml.safe_dump(json_to_dict, stream=fp, default_flow_style=False)
            logger.info("json  to yaml success!!!")
    else:
        logger.info("The file does not end with a JSON suffix!!!")


def yaml_to_json(yaml_file):
    """
    yaml to json file
    """
    if yaml_file.endswith("yaml"):
        with open(yaml_file, "r") as pf:
            # First convert yaml to dict format
            yaml_to_dict = yaml.load(pf, Loader=yaml.FullLoader)
            dict_to_json = json.dumps(yaml_to_dict, sort_keys=False, indent=4, separators=(',', ': '))
        json_file = yaml_file.replace(".yaml", ".json")
        with open(json_file, "w") as fp:
            fp.write(dict_to_json)
            logger.info("yaml to json success!!!")
    else:
        logger.info("The file does not end with a YAML suffix!!!")
