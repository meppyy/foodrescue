# FoodRescue — Functional Requirements

## 2.1 Functional Requirements

### 2.1.1 Authentication & User Management

The system shall provide authentication and user-management functionality for all registered users.

#### Registration

FR-AUTH-01: The system shall allow a new user to register an account.

FR-AUTH-02: The system shall collect the information required for creating a user account.

FR-AUTH-03: The system shall assign a role to the user during registration or account setup.

FR-AUTH-04: The system shall validate the information provided during registration.

#### Login and Logout

FR-AUTH-05: The system shall allow registered users to log in using their credentials.

FR-AUTH-06: The system shall authenticate users before granting access to protected functionality.

FR-AUTH-07: The system shall allow authenticated users to log out of the system.

#### Role-Based Access

FR-AUTH-08: The system shall support the following user roles:

- Donor
- Recipient
- Volunteer
- Administrator

FR-AUTH-09: The system shall restrict access to role-specific functionality according to the user's assigned role.

FR-AUTH-10: The system shall prevent unauthorized users from accessing protected functionality.

#### Password Management

FR-AUTH-11: The system shall provide functionality for password management.

FR-AUTH-12: The system shall securely store user passwords.

#### Profile Management

FR-AUTH-13: The system shall allow users to view their profile information.

FR-AUTH-14: The system shall allow users to update permitted profile information.

#### Account Status

FR-AUTH-15: The system shall maintain the status of each user account.

FR-AUTH-16: The system shall allow authorized administrators to manage user account status.

#### Recipient Verification

FR-AUTH-17: The system shall support administrator approval or rejection of recipient registrations where verification is required.

FR-AUTH-18: The system shall prevent unapproved recipients from accessing functionality that requires recipient eligibility.


### 2.1.2 Food Surplus Listing Management

The system shall provide functionality for donors to create, manage, and monitor surplus-food listings.

#### Creating Food Listings

FR-FOOD-01: The system shall allow authorized donors to create a surplus-food listing.

FR-FOOD-02: The system shall require the donor to provide the food name.

FR-FOOD-03: The system shall allow the donor to specify the food category.

FR-FOOD-04: The system shall allow the donor to specify the available quantity.

FR-FOOD-05: The system shall allow the donor to specify the unit associated with the quantity.

FR-FOOD-06: The system shall allow the donor to specify the food preparation time.

FR-FOOD-07: The system shall record the listing time.

FR-FOOD-08: The system shall allow the donor to specify the expiry or use-by time.

FR-FOOD-09: The system shall allow the donor to specify the dietary type, such as vegetarian or non-vegetarian.

FR-FOOD-10: The system shall allow the donor to provide packaging information.

FR-FOOD-11: The system shall allow the donor to specify the pickup location.

FR-FOOD-12: The system shall allow the donor to provide a description of the food.

FR-FOOD-13: The system shall allow the donor to specify special handling requirements where applicable.

#### Listing Validation

FR-FOOD-14: The system shall validate the information entered before creating a food listing.

FR-FOOD-15: The system shall prevent invalid or incomplete listings from becoming available.

#### Listing Management

FR-FOOD-16: The system shall allow donors to view their active food listings.

FR-FOOD-17: The system shall allow authorized donors to edit eligible food-listing information.

FR-FOOD-18: The system shall allow donors to cancel an available listing before allocation.

#### Listing Status

FR-FOOD-19: The system shall maintain the current status of every food listing.

FR-FOOD-20: The system shall support the following food-listing statuses:

- Draft
- Available
- Requested
- Allocated
- Pickup Pending
- Collected
- Delivered
- Expired
- Cancelled

FR-FOOD-21: The system shall update the listing status when relevant actions or workflow events occur.

FR-FOOD-22: The system shall prevent cancelled or expired listings from receiving new requests.


### 2.1.3 Search and Filtering

The system shall provide eligible recipients with functionality to search, browse, and filter available food listings.

