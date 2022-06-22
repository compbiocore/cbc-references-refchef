#!/usr/bin/env python3

import json

import oyaml as yaml

with open('new_ref.yaml') as f:
    data = f.read()
    datajson = json.loads(data)
    # if yaml_level is indices,
    yaml_level = datajson.get('level')
    yaml_commands = datajson.get('Commands')
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
                                 'commands': datajson.get('Commands').split(', ')
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
                                 'commands': datajson.get('Commands').split(', ')
                             }
                         ]
                     }
                 }
        }
    out = open('new_parsed.yaml', 'w+')
    yaml.dump(yaml_dict, out, allow_unicode=True, width=100000)