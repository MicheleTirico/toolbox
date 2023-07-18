def test_package(a): print ("handfiles: packages has been imported\nrun run from toolbox.handlefiles import tools")

def storeDataframe(logger,pathStore,df):
    logger.log(cl=None,method=None,message="Store dataframe in:{}".format(pathStore))
    df.to_csv(pathStore, sep=';')


def dropValColumns(columns,listValToDrop):
    for i in listValToDrop:        columns.pop(columns.index(i))
    return columns
