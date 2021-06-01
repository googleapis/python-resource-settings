# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.resourcesettings_v1.services.resource_settings_service import pagers
from google.cloud.resourcesettings_v1.types import resource_settings
from .transports.base import ResourceSettingsServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import ResourceSettingsServiceGrpcAsyncIOTransport
from .client import ResourceSettingsServiceClient


class ResourceSettingsServiceAsyncClient:
    """An interface to interact with resource settings and setting values
    throughout the resource hierarchy.

    Services may surface a number of settings for users to control how
    their resources behave. Values of settings applied on a given Cloud
    resource are evaluated hierarchically and inherited by all
    descendants of that resource.

    For all requests, returns a ``google.rpc.Status`` with
    ``google.rpc.Code.PERMISSION_DENIED`` if the IAM check fails or the
    ``parent`` resource is not in a Cloud Organization. For all
    requests, returns a ``google.rpc.Status`` with
    ``google.rpc.Code.INVALID_ARGUMENT`` if the request is malformed.
    """

    _client: ResourceSettingsServiceClient

    DEFAULT_ENDPOINT = ResourceSettingsServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ResourceSettingsServiceClient.DEFAULT_MTLS_ENDPOINT

    setting_path = staticmethod(ResourceSettingsServiceClient.setting_path)
    parse_setting_path = staticmethod(ResourceSettingsServiceClient.parse_setting_path)
    common_billing_account_path = staticmethod(
        ResourceSettingsServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ResourceSettingsServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ResourceSettingsServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        ResourceSettingsServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        ResourceSettingsServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ResourceSettingsServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        ResourceSettingsServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        ResourceSettingsServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        ResourceSettingsServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        ResourceSettingsServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ResourceSettingsServiceAsyncClient: The constructed client.
        """
        return ResourceSettingsServiceClient.from_service_account_info.__func__(ResourceSettingsServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ResourceSettingsServiceAsyncClient: The constructed client.
        """
        return ResourceSettingsServiceClient.from_service_account_file.__func__(ResourceSettingsServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> ResourceSettingsServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            ResourceSettingsServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(ResourceSettingsServiceClient).get_transport_class,
        type(ResourceSettingsServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, ResourceSettingsServiceTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the resource settings service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.ResourceSettingsServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = ResourceSettingsServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_settings(
        self,
        request: resource_settings.ListSettingsRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListSettingsAsyncPager:
        r"""Lists all the settings that are available on the Cloud resource
        ``parent``.

        Args:
            request (:class:`google.cloud.resourcesettings_v1.types.ListSettingsRequest`):
                The request object. The request for ListSettings.
            parent (:class:`str`):
                Required. The Cloud resource that parents the setting.
                Must be in one of the following forms:

                -  ``projects/{project_number}``
                -  ``projects/{project_id}``
                -  ``folders/{folder_id}``
                -  ``organizations/{organization_id}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.resourcesettings_v1.services.resource_settings_service.pagers.ListSettingsAsyncPager:
                The response from ListSettings.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = resource_settings.ListSettingsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_settings,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListSettingsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_setting(
        self,
        request: resource_settings.GetSettingRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resource_settings.Setting:
        r"""Gets a setting.

        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.NOT_FOUND`` if the setting does not exist.

        Args:
            request (:class:`google.cloud.resourcesettings_v1.types.GetSettingRequest`):
                The request object. The request for GetSetting.
            name (:class:`str`):
                Required. The name of the setting to get. See
                [Setting][google.cloud.resourcesettings.v1.Setting] for
                naming requirements.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.resourcesettings_v1.types.Setting:
                The schema for settings.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = resource_settings.GetSettingRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_setting,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def update_setting(
        self,
        request: resource_settings.UpdateSettingRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resource_settings.Setting:
        r"""Updates a setting.

        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.NOT_FOUND`` if the setting does not exist.
        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.FAILED_PRECONDITION`` if the setting is
        flagged as read only. Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.ABORTED`` if the etag supplied in the request
        does not match the persisted etag of the setting value.

        On success, the response will contain only ``name``,
        ``local_value`` and ``etag``. The ``metadata`` and
        ``effective_value`` cannot be updated through this API.

        Note: the supplied setting will perform a full overwrite of the
        ``local_value`` field.

        Args:
            request (:class:`google.cloud.resourcesettings_v1.types.UpdateSettingRequest`):
                The request object. The request for UpdateSetting.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.resourcesettings_v1.types.Setting:
                The schema for settings.
        """
        # Create or coerce a protobuf request object.
        request = resource_settings.UpdateSettingRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_setting,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("setting.name", request.setting.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-resource-settings",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("ResourceSettingsServiceAsyncClient",)
