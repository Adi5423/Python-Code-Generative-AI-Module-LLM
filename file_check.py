import os

filename = 'rsyncd.conf'
filepath = os.path.join(os.getcwd(), filename)

with open(filepath) as fp:
    cfg.read_file(itertools.chain(['[global]\n'], fp), source=filename)

print(cfg.items('global'))
