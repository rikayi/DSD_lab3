import hazelcast

client = hazelcast.HazelcastClient(
    cluster_name="dev",
    cluster_members=[
        "127.0.0.1:5701",
        "127.0.0.1:5702",
        "127.0.0.1:5703",
    ]
)
my_map = client.get_map("lab3_4kndddfj")
key='1'
my_map.put_if_absent(key, 0)
print('starting')
for i in range(10):
    my_map.lock(key).result()
    try:
        value = my_map.get(key).result()
        print(value)
        value = int(value) + 1
        my_map.set(key, value)
    finally:
        my_map.unlock(key)

print("Pessimistic locking Finished! Result = " + str(my_map.get(key).result()))
