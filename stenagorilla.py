from vk_api.longpoll import VkLongPoll, VkEventType

import vk_api, random, time, os, re

#mytokenvk = os.environ.get('0c0151147883a61fcc4cf73fd9255c0d53045071fb0697f8995c14294abfb1add34f73f7dd754112452bd')
vk_session = vk_api.VkApi(token='0c0151147883a61fcc4cf73fd9255c0d53045071fb0697f8995c14294abfb1add34f73f7dd754112452bd')
longpull = VkLongPoll(vk_session)
vk = vk_session.get_api()
while True:
	response = vk.wall.get(count=3,
	owner_id= -171493284)
	#print(response)
	textlookfor=r"промо\s\w+"
	mask=re.findall(textlookfor, str(response))
	print(mask)
	if not (mask[0]=='промо випка'):
		vk.messages.send(
	                            # chat_id= event.chat_id,
	                            peer_id= -171493284,
	                            message=mask,
	                            random_id=random.randint(0, 10000000000000000)
	                        )
	else:
			pass                        
	time.sleep(2)		