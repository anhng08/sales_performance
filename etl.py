import pandas as pd
from sqlalchemy import create_engine
from column_mapping import COLUMN_MAPPING

FILE_PATH = "Dev_Campaigns.xlsx"

DB_URI = "postgresql+psycopg2://user:password@host:port/dbname"

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def apply_mapping(df: pd.DataFrame, mapping: dict) -> pd.DataFrame:
    df = normalize_columns(df)

    rename_dict = {
        col: mapping.get(col, col)
        for col in df.columns
    }

    df = df.rename(columns=rename_dict)

    return df


def validate_columns(df: pd.DataFrame, required_columns: list):
    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise ValueError(f" Missing columns: {missing}")


REQUIRED_SCHEMA = {
    "sales": [
        "order_id",
        "order_date",
        "customer_id",
        "product_id",
        "region_id",
        "quantity",
        "revenue",
        "cost"
    ],
    "customers": ["customer_id", "customer_name"],
    "products": ["product_id", "product_name"],
    "regions": ["region_id"],
    "campaigns": ["campaign_name"]
}


def process_sheet(df, sheet_name):
    print(f" Processing sheet: {sheet_name}")

    df = apply_mapping(df, COLUMN_MAPPING[sheet_name])

    validate_columns(df, REQUIRED_SCHEMA[sheet_name])

    return df


def main():
    sheets = pd.read_excel(FILE_PATH, sheet_name=None)

    engine = create_engine(DB_URI)

    SHEET_MAP = {
        "Sales Orders": "sales",
        "Customers": "customers",
        "Products": "products",
        "Regions": "regions",
        "Marketing Campaigns": "campaigns"
    }

    for sheet_excel, sheet_key in SHEET_MAP.items():
        df = sheets[sheet_excel]

        try:
            df_clean = process_sheet(df, sheet_key)

            table_name = f"{sheet_key}"

            df_clean.to_sql(
                table_name,
                engine,
                if_exists="replace",
                index=False
            )

            print(f" Loaded {table_name}")

        except Exception as e:
            print(f" Error in sheet {sheet_excel}: {e}")


if __name__ == "__main__":
    main()