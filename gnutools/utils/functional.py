import json
import random
import string
import numpy as np
import os
from gnutools.fs import listfiles, parent, name, contain_filter
from argparse import Namespace


def RecNamespace(d):
    results = {}
    for k, v in d.items():
        if type(v) == dict:
            v = RecNamespace(v)
        results[k] = v
    return Namespace(**results)


def RecDict(d):
    results = {}
    for k, v in vars(d).items():
        if type(v) == Namespace:
            v = RecDict(v)
        results[k] = v
    return dict(results)

def system(command):
    """
    Execute a system command
    :param command:
    :return:
    """
    os.system(command)


def json_labels(labels_path, normalizer=None):
    """
    Read a json file to extract the labels in it

    :param labels_path:
    :param normalizer:
    :return list:
    """
    # Load the labels
    with open(os.path.realpath(labels_path)) as label_file:
        labels = str(' '.join(json.load(label_file)))
        labels = normalizer(labels) if normalizer is not None else labels
        labels = labels.split(" ")
        labels = [l for l in labels if len(l) > 0]
        labels.append(" ")
        return labels


def inverse_dict(root=None, filters=None, array=None, exclude=None):
    """
    Inverse a dictionary of files

    :param root: directory to scan
    :param filters: filters or keywords to include in the search
    :param array:
    :param exclude: filterss or keywords to exclude in the search
    :return dict:
    """
    assert ((root is not None) | (array is not None))
    _idict = {}
    if array is not None:
        for f in array:
            _idict[name(f)] = parent(f)
    else:
        for dir, _, files in os.walk(root):
            condition = True
            if exclude is not None:
                if contain_filter(dir, exclude):
                    condition = False
            if condition:
                for file in files:
                    if ((contain_filter(file, filters)) | (filters is None)):
                        if exclude is None:
                            _idict[file] = dir
                        elif not contain_filter(file, exclude):
                            _idict[file] = dir
    return _idict


def regroup(entries, index=0):
    """
    Convert an array into a dictionary by specifying a column index

    :param files:
    :param index:
    :return dictionary:
    """
    d = {}
    for f in entries:
        f = list(f)
        key = f[index]
        del f[index]
        try:
            d[key].append(f[:])
        except:
            d[key] = [f[:]]
    for key, values in d.items():
        d[key] = list(np.array(values).reshape(-1, ))
    return d


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """
    Generate a random id

    :param size:
    :param chars:
    :return string:
    """
    return ''.join(random.choice(chars) for _ in range(size))


# Gather all files together
def regroup_by_parent(dir_data, patterns=["*"]):
    """
    Look for files with pattern in directoryu and regroup by parent directory

    :param dir_data:
    :param patterns:
    :return dictionary:
    """
    files = []
    for pattern in patterns:
        files = files + listfiles(root=dir_data, patterns=[pattern])
    data = {}
    for file in files:
        try:
            data[parent(file)].append(file)
        except:
            data[parent(file)] = [file]
    return data

