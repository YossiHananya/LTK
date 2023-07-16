from sqlalchemy_schemadisplay import create_schema_graph
from sqlalchemy import create_engine, MetaData

if __name__ == "__main__":
    # Create a SQLite engine
    engine = create_engine("sqlite:///soccer_application/development.db")

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
    schema_graph.write_svg("db_schema.svg")
