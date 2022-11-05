import prance


def get_bundled_specs(main_file: str):
    parser = prance.ResolvingParser(
        main_file,
        lazy=True,
        strict=True,
        backend="openapi-spec-validator",
    )
    parser.parse()
    return parser.specification
