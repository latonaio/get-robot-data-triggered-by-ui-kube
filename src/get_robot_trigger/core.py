#!/usr/bin/env python3
# coding: utf-8

# Copyright (c) 2019-2020 Latona. All rights reserved.

import json
import os

from aion.microservice import Options, main_decorator
from aion.kanban import Kanban
from aion.logger import initialize_logger, lprint_exception

JSON_PATH = "/var/lib/aion/Data/control-yaskawa-robot-r_1/command_list.json"
SERVICE_NAME = "get-robot-data-triggered-by-ui"
initialize_logger(SERVICE_NAME)


@main_decorator(SERVICE_NAME)
def main_with_kanban(opt: Options):

    conn = opt.get_conn()
    num = opt.get_number()
    
    # kanban: Kanban = conn.get_one_kanban(SERVICE_NAME, num)
    for kanban in conn.get_kanban_itr(SERVICE_NAME, num):
        metadata = kanban.get_metadata()
        add_list = metadata.get('add_list')
        remove_list = metadata.get('remove_list')

        # Jsonファイルをロードする
        with open(JSON_PATH, 'r') as f:
            command_list = json.load(f)
            new_command_list = []

            for command in command_list.get('command'):
                new_command = command.copy()

                for row in remove_list if remove_list else []:
                    if command.get('command') == row['command']:
                        for rm in row['arrayNo']:
                            if rm in new_command['arrayNo']:
                                new_command['arrayNo'].remove(rm)

                for row in add_list if add_list else []:
                    print(command.get('command'), row['command'])
                    if command.get('command') == row['command']:
                        for ad in row['arrayNo']:
                            new_command['arrayNo'].append(ad)

                new_command['arrayNo'] = sorted(list(set(new_command['arrayNo'])))
                new_command_list.append(new_command)

        with open(JSON_PATH, 'w') as f:
            json.dump({'command': new_command_list}, f, indent=4)

        conn.output_kanban(
            result=True,
            process_number=num,
        )


if __name__ == "__main__":
    main_with_kanban()
