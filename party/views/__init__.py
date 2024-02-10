from .gift_registry_views import (
    GiftRegistryPage,
    GiftUpdateFormPartial,
    GiftDetailPartial,
    delete_gift_partial,
)  # UPDATED
from .new_party_views import (
    page_new_party,
    partial_check_party_date,
    partial_check_invitation,
)
from .party_details_views import PartyDetailPage, PartyDetailPartial
from .party_list_views import PartyListPage


__all__ = [
    "PartyListPage",
    "PartyDetailPage",
    "PartyDetailPartial",
    "page_new_party",
    "partial_check_party_date",
    "partial_check_invitation",
    "GiftRegistryPage",
    "GiftUpdateFormPartial",
    "GiftDetailPartial",
    "delete_gift_partial",  # NEW
]
