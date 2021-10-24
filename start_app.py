from aiohttp import web
import logging
from aiohttp.abc import AbstractAccessLogger


class AccessLogger(AbstractAccessLogger):

    def log(self, request, response, time):
        self.logger.info(f'{request.remote} '
                         f'"{request.method} {request.path} '
                         # f'header {request.headers}'
                         f'query {request.query}'
                         f'done in {time}s: {response.status}')


# r"/v1/chats/{chat_id}/users"
from api.hendler import User_id

def setup_routes(app) -> None:
    app.router.add_view(r'/lib/{user_id}', User_id)


def main() -> None:

    app = web.Application()
    setup_routes(app)
    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app, access_log_class=AccessLogger, port=8081)


if __name__ == '__main__':
    main()
