import os
from dotenv import load_dotenv as ldt
from notion_client import Client
from pprint import pprint 
from modules.rushroyale_stats import RushRoyaleStats, Unit
 
import pdb

rr = RushRoyaleStats()
rr.create_units()

ldt(verbose=True)
ldt('.env')

token = os.environ.get('notion_api_key')
db_id = os.environ.get('notion_db_id_event_schedule_table')

client = Client(auth=token)
res = client.databases.query(
    **{
        "database_id": db_id
    }
)

page_id = "a"
pdb.set_trace()
res = client.blocks.children.list(
    **{
        "block_id": 'xxxxxxxxxxxx',
        "page_size": 1,
    }
)
pprint(res)

"""
for _u in rr.units.values():
    json = {}
    for _k, _v in vars(_u).items():
        if _k == 'images':
            continue
        elif _k == 'key':
            json[_k] = { 'title': [
                  { 'text': { 'content': _v } }
            ]}
        elif _k == 'toxic':
            json[_k] = {
                'type': 'checkbox',
                'checkbox': True,
            }
        else:
            json[_k] = {
                'type': 'rich_text',
                'rich_text': [{
                    'type': 'text',
                    'text': { 'content': _v }
                }]
            }
        json['updated_at'] = {
            'type': 'date',
            'date': {
                'end': None,
                'start': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'time_zone': 'Asia/Tokyo'
            }
        }
    response = client.pages.create(
        **{
            'parent': { 'database_id': db_id },
            'properties': json
        }
    )
"""
