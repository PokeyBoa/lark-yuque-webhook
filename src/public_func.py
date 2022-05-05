# -*- coding: UTF-8 -*-
# import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import NICK_NAME
import random


def empty_dialogue() -> str:
    choose_reply = ['����, û����������! ���һ�߻����ȥ��!', 
                    '���Ǳ�������? ���ز�˵��, ����ˣ��å!', 
                    '�����, �����������, ��ҪѰ�����: /help',
                    '����׬�ҵ�СĿ��, ʮ�������µ���Ŀ��Ҫ������!',
                    f'��ò����, ���� \'{NICK_NAME}\', ������ظ���!']
    res = random.choice(choose_reply)
    return res


def bot_msg_talking(content: dict, flag: int = 1) -> dict:
    """
    flag: 1 means 'p2p' (default)
          0 means 'group'
    """
    if not content:
        data = {'text': '��̫��, ��������ѽ!'}
    else:
        data = {}
        info = content.get('text')
        if not info:
            data = {'text': '�����Ի���Ϊ����, ��Ǹ�����������...'}
        else:
            if flag == 1:
                # �龰0
                data = {'text': "���ڽ�ɶ����?"}

                # �龰1
                keyworks1 = ['hhh', 'hehe', '�Ǻ�']
                for i in keyworks1:
                    if i in info:
                        data = {'text': '�Ǻ����ү!\n������һ��?'}
                        break

                # �龰2
                keyworks2 = ['�ڸ�ɶ', '��ɶ��', '������', '�ڸ���', '�ڸ�ɶ', '��ɶ��', '��ɶ��', '��ʲô', '��ʲô', '��ʲô', '����ô']
                for i in keyworks2:
                    if i in info:
                        data = {'text': 'ˢ����!'}
                        break

                # �龰3
                keyworks3 = ['ha', 'o', 'en', '��', 'Ŷ', '��', '��', '��', '��', '��', '��', '��']
                for i in keyworks3:
                    if (info in i*3) or (i in info):
                        data = {'text': f'{NICK_NAME}���ġ�'}
                        break

                # �龰4
                keyworks4 = ['hello', 'hi', '���']
                for i in keyworks4:
                    if i in info.lower():
                        data = {'text': 'Hi Bro ~\nʹ�� /help ��������ѽ!'}
                        break

            elif flag == 0:
                if info == "/help" or info == NICK_NAME:
                    # ��Ҫʹ�ÿ�Ƭ
                    data = {'text': '���Ҹ���?'}
    return data


if __name__ == '__main__':
    bot_msg_talking({})

