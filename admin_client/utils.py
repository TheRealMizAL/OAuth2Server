import httpx
from httpx import USE_CLIENT_DEFAULT

from .schemas import HttpsUrl

http_client = httpx.AsyncClient()

menu = [
    {
        "name": "Главная",
        "collapse_id": "main-collapse",
        "items": {
            "Дашбоард": "main-dashboard",
            "Журналы": "journals-dashboard",
        }
    },
    {
        "name": "Управление",
        "collapse_id": "control-collapse",
        "items": {
            "Пользователи": "accounts-dashboard",
            "Группы": "groups-dashboard",
            "Клиенты": "clients-dashboard",
            "Ресурсы": "resources-dashboard",
            "Политики": "policies-dashboard"
        }
    },
    {
        "name": "Консоли",
        "collapse_id": "consoles-collapse",
        "items": dict()
    }
]


async def resolve_server(*, server_id=None, server_name=None) -> (str, str):
    if not (server_id or server_name):
        pass


async def send_webhook(*,
                       server_id=None,
                       server_name=None,
                       content=None,
                       data=None,
                       files=None,
                       json=None,
                       params=None,
                       headers=None,
                       cookies=None,
                       auth=USE_CLIENT_DEFAULT,
                       follow_redirects=USE_CLIENT_DEFAULT,
                       timeout=USE_CLIENT_DEFAULT,
                       extensions=None, ):
    url, method = await resolve_server(server_id=server_id, server_name=server_name)

    await http_client.request(method=method,
                              url=url,
                              content=content,
                              data=data,
                              files=files,
                              json=json,
                              params=params,
                              headers=headers,
                              cookies=cookies,
                              auth=auth,
                              follow_redirects=follow_redirects,
                              timeout=timeout,
                              extensions=extensions)


async def inject_console(server_path: HttpsUrl, token: str):
    server_meta = (
        await http_client.get(f'{server_path}/discover', headers={'Authorization': f'Bearer {token}'})).json()
    if console_path := server_meta.get('console', None):
        console_html = (await http_client.get(f'{server_path}/{console_path}',
                                              headers={'Authorization': f'Bearer {token}'})).text
        global menu
        menu[2]['items'][server_meta['server_id']] = {
            'name': server_meta['name'],
            'console': console_html
        }
    return None
