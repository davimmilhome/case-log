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


def monitoramento_entrega_parser(
    base_monitoramento_entregas: pd.DataFrame, retornar_painel_de_erros=False
) -> pd.DataFrame:

    base_monitoramento_entregas_parseada = base_monitoramento_entregas.copy()

    logger.info(
        f"Tamnho da base antes do drop de DATA na: {base_monitoramento_entregas_parseada.shape[0]}"
    )
    base_monitoramento_entregas_parseada.dropna(subset=["DATA_PEDIDO"], inplace=True)
    logger.info(
        f"Tamnho da base depois do drop de DATA na: {base_monitoramento_entregas_parseada.shape[0]}"
    )

    mascara_data_pedido_preenchido = base_monitoramento_entregas_parseada[
        "DATA_PEDIDO"
    ].notna()

    base_monitoramento_entregas_parseada["STATUS_PEDIDO"] = np.where(
        mascara_data_pedido_preenchido,
        "Entregue",
        "Cancelado",
    )

    base_monitoramento_entregas_parseada["DATA_PEDIDO"] = (
        base_monitoramento_entregas_parseada["DATA_PEDIDO"].dt.strftime("%d/%m/%Y")
    )

    base_monitoramento_entregas_parseada.loc[
        mascara_data_pedido_preenchido, "DATA_ENTREGA"
    ] = pd.to_datetime(
        base_monitoramento_entregas_parseada.loc[
            mascara_data_pedido_preenchido, "DATA_ENTREGA"
        ],
        format="%d/%m/%Y",
        errors="coerce",
    )

    base_monitoramento_entregas_parseada["DIFERENCA_PRAZO_TRANSITO"] = (
        base_monitoramento_entregas_parseada["PRAZO_ENTREGA_DIAS"]
        - base_monitoramento_entregas_parseada["TEMPO_TRANSITO_DIAS"]
    )

    base_monitoramento_entregas_parseada["STATUS_PRAZO_ENTREGA"] = np.where(
        base_monitoramento_entregas_parseada["DIFERENCA_PRAZO_TRANSITO"] < 0,
        "Fora do prazo",
        "Dentro do prazo",
    )

    condicoes = [
        base_monitoramento_entregas_parseada["AVALIACAO_CLIENTE"] == 1,
        base_monitoramento_entregas_parseada["AVALIACAO_CLIENTE"].isin([2, 3]),
        base_monitoramento_entregas_parseada["AVALIACAO_CLIENTE"] == 4,
        base_monitoramento_entregas_parseada["AVALIACAO_CLIENTE"] == 5,
    ]

    categorias_satisfacao = [
        "Insatisfeito",
        "Pouco Satisfeito",
        "Satisfeito",
        "Muito Satisfeito",
    ]

    base_monitoramento_entregas_parseada["CATEGORIA_SATISFACAO"] = np.select(
        condicoes, categorias_satisfacao, default=None
    )

    return base_monitoramento_entregas_parseada


if __name__ == "__main__":
    from services import base_monitoramento_entregas_service

    df = base_monitoramento_entregas_service()
    df = monitoramento_entrega_parser(df)
    print(df.head())

    output_path_csv = os.path.join(
        ProjectDefinitions.getROOTDir(),
        "general_data_entry/output/base_monitoramento_entregas_parseada.csv",
    )
    PandasUtils.output_csv_file(df, output_path=output_path_csv)