#### Browsing Available Food

FR-SEARCH-01: The system shall allow eligible recipients to view available food listings.

FR-SEARCH-02: The system shall display relevant food-listing information when a listing is viewed.

FR-SEARCH-03: The system shall display only listings that are currently available for requesting.

#### Search

FR-SEARCH-04: The system shall allow users to search available food listings using relevant food information.

FR-SEARCH-05: The system shall return food listings that match the user's search criteria.

#### Filtering

FR-SEARCH-06: The system shall allow users to filter food listings by food category.

FR-SEARCH-07: The system shall allow users to filter food listings by dietary type, such as vegetarian or non-vegetarian.

FR-SEARCH-08: The system shall allow users to filter food listings by available quantity.

FR-SEARCH-09: The system shall allow users to filter food listings by location or distance.

FR-SEARCH-10: The system shall allow users to filter food listings by expiry urgency.

FR-SEARCH-11: The system shall allow users to filter food listings by availability status.

FR-SEARCH-12: The system shall allow users to filter food listings by listing date.

#### Sorting

FR-SEARCH-13: The system shall allow users to sort available food listings by expiry time, with the soonest expiry appearing first.

FR-SEARCH-14: The system shall allow users to sort available food listings by proximity.

FR-SEARCH-15: The system shall allow users to sort available food listings by quantity.

FR-SEARCH-16: The system shall allow users to sort available food listings by listing date, with newer listings appearing first.

#### Listing Details

FR-SEARCH-17: The system shall allow an eligible recipient to view the details of a selected food listing before submitting a request.

FR-SEARCH-18: The system shall prevent users from requesting a listing that is no longer available.


### 2.1.4 Rule-Based Food Prioritization

The system shall provide a transparent rule-based mechanism for determining the priority of available food listings.

#### Priority Calculation

FR-PRIORITY-01: The system shall calculate a priority level for an available food listing using predefined rules.

FR-PRIORITY-02: The system shall consider the time remaining before food expiry as a priority factor.

FR-PRIORITY-03: The system shall consider the quantity of food available as a priority factor.

FR-PRIORITY-04: The system shall consider the food category as a priority factor where applicable.

FR-PRIORITY-05: The system shall consider geographic distance as a priority factor.

FR-PRIORITY-06: The system shall consider recipient suitability as a priority factor.

FR-PRIORITY-07: The system shall consider the age of the food listing as a priority factor.

#### Priority Classification

FR-PRIORITY-08: The system shall classify food listings into the following priority levels:

- High Priority
- Medium Priority
- Low Priority

FR-PRIORITY-09: The system shall assign a higher priority to listings requiring more urgent redistribution based on the predefined rules.

FR-PRIORITY-10: The system shall make the factors contributing to a listing's priority understandable to authorized users.

#### Rule-Based Operation

FR-PRIORITY-11: The prioritization mechanism shall use predefined rules rather than Machine Learning or Artificial Intelligence models.

FR-PRIORITY-12: The system shall apply the same defined prioritization rules consistently to eligible food listings.

FR-PRIORITY-13: The prioritization rules shall be configurable during system development where necessary.



### 2.1.5 Recipient Matching

The system shall provide a rule-based mechanism to identify recipients who may be suitable for a particular surplus-food listing.

#### Eligibility Check

FR-MATCH-01: The system shall identify recipients who are eligible to receive the selected food listing.

FR-MATCH-02: The system shall exclude recipients whose accounts have not been approved where recipient verification is required.

#### Matching Criteria

FR-MATCH-03: The system shall consider food type or category when identifying suitable recipients.

FR-MATCH-04: The system shall consider dietary compatibility when identifying suitable recipients.

FR-MATCH-05: The system shall consider the quantity required by the recipient.

FR-MATCH-06: The system shall consider the recipient's capacity when identifying suitable matches.

FR-MATCH-07: The system shall consider geographic proximity between the food listing and the recipient.

