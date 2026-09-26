# FoodRescue — Core System Logic

## 5.1 Food Listing Lifecycle

The Food Listing Lifecycle defines how a surplus-food listing moves through the FoodRescue system from creation to final completion, expiry, or cancellation.

The lifecycle is controlled through validation, business rules, request activity, allocation, pickup, delivery, and expiry events.

### 5.1.1 Listing States

A food listing may have the following states:

- Draft
- Available
- Requested
- Allocated
- Pickup Pending
- Collected
- Delivered
- Expired
- Cancelled

### 5.1.2 Listing Lifecycle

The normal lifecycle is:

Draft
    ↓
Available
    ↓
Requested
    ↓
Allocated
    ↓
Pickup Pending
    ↓
Collected
    ↓
Delivered

Alternative terminal states include:

Available → Cancelled
Available → Expired
Requested → Expired
Requested → Cancelled
Pickup Pending → Expired
Pickup Pending → Cancelled

### 5.1.3 State Transition Rules

#### Draft → Available

A listing may move from Draft to Available when:

1. The donor submits the listing.
2. Required information is present.
3. Listing validation succeeds.
4. The listing has a valid expiry/use-by time.
5. The listing is made available for requesting.

#### Available → Requested

A listing moves to Requested when a valid request is submitted for it.

#### Requested → Allocated

A listing moves to Allocated when an eligible request is approved and the corresponding allocation is created.

#### Allocated → Pickup Pending

A listing moves to Pickup Pending when allocation is established and pickup coordination begins.

#### Pickup Pending → Collected

A listing moves to Collected when the volunteer confirms that the food has been collected.

#### Collected → Delivered

A listing moves to Delivered when delivery is confirmed.

#### Available → Cancelled

A donor may cancel an available listing before allocation.

#### Available / Requested / Pickup Pending → Expired

A listing becomes Expired when its expiry time has passed.

#### Cancellation and Expiry Restrictions

A Cancelled or Expired listing shall not accept new requests.

### 5.1.4 Listing Validation

Before a listing becomes Available, the system shall validate:

- Food name
- Food category
- Quantity
- Unit
- Preparation time
- Expiry/use-by time
- Dietary type
- Pickup location
- Required listing information

The system shall reject incomplete or invalid listings.

### 5.1.5 Quantity Management

The available quantity of a listing shall be maintained throughout the request and allocation workflow.

The system shall ensure that:

- A recipient cannot request more than the available quantity.
- Allocated quantity does not exceed available quantity.
- The same available quantity cannot be allocated to multiple recipients beyond what is available.

### 5.1.6 Expiry Interaction

The listing lifecycle shall interact with the expiry-management process.

If the expiry time is reached:

1. The listing shall be marked Expired.
2. New requests shall be prevented.
3. Affected pending requests shall be identified.
4. Affected requests shall be handled according to the expiry workflow.
5. Relevant users shall be notified.

### 5.1.7 Listing Lifecycle Pseudocode

```
CREATE LISTING
    ↓
VALIDATE LISTING
    ↓
IF valid
    → status = AVAILABLE
ELSE
    → remain INVALID / reject submission

WHEN request received
    → status = REQUESTED

WHEN request approved AND allocation created
    → status = ALLOCATED

WHEN pickup coordination begins
    → status = PICKUP_PENDING

WHEN pickup confirmed
    → status = COLLECTED

WHEN delivery confirmed
    → status = DELIVERED

AT ANY APPLICABLE ACTIVE STATE
    IF expiry time reached
        → status = EXPIRED

IF donor cancels before allocation
    → status = CANCELLED
```

### 5.1.8 Lifecycle Invariants

The following conditions shall remain true throughout the lifecycle:

1. Expired listings cannot receive new requests.
2. Cancelled listings cannot receive new requests.
3. Allocated quantity cannot exceed available quantity.
4. A listing cannot be marked Delivered before pickup has been completed.
5. Completed transactions shall not be arbitrarily modified by ordinary users.
6. Every listing shall have a valid current status.

### 5.1.9

The Food Listing Lifecycle interacts with:

- Food Listing Management
- Search and Filtering
- Prioritization
- Recipient Matching
- Request and Allocation
- Pickup and Delivery
- Expiry Management
- Notification Management
- Impact Tracking