from typing import Optional
from infrastructure.repositories.event_store_repository import EventStore
from event_sourcing_sample.bank_account_aggregate import BankAccount
from multipledispatch import dispatch


@dispatch(EventStore, str)
def rebuild_aggregate(event_store: EventStore, aggregate_id: str):
    """
    Rebuilds the bank account aggregate by applying all the events associated with the given aggregate ID.

    Args:
        event_store (EventStore): The event store containing the events.
        aggregate_id (str): The ID of the aggregate to rebuild.

    Returns:
        BankAccount: The rebuilt bank account aggregate.
    """
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
    """
    Rebuilds the bank aggregate by applying events from the event store associated with the given aggregate ID and upto the given version.

    Args:
        event_store (EventStore): The event store containing the events.
        aggregate_id (str): The ID of the aggregate to rebuild.
        upto_version (Optional[int], optional): The maximum version of events to apply. Defaults to None.

    Returns:
        The rebuilt aggregate.
    """
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
