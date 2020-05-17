from vk_api.longpoll import VkLongPoll, VkEventType

import vk_api, random, time, os, re

mytokenvk = os.environ.get('TOKEN_VK')
vk_session = vk_api.VkApi(token=mytokenvk)
longpull = VkLongPoll(vk_session)
vk = vk_session.get_api()
while True:
	response = vk.wall.get(count=4,
	owner_id= -171493284)
	#print(response)
	textlookfor=r"промо\s\w+"
	mask=re.findall(textlookfor, str(response))
	print(mask)
	if not (mask[-1]=='промо донат'):
		vk.messages.send(
	                            # chat_id= event.chat_id,
	                            peer_id= -171493284,
	                            message=mask,
	                            random_id=random.randint(0, 10000000000000000)
	                        )
	else:
			pass                        
	time.sleep(61)		
