import copy
import json
from aiohttp import web
from NeirinNetwork import network



class User_id(web.View):

    async def get(self):
        try:
            user_id = self.request.match_info['user_id']
            pred = network.pred_fun(int(user_id))
            pred_list = []
            tmp_dict = dict()
            for i in pred:
                print(i)
                tmp_dict['id'] = i
                tmp_dict['title'],tmp_dict['author'] = network.get_full_information_by_id(i)
                pred_list.append(copy.copy(tmp_dict))
            history = network.get_history_list(int(user_id))
            history_list = []
            tmp_dict = dict()
            for i in history:
                tmp_dict['id'] = i
                tmp_dict['title'], tmp_dict['author'] = network.get_full_information_by_id(i)
                history_list.append(copy.copy(tmp_dict))
            result = {
                "recommendations": pred_list,
                "history":history_list
            }
            return web.Response(status=200, body=json.dumps(result),
                                content_type='application/json')
        except Exception as e:
            print(e)
            return web.Response(status=500, body=json.dumps({'message' : 'Error'}),
                                content_type='application/json')

