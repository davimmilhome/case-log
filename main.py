import os

from services import base_monitoramento_entregas_service

from parsers import (
    monitoramento_entrega_parser,
    painel_erros_parser,
)

from utils import PandasUtils

from cfg import (
    LoggingConfig,
    ProjectDefinitions,
)


def run():

    base_monitoramento_entregas = base_monitoramento_entregas_service()
    base_monitoramento_entregas_parseado = monitoramento_entrega_parser(
        base_monitoramento_entregas
    )

    output_path_csv = os.path.join(
        ProjectDefinitions.getROOTDir(),
        "general_data_entry/output/base_monitoramento_entregas_parseada.csv",
    )
    PandasUtils.output_csv_file(
        base_monitoramento_entregas_parseado, output_path=output_path_csv
    )

    painel_erros_parseado = painel_erros_parser(base_monitoramento_entregas)

    output_path_csv = os.path.join(
        ProjectDefinitions.getROOTDir(),
        "general_data_entry/output/painel_erros_parseado.csv",
    )
    PandasUtils.output_csv_file(painel_erros_parseado, output_path=output_path_csv)

    return 0


if __name__ == "__main__":
    run()
