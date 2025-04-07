""""""

import os
from datetime import datetime
from datetime import timedelta

import pandas as pd
import numpy as np

from cfg import LoggingConfig, ProjectDefinitions

from utils import (
    PandasUtils,
)


#######################################################################
# CFG
#######################################################################

logger = LoggingConfig.get_active_logger(__name__)

# Pandas
pd.set_option("display.max_columns", None)
pd.options.mode.chained_assignment = None  # default='warn', retira avisos


def painel_erros_parser(base_monitoramento_entregas: pd.DataFrame) -> pd.DataFrame:

    painel_erros_parseado = base_monitoramento_entregas.copy()

    # Como o tipo é TIME observar que vai considerar NAT
    mascara_data_pedido_nat = painel_erros_parseado["DATA_PEDIDO"].isna()

    painel_erros_parseado = painel_erros_parseado[mascara_data_pedido_nat]

    colunas_inconsistentes_para_limpeza = [
        "PRAZO_ENTREGA_DIAS",
        "DATA_ENTREGA",
        "AVALIACAO_CLIENTE",
        "TEMPO_TRANSITO_DIAS",
    ]

    painel_erros_parseado.loc[
        mascara_data_pedido_nat, colunas_inconsistentes_para_limpeza
    ] = None

    logger.info(f"Tamnho do painel de erros: {painel_erros_parseado.shape[0]}")

    return painel_erros_parseado


if __name__ == "__main__":
    from services import base_monitoramento_entregas_service

    df = base_monitoramento_entregas_service()
    df = painel_erros_parser(df)
    print(df.head())

    output_path_csv = os.path.join(
        ProjectDefinitions.getROOTDir(),
        "general_data_entry/output/painel_erros_parseado.csv",
    )
    PandasUtils.output_csv_file(df, output_path=output_path_csv)
