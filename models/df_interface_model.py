from abc import abstractmethod


class DFInterfaceModel:

    @staticmethod
    def get_labels_relations():
        pass

    @abstractmethod
    def get_original_labels():
        pass

    @abstractmethod
    def get_labels_alias():
        pass
