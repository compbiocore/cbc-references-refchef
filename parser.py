#!/usr/bin/env python3
import json
import re
from urllib.request import urlopen

import oyaml as yaml

with open('new_ref.yaml') as f:
    data = f.read()
    datajson = json.loads(data)
    # if yaml_level is indices,
    yaml_level = datajson.get('level')
    yaml_commands = datajson.get('Commands').rstrip()
    commands = re.split('\n|, ', yaml_commands)
    if 'src' in datajson:
        yaml_dict = {
            datajson.get('name'):
                {'metadata':
                     {'name': datajson.get('name'),
                      'common_name': datajson.get('common'),
                      'custom': datajson.get('custom'),
                      'description': datajson.get('description'),
                      'downloader': 'joselynn wallace',
                      'ncbi_taxon_id': datajson.get('taxon_id'),
                      'ensembl_release_number': datajson.get('ensembl_rel'),
                      'accession':
                          {'genbank': datajson.get('genbank'),
                           'refseq': datajson.get('refseq')},
                      'organism': datajson.get('organism'),
                      'organization': datajson.get('organization'),
                      'category': datajson.get('category')
                      },
                 'levels':
                     {yaml_level:
                         [
                             {
                                 'component': datajson.get('component'),
                                 'complete':
                                     {'status': 'false'},
                                 'src': datajson.get('src'),
                                 'commands': commands
                             }
                         ]
                     }
                 }
        }
    else:
        yaml_dict = {
            datajson.get('name'):
                {'metadata':
                     {'name': datajson.get('name'),
                      'common_name': datajson.get('common'),
                      'custom': datajson.get('custom'),
                      'description': datajson.get('description'),
                      'downloader': 'joselynn wallace',
                      'ncbi_taxon_id': datajson.get('taxon_id'),
                      'ensembl_release_number': datajson.get('ensembl_rel'),
                      'accession':
                          {'genbank': datajson.get('genbank'),
                           'refseq': datajson.get('refseq')},
                      'organism': datajson.get('organism'),
                      'organization': datajson.get('organization'),
                      'category': datajson.get('category')
                      },
                 'levels':
                     {yaml_level:
                         [
                             {
                                 'component': datajson.get('component'),
                                 'complete':
                                     {'status': 'false'},
                                 'commands': commands
                             }
                         ]
                     }
                 }
        }
    out = open('new_parsed.yaml', 'w+')
    yaml.dump(yaml_dict, out, allow_unicode=True, width=100000)


def url_valid(commands: list) -> dict :
    '''
    Checks if the URL(s) in commands is still valid.

    Parameters:
    commands -- the list of commands within which the URL(s) are contained

    Returns:
    A dictionary containing the URL(s) as keys and a boolean of whether they are valid or not as the associated values
    '''
    url_dict = {}
    for command in commands:
        for arg in command.split():
            if re.search("^http", arg):
                try:
                    urlopen(arg)
                except:
                    url_dict[arg] = False
                    continue
                url_dict[arg] = True
    return url_dict