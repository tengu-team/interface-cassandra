# Cassandra Interface

 This is a Juju charm interface layer. This interface is used for
 connecting a client to the Cassandra Charm. Currently only the requires
 side is implemented, since the Cassandra charm is not yet a reactive 
 charm.

### Examples

#### Requires

If your charm needs to connect to Cassandra:

  `metadata.yaml`

```yaml
requires:
  datastore:
    interface: cassandra
```

  `layer.yaml`

```yaml
includes: ['interface:cassandra']
```  

  `reactive/code.py`

```python
@when('datastore.available')
def connect_to_cassandra(datastore):
    ds = datastore.get_configuration()
    print('{}/{}'.format(ds.host(), ds.rpc_port()))
)

```

# Contact Information

 - Gregory Van Seghbroeck <gregory.vanseghbroeck@tengu.io>
