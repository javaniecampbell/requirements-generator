from domain.event_store import EventStore
from event_sourcing_sample.bank_account_aggregate import BankAccount


def rebuild_aggregate(event_store: EventStore, aggregate_id):
    bank_account = BankAccount(aggregate_id)
    events = event_store.get_events_for_aggregate(aggregate_id)
    for event in events:
        print(f"Applying event: {event.type}")
        bank_account.apply(event)
    return bank_account
