import connexion
from connexion.resolver import MethodViewResolver

from src.utils.specification import get_bundled_specs


def create_app() -> connexion.App:
    app = connexion.FlaskApp(__name__, specification_dir='openapi/')

    # One big api YML
    # app.add_api(
    #     'api.yml',
    #     resolver=MethodViewResolver("src.api.v1.views"),
    # )

    # api YML sliced into parts
    app.add_api(
        get_bundled_specs("./openapi/v1.yml"),
        validate_responses=True,
        resolver=MethodViewResolver("src.api.v1.views"),
    )
    return app


app = create_app()
flask_app = app.app

if __name__ == "__main__":
    app.run(port=8080, debug=True)