FR-MATCH-08: The system shall consider recipient availability when identifying suitable matches.

FR-MATCH-09: The system shall consider the expiry urgency of the food listing when evaluating potential matches.

#### Match Ranking

FR-MATCH-10: The system shall evaluate potential recipients using the defined matching criteria.

FR-MATCH-11: The system shall rank suitable recipients according to the predefined matching rules.

FR-MATCH-12: The system shall display the resulting suitable recipient matches to authorized users.

#### Rule-Based Operation

FR-MATCH-13: The recipient matching mechanism shall use predefined rules rather than Machine Learning or Artificial Intelligence models.

FR-MATCH-14: The system shall apply the defined matching criteria consistently to eligible food listings and recipients.

FR-MATCH-15: The system shall not recommend recipients who fail mandatory eligibility or compatibility requirements.



### 2.1.6 Request and Allocation Management

The system shall provide functionality for recipients to request available surplus food and for authorized users to review, approve, reject, and allocate those requests.

#### Food Requests

FR-REQUEST-01: The system shall allow an eligible recipient to submit a request for an available food listing.

FR-REQUEST-02: The system shall allow the recipient to specify the quantity requested.

FR-REQUEST-03: The system shall record the time at which a request is submitted.

FR-REQUEST-04: The system shall associate each request with the corresponding food listing and recipient.

FR-REQUEST-05: The system shall prevent requests from being submitted for expired or cancelled food listings.

FR-REQUEST-06: The system shall prevent a recipient from requesting more food than the available quantity.

#### Request Review

FR-REQUEST-07: The system shall allow authorized donors to view requests submitted for their food listings.

FR-REQUEST-08: The system shall allow authorized administrators to monitor food requests.

FR-REQUEST-09: The system shall allow an authorized donor or administrator to approve a request.

FR-REQUEST-10: The system shall allow an authorized donor or administrator to reject a request.

FR-REQUEST-11: The system shall allow a recipient to cancel a request where cancellation is permitted by the current request state.

#### Request Status

FR-REQUEST-12: The system shall maintain the status of each food request.

FR-REQUEST-13: The system shall support the following request statuses:

- Pending
- Approved
- Rejected
- Cancelled
- Allocated
- Completed
- Expired

FR-REQUEST-14: The system shall update the request status when relevant workflow actions occur.

#### Allocation

FR-REQUEST-15: The system shall create an allocation for an approved food request.

FR-REQUEST-16: The system shall associate an allocation with the approved request.

FR-REQUEST-17: The system shall ensure that the allocated quantity does not exceed the available quantity of the food listing.

FR-REQUEST-18: The system shall prevent the same available food quantity from being allocated to multiple recipients beyond the available amount.

FR-REQUEST-19: The system shall record the volunteer assigned to an allocation where pickup or delivery assistance is required.

FR-REQUEST-20: The system shall record relevant pickup and delivery information associated with the allocation.

#### Allocation Status

FR-REQUEST-21: The system shall maintain the status of each allocation.

FR-REQUEST-22: The system shall update the allocation status as the pickup and delivery workflow progresses.

FR-REQUEST-23: The system shall prevent an allocation from being completed unless the required preceding workflow steps have been completed.



### 2.1.7 Pickup and Delivery Management

The system shall provide functionality for coordinating and tracking the physical collection and delivery of allocated surplus food.

#### Volunteer Assignment

FR-DELIVERY-01: The system shall allow an authorized user to assign a volunteer to an approved allocation when pickup or delivery assistance is required.

FR-DELIVERY-02: The system shall consider volunteer availability when assigning a volunteer.

FR-DELIVERY-03: The system shall allow volunteers to view their assigned pickup and delivery tasks.

FR-DELIVERY-04: The system shall allow a volunteer to accept an available assignment.

FR-DELIVERY-05: The system shall allow a volunteer to reject an assignment where permitted.

#### Pickup Coordination

FR-DELIVERY-06: The system shall allow relevant users to view pickup details associated with an allocation.

