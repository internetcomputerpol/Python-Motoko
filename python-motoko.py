from ic.client import Client 
from ic.identity import Identity
from ic.agent import Agent 
from ic.candid import encode, Types


urlad = 'https://ic0.app'
client = Client(url=urlad)

identity = Identity()
agent = Agent(identity,client)
canister_id = 'zydb5-siaaa-aaaab-qacba-cai' # W waszym przypadku id kanistra będzie inne

method_name = 'dataShow_update'
method_name_update = 'dataShow_query'
param = [ { 'type' : Types.Nat, 'value' : 10}]

result_update =  await agent.update_raw_async(canister_id,method_name,encode(param))
result_query = await agent.query_raw_async(canister_id,method_name_update,encode(param))


decode_value = result_update[0]['value']
decode_value_query = result_query[0]['value']
print(f" {decode_value_query}")
print(f" {decode_value}")

#Kod do Motoko Playground z kodem Kanistra ICP : https://m7sm4-2iaaa-aaaab-qabra-cai.ic0.app/?tag=2430116220


