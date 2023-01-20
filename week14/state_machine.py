from state_machine import (State, Event, acts_as_state_machine, after, before, InvalidStateTransition)


@acts_as_state_machine
class Process:
    checkout = State(initial=True)
    payment = State()
    pending = State()
    confirmed = State()
    canceled = State()

    # define transitions
    payment_info = Event(from_states=checkout, to_state=payment)
    submit_order = Event(from_states=payment,to_state=pending)
    disapprove = Event(from_states=pending,to_state=checkout)
    approve = Event(from_states=pending,to_state=confirmed)
    cancel = Event(from_states=confirmed,to_state=cancelled)