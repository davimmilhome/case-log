import os
from datetime import datetime


import pandas as pd

from models import DFBaseMonitoramentoEntregasModel

from cfg import ProjectDefinitions, LoggingConfig


from utils import PandasUtils


logger = LoggingConfig.get_active_logger(__name__)


def base_monitoramento_entregas_service() -> pd.DataFrame:

    input_path = os.path.join(
        ProjectDefinitions.getROOTDir(), "general_data_entry/input/"
    )
    file_name = "base_monitoramento_entregas.csv"
    complete_input_path = os.path.join(input_path, file_name)

    base_monitoramento_entregas = pd.read_csv(
        filepath_or_buffer=complete_input_path,
        sep=",",
        decimal=".",
        encoding="utf-8-sig",
        skiprows=0,  # Skipa a primeira linha do arquivo, cabecalho
    )

    base_monitoramento_entregas.columns = (
        DFBaseMonitoramentoEntregasModel.get_labels_alias()
    )

    logger.info(
        f"Tamnho da base antes do drop na: {base_monitoramento_entregas.shape[0]}"
    )
    base_monitoramento_entregas.dropna(inplace=True)
    logger.info(
        f"Tamnho da base após do drop na: {base_monitoramento_entregas.shape[0]}"
    )

    base_monitoramento_entregas["DATA_PEDIDO"] = pd.to_datetime(
        base_monitoramento_entregas["DATA_PEDIDO"],
        format="%Y-%m-%d",
        errors="coerce",
    )

    base_monitoramento_entregas["DATA_ENTREGA"] = pd.to_datetime(
        base_monitoramento_entregas["DATA_ENTREGA"],
        format="%Y-%m-%d",
        errors="coerce",
    )

    return base_monitoramento_entregas


if __name__ == "__main__":
    df = base_monitoramento_entregas_service()
    print(df.head(100))
    print(df.columns)
    print(df.dtypes)

    PandasUtils.output_csv_file(
        df,
        os.path.join(
            ProjectDefinitions.getROOTDir(),
            "general_data_entry/output/base_monitoramento_entregas_t.csv",
        ),
    )
