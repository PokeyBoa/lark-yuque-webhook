# -*- coding: UTF-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import BASE_PATH
import json

json_filepath = os.path.join(BASE_PATH, 'meg_card', 'files', 'assistant_card.json')


def __assistant_card() -> dict:
    cards = {
        "config": {
            "wide_screen_mode": True
        },
        "header": {
            "template": "purple",
            "title": {
                "content": "šŖ¶ čÆ­é - č®©åå°ēäøŖä½ļ¼ä¹ę„ęčŖå·±ēę°å­č±å­ āļø",
                "tag": "plain_text"
            }
        },
        "elements": [{
            "extra": {
                "alt": {
                    "content": "",
                    "tag": "plain_text"
                },
                "img_key": "img_v2_d24d654b-21cb-4858-9edf-1ff1e927dd9g",
                "tag": "img"
            },
            "tag": "div",
            "text": {
                "content": "š  čÆ­éļ¼š ęäøēåØēŗæęę”£ē¼č¾äøååå·„å·ć\nš  čÆ­éå°å©ęļ¼åå āå°éåå­¦āćå°éčÆēå¾ē„å„ š£ čæčäøå®¶å¤§åē¾ęÆļ¼ęēä¹å¹“ē³»å BAT čååŗåļ¼å¤“ę” *Lark Bot*, éæé *YuQue*, č¾č®Æ *Cloud Infra* ęå”ļ¼ć",
                "tag": "lark_md"
            }
        }, {
            "alt": {
                "content": "",
                "tag": "plain_text"
            },
            "img_key": "img_v2_aab78eaf-51bc-4f62-9ea5-8c521c2150ag",
            "tag": "img"
        }, {
            "fields": [{
                "is_short": True,
                "text": {
                    "content": "**äø­ęå­¦åļ¼**\n[čÆ­é](https://www.yuque.com/about/careers)",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "**č±ęåē§°ļ¼**\n[Yu Que](https://www.yuque.com/about/)",
                    "tag": "lark_md"
                }
            }, {
                "is_short": False,
                "text": {
                    "content": "",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "**ćčÆ­ćš¬ļ¼**\n[äŗŗäøäŗŗé«ęēę²éę¹å¼](https://baike.baidu.com/item/%E8%AF%AD%E9%9B%80/24190957?fr=aladdin)",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "**āļøćéćļ¼**\n[č±”å¾ āę¬¢ä¹ćåęćē¾äø½āļ¼č½»ēµē¾č§](https://baike.baidu.com/item/%E8%AF%AD%E9%9B%80/24190957?fr=aladdin)",
                    "tag": "lark_md"
                }
            }, {
                "is_short": False,
                "text": {
                    "content": "",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "**APP åŗēØļ¼**[@å°éåå­¦ (v1.0.0)](https://github.com/PokeyBoa/lark_yuque_webhook)",
                    "tag": "lark_md"
                }
            }],
            "tag": "div"
        }, {
            "tag": "hr"
        }, {
            "extra": {
                "alt": {
                    "content": "",
                    "tag": "plain_text"
                },
                "img_key": "img_v2_03706b68-884d-415a-9552-0361849b210g",
                "tag": "img"
            },
            "tag": "div",
            "text": {
                "content": "**å©ęåē**\n\nšø **åŗēØļ¼**Yuque Assistant\t\t\t       š¹ **ē±å„½ļ¼**@å°éåå­¦ éŖå å\nšø **åēļ¼**'/help' or call my name\t\t       š¹ **č½åļ¼**Wiki åŗę“ę° ā”ļø é£ä¹¦ē¾¤ē»\n",
                "tag": "lark_md"
            }
        }, {
            "tag": "hr"
        }, {
            "fields": [{
                "is_short": False,
                "text": {
                    "content": "**Repo Webhook**",
                    "tag": "lark_md"
                }
            }, {
                "is_short": False,
                "text": {
                    "content": "",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "[ååøåå®¹ ā](https://open.feishu.cn)",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "[ę“ę°åå®¹ ā](https://open.feishu.cn)",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "[åč”ØčÆč®ŗ ā](https://open.feishu.cn)",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "[ę“ę°čÆč®ŗ ā](https://open.feishu.cn)",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "[åå¤čÆč®ŗ ā](https://open.feishu.cn)",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "[čÆå®”åč½ ā](https://open.feishu.cn)",
                    "tag": "lark_md"
                }
            }],
            "tag": "div"
        }, {
            "tag": "hr"
        }, {
            "elements": [{
                "alt": {
                    "content": "",
                    "tag": "plain_text"
                },
                "img_key": "img_v2_ce77be32-d666-4488-89e8-9b7ca4991b0g",
                "tag": "img"
            }, {
                "content": "ä»„äøéØååå®¹ęčŖ Baidu ē¾ē§čÆę”",
                "tag": "plain_text"
            }],
            "tag": "note"
        }]
    }
    return cards


def __save_file() -> None:
    res = __assistant_card()
    with open(json_filepath, mode='w', encoding='utf-8') as f:
        json.dump(res, f)
    print(res)


def rjson() -> dict:
    with open(json_filepath, mode='rt', encoding='utf-8') as f:                                                                                                                                                              
        content = json.load(f)
    return content


if __name__ == '__main__':
    # __save_file()
    res = rjson()
    print(res)

