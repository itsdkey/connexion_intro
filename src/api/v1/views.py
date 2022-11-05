from flask.views import MethodView


def health_check() -> dict:
    return {"status": "OK"}


class CreatePostView(MethodView):
    def post(self, body: dict, **kwargs) -> tuple[dict, int]:
        return body, 201
