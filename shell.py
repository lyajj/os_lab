import os
import logging

from vim import Vim
from utils import not_exist_guard, exist_guard

logging.basicConfig(filename='fs_journal.log', level=logging.INFO)

@exist_guard
def create_file(filepath):
    logging.info('create ' + filepath)
    with open(filepath, 'w') as f:
        f.write('\n')


@not_exist_guard
def edit_file(filepath):
    logging.info('update ' + filepath)
    vim = Vim(filepath)
    vim.exec()


@not_exist_guard    
def output_file(filepath):
    with open(filepath, 'r') as f:
        print(f.read())


@not_exist_guard    
def delete_file(filepath):
    logging.info('remove ' + filepath)
    os.remove(filepath)


def parse_cmd(cmd_string):
    split = cmd_string.split(' ')

    cmd = split[0]
    cmd_args = split[1:]

    if (cmd == ''):
        pass
    elif (cmd == 'ls'):
        print(' '.join(os.listdir()))
    elif (cmd == 'touch'):
        create_file(cmd_args)
    elif (cmd == 'vim'):
        edit_file(cmd_args)
    elif (cmd == 'cat'):
        output_file(cmd_args)
    elif (cmd == 'rm'):
        delete_file(cmd_args)
    else:
        print('Unknown command!')