FR-DELIVERY-07: The system shall allow a pickup to be scheduled for an allocated food request.

FR-DELIVERY-08: The system shall allow the volunteer to update the status of the pickup.

FR-DELIVERY-09: The system shall allow the volunteer to confirm that food has been collected.

#### Delivery Coordination

FR-DELIVERY-10: The system shall allow the volunteer to view the delivery details associated with an allocation.

FR-DELIVERY-11: The system shall allow the volunteer to update the delivery status.

FR-DELIVERY-12: The system shall allow the volunteer to confirm that the food has been delivered.

FR-DELIVERY-13: The system shall allow the recipient to confirm receipt of the delivered food.

#### Delivery Status

FR-DELIVERY-14: The system shall maintain the current status of each pickup and delivery assignment.

FR-DELIVERY-15: The system shall support the following assignment statuses:

- Unassigned
- Assigned
- Pickup Scheduled
- Picked Up
- In Transit
- Delivered
- Failed
- Cancelled

FR-DELIVERY-16: The system shall update the assignment status when relevant pickup or delivery actions occur.

#### Workflow Validation

FR-DELIVERY-17: The system shall prevent a delivery from being marked as completed before pickup has been confirmed.

FR-DELIVERY-18: The system shall handle failed or cancelled pickup and delivery assignments.

FR-DELIVERY-19: The system shall allow an assignment to become unassigned when an assigned volunteer becomes unavailable and reassignment is required.

FR-DELIVERY-20: The system shall record completed pickup and delivery activities in the relevant transaction history.



### 2.1.8 Food Expiry Management

The system shall monitor the expiry or use-by time of active food listings and take appropriate actions when food becomes close to expiry or expires.

#### Expiry Monitoring

FR-EXPIRY-01: The system shall record the expiry or use-by time of each food listing.

FR-EXPIRY-02: The system shall periodically check the expiry status of active food listings.

FR-EXPIRY-03: The system shall compare the current system time with the expiry time of active food listings.

#### Expiry Classification

FR-EXPIRY-04: The system shall identify food listings according to their remaining time before expiry.

FR-EXPIRY-05: The system shall classify listings with more than 24 hours remaining as Normal.

FR-EXPIRY-06: The system shall classify listings with 6 to 24 hours remaining as Attention.

FR-EXPIRY-07: The system shall classify listings with less than 6 hours remaining as Urgent.

FR-EXPIRY-08: The system shall classify listings whose expiry time has passed as Expired.

#### Expired Listings

FR-EXPIRY-09: The system shall automatically mark an expired food listing as Expired.

FR-EXPIRY-10: The system shall prevent new requests from being submitted for expired listings.

FR-EXPIRY-11: The system shall prevent expired food from being allocated to a new recipient.

FR-EXPIRY-12: The system shall identify pending requests affected by an expired food listing.

FR-EXPIRY-13: The system shall cancel affected pending requests when required by the applicable workflow rules.

#### Notifications and Warnings

FR-EXPIRY-14: The system shall provide urgency warnings for food listings approaching expiry.

FR-EXPIRY-15: The system shall notify relevant users when a food listing expires.

FR-EXPIRY-16: The system shall notify affected users when an active request or allocation is affected by food expiry.

#### Expiry Consistency

FR-EXPIRY-17: The system shall ensure that expired or unavailable food cannot re-enter the active requesting workflow unless explicitly handled by an authorized system process.

FR-EXPIRY-18: The system shall record expiry-related status changes in the relevant system history.



### 2.1.9 Notification Management

The system shall provide an in-app notification mechanism to inform users about important events and changes related to their activities.

#### Notification Generation

FR-NOTIFY-01: The system shall generate notifications when predefined system events occur.

FR-NOTIFY-02: The system shall associate each notification with the relevant user.

FR-NOTIFY-03: The system shall record the message, notification type, read status, and creation time for each notification.

#### Donor Notifications

