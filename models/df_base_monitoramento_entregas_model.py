from models import DFInterfaceModel


class DFBaseMonitoramentoEntregasModel(DFInterfaceModel):

    __labels_relation = {
        "ID_Pedido": "ID_PEDIDO",
        "Data_Pedido": "DATA_PEDIDO",
        "Prazo_Entrega_Dias": "PRAZO_ENTREGA_DIAS",
        "Tempo_Transito_Dias": "TEMPO_TRANSITO_DIAS",
        "Data_Entrega": "DATA_ENTREGA",
        "Regiao": "REGIAO",
        "Transportadora": "TRANSPORTADORA",
        "Status_Pedido": "STATUS_PEDIDO",
        "Avaliacao_Cliente": "AVALIACAO_CLIENTE",
    }

    @staticmethod
    def get_labels_relations():
        return DFBaseMonitoramentoEntregasModel.__labels_relation

    @staticmethod
    def get_original_labels():
        original_labels = list(
            DFBaseMonitoramentoEntregasModel.__labels_relation.keys()
        )
        return original_labels

    @staticmethod
    def get_labels_alias():
        labels_alias = list(DFBaseMonitoramentoEntregasModel.__labels_relation.values())
        return labels_alias


if __name__ == "__main__":
    print(
        DFBaseMonitoramentoEntregasModel.get_labels_alias(),
        type(DFBaseMonitoramentoEntregasModel.get_labels_alias()),
    )
    pass
