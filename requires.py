#!/usr/bin/env python3
# Copyright (C) 2017  Qrama, developed by Tengu-team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# pylint: disable=c0111,c0301,c0325, r0903,w0406
from charms.reactive import hook, RelationBase, scopes


class CassandraRequires(RelationBase):
    scope = scopes.UNIT

    @hook('{requires:cassandra}-relation-joined')
    def joined(self):
        for conv in self.conversations():
            conv.remove_state('{relation_name}.removed')
            conv.set_state('{relation_name}.connected')

    @hook('{requires:cassandra}-relation-changed')
    def changed(self):
        for conv in self.conversations():
            conv.set_state('{relation_name}.available')

    @hook('{requires:cassandra}-relation-{departed,broken}')
    def broken(self):
        for conv in self.conversations():
            conv.remove_state('{relation_name}.connected')
            conv.remove_state('{relation_name}.available')
            conv.set_state('{relation_name}.removed')

    def get_configuration(self):
        for conv in self.conversations():
            yield {
                'username': conv.get_remote('username'),
                'password': conv.get_remote('password'),
                'host': conv.get_remote('private-address'),
                'native_transport_port': conv.get_remote('native_transport_port'),
                'rpc_port': conv.get_remote('rpc_port'),
                'cluster_name': conv.get_remote('cluster_name'),
                'datacenter': conv.get_remote('datacenter'),
                'rack': conv.get_remote('rack'),
                }
