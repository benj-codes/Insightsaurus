from storages.backends.azure_storage import AzureStorage

class AzureStaticStorage(AzureStorage):
    account_name = 'c0011865insightsaurus'
    account_key = 'T5nBDBBRn/mryCaIrlW2ROiEVPR3jjJBgkOLBy6tH108N+DXls17oTf7Z3bI63WgOo8avFMdfiSp+AStWrs93w=='
    azure_container = 'static'
    expiration_secs = None

class AzureMediaStorage(AzureStorage):
    account_name = 'c0011865insightsaurus'
    account_key = 'T5nBDBBRn/mryCaIrlW2ROiEVPR3jjJBgkOLBy6tH108N+DXls17oTf7Z3bI63WgOo8avFMdfiSp+AStWrs93w=='
    azure_container = 'media'
    expiration_secs = None