from infrastructure.repositories.event_store import EventStore
from event_sourcing_sample.bank_account_aggregate import BankAccount
from event_sourcing_sample.helpers import rebuild_aggregate


def sample_usage():
    """
    This example simplifies many aspects of a real-world implementation, such as concurrency, event versioning, and snapshotting for performance. In practice, frameworks and libraries are often used to handle the complexity of event sourcing and aggregates, and the event store might be a database designed for event storage.
    """
    event_store = EventStore()

    # Create a new bank account
    bank_account = BankAccount(id="123")
    bank_account.create_account("John Doe")
    bank_account.deposit_money(100)

    # Persist changes (events) to the event store
    event_store.save_events(bank_account.id, bank_account.changes, expected_version=0)

    # Print history of events for auditing
    events = event_store.get_events_for_aggregate("123")
    print(f"Account History: \n")
    for event in events:
        print(
            f"Event Type: {event.type}, Data: {event.data}, Timestamp: {event.timestamp}"
        )

    # Rebuild the bank account's state from events
    reconstructed_account = rebuild_aggregate(event_store, "123")
    print(f"Reconstructed Account Balance: {reconstructed_account.balance}")


if __name__ == "__main__":
    sample_usage()
