import torch.nn as nn

class MultiLabelModel(nn.Module):
    def __init__(self, basemodel, basemodel_output, num_classes):
        super(MultiLabelModel, self).__init__()
        self.basemodel = basemodel
        self.num_classes = num_classes
        for index, num_class in enumerate(num_classes):
            setattr(self, "FullyConnectedLayer_" + str(index), nn.Linear(basemodel_output, num_class))
    
    def forward(self, x):
        x = self.basemodel.forward(x)
        outs = list()
        dir(self)
        for index, num_class in enumerate(self.num_classes):
            fun = eval("self.FullyConnectedLayer_" + str(index))
            out = fun(x)
            outs.append(out)
        return outs


def BuildMultiLabelModel(basemodel, basemodel_output, num_classes):
    return MultiLabelModel(basemodel, basemodel_output, num_classes)
