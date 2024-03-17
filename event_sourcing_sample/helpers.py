from typing import Optional
from domain.event_store import EventStore
from event_sourcing_sample.bank_account_aggregate import BankAccount
from multipledispatch import dispatch


@dispatch(EventStore, str)
def rebuild_aggregate(event_store: EventStore, aggregate_id: str):
    bank_account = BankAccount(aggregate_id)
    events = event_store.get_events_for_aggregate(aggregate_id)
    for event in events:
        print(f"Applying event: {event.type}")
        bank_account.apply(event)
    return bank_account


@dispatch(EventStore, str, int)
def rebuild_aggregate(
    event_store: EventStore, aggregate_id: str, upto_version: Optional[int] = None
):
    snapshot = event_store.get_latest_snapshot(aggregate_id)
    if snapshot:
        aggregate = snapshot.state
        starting_version = snapshot.version
    else:
        aggregate = BankAccount(aggregate_id)
        starting_version = 0
    events = event_store.get_events_for_aggregate(
        aggregate_id, after_version=starting_version
    )
    for event in events:
        if upto_version is not None and event.version > upto_version:
            break
        aggregate.apply(event)
    return aggregate
