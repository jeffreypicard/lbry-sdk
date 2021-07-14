# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import lbry.schema.types.v2.hub_pb2 as hub__pb2
import lbry.schema.types.v2.result_pb2 as result__pb2


class HubStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeHeaders = channel.unary_stream(
                '/pb.Hub/SubscribeHeaders',
                request_serializer=hub__pb2.BlockRequest.SerializeToString,
                response_deserializer=result__pb2.BlockHeaderOutput.FromString,
                )
        self.Search = channel.unary_unary(
                '/pb.Hub/Search',
                request_serializer=hub__pb2.SearchRequest.SerializeToString,
                response_deserializer=result__pb2.Outputs.FromString,
                )
        self.GetBlock = channel.unary_unary(
                '/pb.Hub/GetBlock',
                request_serializer=hub__pb2.BlockRequest.SerializeToString,
                response_deserializer=result__pb2.BlockOutput.FromString,
                )
        self.GetBlockHeader = channel.unary_unary(
                '/pb.Hub/GetBlockHeader',
                request_serializer=hub__pb2.BlockRequest.SerializeToString,
                response_deserializer=result__pb2.BlockHeaderOutput.FromString,
                )


class HubServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SubscribeHeaders(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockHeader(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HubServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeHeaders': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeHeaders,
                    request_deserializer=hub__pb2.BlockRequest.FromString,
                    response_serializer=result__pb2.BlockHeaderOutput.SerializeToString,
            ),
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=hub__pb2.SearchRequest.FromString,
                    response_serializer=result__pb2.Outputs.SerializeToString,
            ),
            'GetBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlock,
                    request_deserializer=hub__pb2.BlockRequest.FromString,
                    response_serializer=result__pb2.BlockOutput.SerializeToString,
            ),
            'GetBlockHeader': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockHeader,
                    request_deserializer=hub__pb2.BlockRequest.FromString,
                    response_serializer=result__pb2.BlockHeaderOutput.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.Hub', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Hub(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SubscribeHeaders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pb.Hub/SubscribeHeaders',
            hub__pb2.BlockRequest.SerializeToString,
            result__pb2.BlockHeaderOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Hub/Search',
            hub__pb2.SearchRequest.SerializeToString,
            result__pb2.Outputs.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Hub/GetBlock',
            hub__pb2.BlockRequest.SerializeToString,
            result__pb2.BlockOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlockHeader(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Hub/GetBlockHeader',
            hub__pb2.BlockRequest.SerializeToString,
            result__pb2.BlockHeaderOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
