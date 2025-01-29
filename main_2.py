import vk_api

def get_vk_session(token):
    vk_session = vk_api.VkApi(token=token)
    return vk_session.get_api()