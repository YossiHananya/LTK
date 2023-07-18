import os.path

from sqlalchemy_schemadisplay import create_schema_graph
from sqlalchemy import create_engine, MetaData
import argparse

from LTK.soccer_application.config.config import Config
from LTK.soccer_application.config.config_names import ConfigName


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create a schema graph of the database"
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="data/db_schema.svg",
        help="The output file name",
    )
    parser.add_argument(
        "--mode",
        "-m",
        type=str,
        default="dev",
        help="The mode to run the application in",
    )

    return parser.parse_args()


def get_db_name(mode):
    assert mode in [conf.value for conf in ConfigName], "Invalid mode"

    config_file = Config(os.path.join("..", "soccer_application", "config", f"{mode}.yaml"))
    return config_file.get("APP_CONFIG")["DATABASE_URI"]


if __name__ == "__main__":
    args = parse_args()

    # Create a SQLite engine
    engine = create_engine(f"sqlite:///soccer_application/{get_db_name(args.mode)}")

    metadata = MetaData()
    metadata.reflect(bind=engine)

    # Create the schema graph figure
    schema_graph = create_schema_graph(
        metadata=metadata,
        show_datatypes=True,
        show_indexes=False,
        rankdir="LR",
    )

    # Save the figure to a file
    schema_graph.write_svg(args.output)
