#!/usr/bin/env python3
import json
import re

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