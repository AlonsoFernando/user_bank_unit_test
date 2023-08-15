from src.service.service_user import ServiceUser

service = ServiceUser()

result = service.add_user("Fabricio", "Engenheiro")
print(result)
for i in service.store.bd:
    print(i.name, " - ", i.job)
print("---------------------")

result = service.update_user("Fabricio", "Desenvolvedor")
print(result)
for i in service.store.bd:
    print(i.name, " - ", i.job)
print("---------------------")

result = service.get_user_by_name("Fabricio")
print(result.name, "-", result.job)
print("---------------------")

result = service.remove_user("Fabricio")
print(result)
print("---------------------")