FR-NOTIFY-04: The system shall notify a donor when a new request is submitted for one of their food listings.

FR-NOTIFY-05: The system shall notify a donor when a request for their food listing is approved or rejected.

FR-NOTIFY-06: The system shall notify a donor when a volunteer is assigned to an approved allocation.

FR-NOTIFY-07: The system shall notify a donor when the pickup has been completed.

FR-NOTIFY-08: The system shall notify a donor when one of their food listings is approaching expiry.

#### Recipient Notifications

FR-NOTIFY-09: The system shall notify a recipient when their food request is approved.

FR-NOTIFY-10: The system shall notify a recipient when a volunteer is assigned to the relevant allocation.

FR-NOTIFY-11: The system shall notify a recipient when the food has been collected.

FR-NOTIFY-12: The system shall notify a recipient when delivery has been completed.

FR-NOTIFY-13: The system shall notify a recipient when a relevant food listing or request is cancelled.

#### Volunteer Notifications

FR-NOTIFY-14: The system shall notify a volunteer when a new pickup assignment is created.

FR-NOTIFY-15: The system shall notify a volunteer when a pickup or delivery time requires attention.

FR-NOTIFY-16: The system shall notify a volunteer when an assignment is cancelled or changed.

#### Notification Management

FR-NOTIFY-17: The system shall allow users to view their notifications.

FR-NOTIFY-18: The system shall indicate whether a notification has been read or remains unread.

FR-NOTIFY-19: The system shall allow users to mark notifications as read.

FR-NOTIFY-20: The system shall display relevant notifications according to the user's role and system activity.

FR-NOTIFY-21: The initial implementation shall provide notifications through the application interface.

FR-NOTIFY-22: External notification channels such as SMS and WhatsApp shall not be required for the initial implementation.



### 2.1.10 Role-Specific Dashboards

The system shall provide dashboards that display information and statistics relevant to the user's role.

#### Donor Dashboard

FR-DASH-01: The system shall provide donors with a dashboard displaying their active food listings.

FR-DASH-02: The system shall display the number of pending requests associated with the donor's listings.

FR-DASH-03: The system shall display the number of completed donations.

FR-DASH-04: The system shall display the number of expired food listings.

FR-DASH-05: The system shall display the total quantity of food successfully redistributed by the donor.

#### Recipient Dashboard

FR-DASH-06: The system shall provide recipients with a dashboard displaying available food listings.

FR-DASH-07: The system shall display the recipient's pending requests.

FR-DASH-08: The system shall display the recipient's approved requests.

FR-DASH-09: The system shall display the amount or number of food allocations received by the recipient.

FR-DASH-10: The system shall provide recipients with access to their request history.

#### Volunteer Dashboard

FR-DASH-11: The system shall provide volunteers with a dashboard displaying their assigned pickup and delivery tasks.

FR-DASH-12: The system shall display the volunteer's pending tasks.

FR-DASH-13: The system shall display the number of completed deliveries.

FR-DASH-14: The system shall display failed or cancelled assignments where applicable.

FR-DASH-15: The system shall provide volunteers with access to their completed assignment history.

#### Administrator Dashboard

FR-DASH-16: The system shall provide administrators with an overview of system activity.

FR-DASH-17: The system shall display the total number of registered users.

FR-DASH-18: The system shall display the number of active donors.

FR-DASH-19: The system shall display the number of active recipients.

FR-DASH-20: The system shall display the number of active volunteers.

FR-DASH-21: The system shall display the number of active food listings.

FR-DASH-22: The system shall display the number of successful redistributions.

FR-DASH-23: The system shall display the amount of expired food.

FR-DASH-24: The system shall display the total quantity of food rescued or redistributed.

FR-DASH-25: The system shall display the number of completed deliveries.

FR-DASH-26: The system shall display the number of failed transactions or redistributions.

#### Dashboard Access

FR-DASH-27: The system shall display dashboard information according to the authenticated user's role.

