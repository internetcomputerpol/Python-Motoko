from ic.client import Client 
from ic.identity import Identity
from ic.agent import Agent
from ic.candid import encode,Types

 
ic_url = 'https://ic0.app'
client = Client(url=ic_url)
identity = Identity()
agent = Agent(identity,client)

canisterId = 'zkfwe-6yaaa-aaaab-qacca-cai'
methodName = 'dataShow'
methodNameUpdate = 'dataChage'
param = [ {'type': Types.Nat, 'value': 100}]

result = await agent.query_raw_async(canisterId,methodName,encode(param))
result_update = await agent.update_raw_async(canisterId,methodNameUpdate,encode(param))

result_nice = result[0]['value']
result_nice2 = result_update[0]['value']
print(f"Elegancko  {result_nice}") 
print(f"Elegancko  {result_nice2}") 
