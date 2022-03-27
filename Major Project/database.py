import pyodbc
server = 'inventory-management.database.windows.net'
database = 'inventorydb'
username = 'Project'
password = 'Inventory@1234'   
driver='{ODBC Driver 13 for SQL Server}'
mysql = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)