FR-DASH-28: The system shall prevent users from accessing dashboards belonging to other roles unless explicitly authorized.

FR-DASH-29: The system shall update dashboard statistics based on the current system data.



### 2.1.11 Impact Tracking

The system shall maintain records and statistics that allow the impact of surplus-food redistribution activities to be measured.

#### Impact Metrics

FR-IMPACT-01: The system shall track the total quantity of food listed through the platform.

FR-IMPACT-02: The system shall track the total quantity of food successfully redistributed.

FR-IMPACT-03: The system shall track the total quantity of food that expired without successful redistribution.

FR-IMPACT-04: The system shall track the number of successful food donations.

FR-IMPACT-05: The system shall track the number of recipient organizations or groups served.

FR-IMPACT-06: The system shall track the number of completed food pickups.

FR-IMPACT-07: The system shall track the number of completed food deliveries.

#### Impact Reporting

FR-IMPACT-08: The system shall make relevant impact statistics available to authorized users.

FR-IMPACT-09: The system shall display impact statistics on the appropriate dashboards.

FR-IMPACT-10: The system shall calculate impact statistics from recorded system transactions rather than manually entered values.

FR-IMPACT-11: The system shall update impact statistics when relevant food-listing, allocation, pickup, or delivery transactions are completed.

FR-IMPACT-12: The system shall maintain historical records required for calculating and reviewing redistribution impact.


### 2.1.12 Administration

The system shall provide administrators with functionality to supervise users, listings, requests, allocations, and other system activities.

#### User Management

FR-ADMIN-01: The system shall allow authorized administrators to view registered users.

FR-ADMIN-02: The system shall allow authorized administrators to manage donor accounts.

FR-ADMIN-03: The system shall allow authorized administrators to manage recipient accounts.

FR-ADMIN-04: The system shall allow authorized administrators to manage volunteer accounts.

FR-ADMIN-05: The system shall allow authorized administrators to manage user account status.

#### Recipient Verification

FR-ADMIN-06: The system shall allow administrators to review recipient registrations requiring verification.

FR-ADMIN-07: The system shall allow administrators to approve recipient registrations.

FR-ADMIN-08: The system shall allow administrators to reject recipient registrations.

FR-ADMIN-09: The system shall maintain the verification status of recipient accounts.

#### Food Listing Management

FR-ADMIN-10: The system shall allow administrators to view food listings across the system.

FR-ADMIN-11: The system shall allow administrators to monitor the status of food listings.

FR-ADMIN-12: The system shall allow administrators to remove invalid or inappropriate food listings.

#### Request and Allocation Monitoring

FR-ADMIN-13: The system shall allow administrators to monitor food requests.

FR-ADMIN-14: The system shall allow administrators to monitor food allocations.

FR-ADMIN-15: The system shall allow administrators to monitor the progress of pickup and delivery activities.

FR-ADMIN-16: The system shall allow administrators to review failed or cancelled redistribution transactions.

#### Issue and Dispute Management

FR-ADMIN-17: The system shall allow administrators to review reported issues or disputes.

FR-ADMIN-18: The system shall allow authorized administrators to take appropriate administrative action on reported issues.

#### System Data Management

FR-ADMIN-19: The system shall allow administrators to manage food categories used by the system.

FR-ADMIN-20: The system shall allow administrators to manage relevant system-level data and settings where permitted.

#### Monitoring and Reporting

FR-ADMIN-21: The system shall provide administrators with access to system statistics.

FR-ADMIN-22: The system shall allow administrators to view successful and failed redistribution activities.

FR-ADMIN-23: The system shall allow administrators to view impact statistics.

FR-ADMIN-24: The system shall provide administrators with access to relevant system reports.

#### Administrative Authorization

FR-ADMIN-25: The system shall restrict administrative functionality to authenticated users with administrator privileges.

FR-ADMIN-26: The system shall record relevant administrative actions where audit tracking is required.