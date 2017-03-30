# -*- coding: utf-8 -*-
# 双色球的中奖率，还是写代码比较好

import random


# 随便生成一组红球和蓝球
def random_money():
    red_ball = [str(i) if i > 9 else '0' + str(i) for i in random.sample(range(1, 34), 6)]
    blue_ball = random.randint(1, 16)
    blue_ball = str(blue_ball) if blue_ball > 9 else '0' + str(blue_ball)
    return red_ball, blue_ball


# 多少个数字是一样的
def equal_number(right_list, mine_list):
    result = 0
    for i in right_list:
        if i in mine_list:
            result += 1
    return result


# 判断有没有中奖
def funds_level(right_list, mine_list):
    number = equal_number(right_list['red'], mine_list['red'])
    if right_list['blue'] != mine_list['blue']:
        if number == 6:
            return {'success': True, 'message': '二等奖', 'level': 2}
        elif number == 5:
            return {'success': True, 'message': '四等奖', 'level': 4}
        elif number == 4:
            return {'success': True, 'message': '五等奖', 'level': 5}
    else:
        if number == 6:
            return {'success': True, 'message': '一等奖', 'level': 1}
        elif number == 5:
            return {'success': True, 'message': '三等奖', 'level': 3}
        elif number == 4:
            return {'success': True, 'message': '四等奖', 'level': 4}
        elif number == 3:
            return {'success': True, 'message': '五等奖', 'level': 5}
        elif number == 2:
            return {'success': True, 'message': '六等奖', 'level': 6}
        elif number == 1:
            return {'success': True, 'message': '六等奖', 'level': 6}
        elif number == 0:
            return {'success': True, 'message': '六等奖', 'level': 6}
    return {'success': False, 'message': '没有中奖', 'level': 0}


if __name__ == '__main__':
    count = 100
    proportion_list = {'一等奖': [], '二等奖': [], '三等奖': [], '四等奖': [], '五等奖': [], '六等奖': [], '没有中奖': []}
    for i in range(1, count+1):
        red_win, blue_win = random_money()
        red_mine, blue_mine = random_money()
        result = funds_level({'red': red_win, 'blue': blue_win}, {'red': red_mine, 'blue': blue_mine})
        proportion_list[result['message']].append({'level': result['level'],
                                                   'message': result['message'],
                                                   'mine': {'red': red_mine, 'blue': blue_mine},
                                                   'win': {'red': red_win, 'blue': blue_win}
                                                   })
    for key, value in proportion_list.items():
        print("%s 一共有%d个，中奖比例为:%f,分别是:%r" % (key,
                                             len(value),
                                             len(value)/count,
                                             [{'中奖号码': i['mine'], '开奖号码': i['win']} if i['level'] != 0 else '' for i in value]))
