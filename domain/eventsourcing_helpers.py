from typing import Optional
from domain.aggregate_root import AggregateRoot
from multipledispatch import dispatch
from domain.event_store import EventStore


@dispatch(EventStore, type, str)
def rebuild_aggregate(
    event_store: EventStore, aggregate_class: type, aggregate_id: str
):
    if not issubclass(aggregate_class, AggregateRoot):
        raise ValueError("Aggregate class must inherit from AggregateRoot.")

    aggregate = aggregate_class(aggregate_id)
    events = event_store.get_events_for_aggregate(aggregate_id)
    aggregate.load_from_history(events)
    return aggregate

@dispatch(EventStore, type, str, Optional[int])
def rebuild_aggregate(event_store, aggregate_class, aggregate_id, upto_version=None):
    if not issubclass(aggregate_class, AggregateRoot):
        raise ValueError("Aggregate class must inherit from AggregateRoot.")

    snapshot = event_store.get_latest_snapshot(aggregate_id)
    if snapshot:
        aggregate = aggregate_class(aggregate_id)
        aggregate.restore_from_snapshot(snapshot)
        starting_version = snapshot.version
    else:
        aggregate = aggregate_class(aggregate_id)
        starting_version = 0

    events = event_store.get_events_for_aggregate(aggregate_id, after_version=starting_version)
    for event in events:
        if upto_version is not None and event.version > upto_version:
            break
        aggregate.apply(event)

    return aggregate
