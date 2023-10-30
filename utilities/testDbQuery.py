import dbManager

dbManager.createDbConnection()
data = dbManager.getMysqlQuery("select tutorial_author from selenium where tutorial_id = 2")
print(str(data))